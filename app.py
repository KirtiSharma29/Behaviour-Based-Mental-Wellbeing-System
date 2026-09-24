from datetime import datetime
import pandas as pd

from flask import Flask, render_template, request, redirect, url_for, flash, Response
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from config import Config
from database.db import db
from database.models import User, Prediction
from utils.ml import load_model, simple_suggestion
from utils.reports import predictions_to_csv, summary_stats


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    login_manager = LoginManager(app)
    login_manager.login_view = "login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ✅ Load ONLY one model file
    model, model_error = load_model(app.config["MODEL_PATH"])

    def current_model_error():
        return model_error

    @app.get("/")
    def index():
        return redirect(url_for("home" if current_user.is_authenticated else "login"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("home"))

        if request.method == "POST":
            email = (request.form.get("email") or "").strip().lower()
            password = request.form.get("password") or ""
            user = User.query.filter_by(email=email).first()

            if not user or not user.check_password(password):
                flash("Invalid email or password", "error")
                return render_template("auth/login.html", title="Login")

            login_user(user)
            flash("Logged in successfully", "success")
            return redirect(url_for("home"))

        return render_template("auth/login.html", title="Login")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for("home"))

        if request.method == "POST":
            name = (request.form.get("name") or "").strip()
            email = (request.form.get("email") or "").strip().lower()
            password = request.form.get("password") or ""

            if len(password) < 6:
                flash("Password must be at least 6 characters", "error")
                return render_template("auth/register.html", title="Register")

            if User.query.filter_by(email=email).first():
                flash("Email already registered. Please login.", "error")
                return redirect(url_for("login"))

            u = User(name=name, email=email)
            u.set_password(password)
            db.session.add(u)
            db.session.commit()

            login_user(u)
            flash("Account created successfully", "success")
            return redirect(url_for("home"))

        return render_template("auth/register.html", title="Register")

    @app.get("/logout")
    @login_required
    def logout():
        logout_user()
        flash("Logged out", "success")
        return redirect(url_for("login"))

    @app.get("/home")
    @login_required
    def home():
        return render_template("pages/home.html", title="Home", model_error=current_model_error())

    @app.get("/about")
    @login_required
    def about():
        return render_template("pages/about.html", title="About")

    @app.route("/prediction", methods=["GET", "POST"])
    @login_required
    def prediction():
        result = None

        if request.method == "POST":
            if model is None:
                flash("Model not loaded. Put best_emotion_model.pkl inside /models folder.", "error")
                return render_template("pages/prediction.html", title="Prediction", result=None, model_error=current_model_error())

            try:
                attention_level = int(request.form["attention_level"])
                mood_score = int(request.form["mood_score"])
                stress_level = int(request.form["stress_level"])
                interaction_level = int(request.form["interaction_level"])
                task_engagement = int(request.form["task_engagement"])
                trigger_noise = int(request.form["trigger_noise"])
                trigger_social = int(request.form["trigger_social"])
                routine_change = int(request.form["routine_change"])

                now = datetime.now()

                # ✅ IMPORTANT: Use the SAME column names as training
                row = {
                    "Child_ID": 1,
                    "Attention_Level": attention_level,
                    "Mood_Score": mood_score,
                    "Stress_Level": stress_level,
                    "Interaction_Level": interaction_level,
                    "Task_Engagement": task_engagement,
                    "Trigger_Noise": trigger_noise,
                    "Trigger_Social": trigger_social,
                    "Routine_Change": routine_change,
                    "obs_hour": now.hour,
                    "obs_dayofweek": now.weekday(),
                }

                # ✅ Convert to DataFrame (best practice for sklearn pipelines)
                X = pd.DataFrame([row])
                pred = model.predict(X)[0]

                sugg = simple_suggestion(
                    str(pred),
                    stress_level=stress_level,
                    triggers={
                        "Trigger_Noise": bool(trigger_noise),
                        "Trigger_Social": bool(trigger_social),
                        "Routine_Change": bool(routine_change),
                    },
                )

                rec = Prediction(
                    user_id=current_user.id,
                    attention_level=attention_level,
                    mood_score=mood_score,
                    stress_level=stress_level,
                    interaction_level=interaction_level,
                    task_engagement=task_engagement,
                    trigger_noise=trigger_noise,
                    trigger_social=trigger_social,
                    routine_change=routine_change,
                    predicted_emotion=str(pred),
                    suggestion=sugg,
                )
                db.session.add(rec)
                db.session.commit()

                result = rec
                flash("Prediction saved to history", "success")

            except Exception as e:
                flash(f"Prediction failed: {e}", "error")

        return render_template("pages/prediction.html", title="Prediction", result=result, model_error=current_model_error())

    @app.get("/history")
    @login_required
    def history():
        rows = (
            Prediction.query.filter_by(user_id=current_user.id)
            .order_by(Prediction.created_at.desc())
            .limit(500)
            .all()
        )
        return render_template("pages/history.html", title="History", rows=rows)

    @app.get("/report")
    @login_required
    def report():
        rows = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.created_at.desc()).all()
        stats = summary_stats(rows)
        return render_template("pages/report.html", title="Report", stats=stats)

    @app.get("/report/download.csv")
    @login_required
    def download_report_csv():
        rows = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.created_at.asc()).all()
        csv_text, _ = predictions_to_csv(rows)
        filename = f"prediction_report_{current_user.id}.csv"
        return Response(csv_text, mimetype="text/csv", headers={"Content-Disposition": f"attachment; filename={filename}"})

    return app

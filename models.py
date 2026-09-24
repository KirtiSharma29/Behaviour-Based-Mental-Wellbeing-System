from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db import db

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

class Prediction(db.Model):
    __tablename__ = "predictions"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)

    attention_level = db.Column(db.Integer, nullable=False)
    mood_score = db.Column(db.Integer, nullable=False)
    stress_level = db.Column(db.Integer, nullable=False)
    interaction_level = db.Column(db.Integer, nullable=False)
    task_engagement = db.Column(db.Integer, nullable=False)

    trigger_noise = db.Column(db.Integer, nullable=False, default=0)
    trigger_social = db.Column(db.Integer, nullable=False, default=0)
    routine_change = db.Column(db.Integer, nullable=False, default=0)

    predicted_emotion = db.Column(db.String(40), nullable=False)
    suggestion = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    user = db.relationship("User", backref=db.backref("predictions", lazy=True))

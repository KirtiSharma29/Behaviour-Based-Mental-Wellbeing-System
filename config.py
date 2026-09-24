import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-please")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(INSTANCE_DIR, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ✅ Only one model file
    MODEL_PATH = os.path.join(BASE_DIR, "models", "best_emotion_model.pkl")

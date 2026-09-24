import os
import joblib

def load_model(model_path: str):
    if not os.path.exists(model_path):
        return None, (
            "Model file not found. Place your trained model file here:\n"
            f"  - {model_path}\n"
            "Then restart the app."
        )
    model = joblib.load(model_path)
    return model, None


def simple_suggestion(emotion: str, stress_level: int, triggers: dict):
    tips = []
    if triggers.get("Routine_Change"):
        tips.append("Reduce sudden routine changes; introduce changes gradually.")
    if triggers.get("Trigger_Noise"):
        tips.append("Provide a quieter space or noise-cancelling support.")
    if triggers.get("Trigger_Social"):
        tips.append("Limit overwhelming social exposure; prefer small-group interaction.")

    if emotion == "Happy":
        core = "Encourage the same activity pattern; reinforce positive behaviour with praise."
    elif emotion == "Calm":
        core = "Maintain consistency; continue supportive routine and gentle engagement."
    elif emotion == "Stressed":
        core = "Offer a short break, breathing exercise, and simplify tasks into smaller steps."
    elif emotion == "Anxious":
        core = "Use reassurance, predictable schedule, and guided calming activities."
    else:
        core = "Monitor behaviour and provide supportive guidance."

    if stress_level >= 4:
        tips.append("Try structured relaxation: 5-min breathing + hydration + calm corner.")
    if not tips:
        tips.append("Maintain a supportive environment and track behaviour changes daily.")

    return core + " " + " ".join(tips)

import io
import pandas as pd

def predictions_to_csv(pred_rows):
    data = []
    for r in pred_rows:
        data.append({
            "created_at": r.created_at.isoformat(sep=" ", timespec="seconds"),
            "attention_level": r.attention_level,
            "mood_score": r.mood_score,
            "stress_level": r.stress_level,
            "interaction_level": r.interaction_level,
            "task_engagement": r.task_engagement,
            "trigger_noise": r.trigger_noise,
            "trigger_social": r.trigger_social,
            "routine_change": r.routine_change,
            "predicted_emotion": r.predicted_emotion,
            "suggestion": r.suggestion,
        })
    df = pd.DataFrame(data)
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    return buf.getvalue(), len(df)

def summary_stats(pred_rows):
    if not pred_rows:
        return {"total": 0, "most_common_emotion": None, "avg_stress": None}
    total = len(pred_rows)
    emotions = [p.predicted_emotion for p in pred_rows]
    most_common = pd.Series(emotions).value_counts().idxmax()
    avg_stress = round(float(pd.Series([p.stress_level for p in pred_rows]).mean()), 2)
    return {"total": total, "most_common_emotion": most_common, "avg_stress": avg_stress}

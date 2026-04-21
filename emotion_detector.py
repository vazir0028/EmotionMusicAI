import cv2
from deepface import DeepFace

def detect_emotion(frame):
    try:
        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False
        )

        if isinstance(result, list):
            result = result[0]

        emotion = result["dominant_emotion"]
        confidence = result["emotion"][emotion]

        return emotion, round(confidence, 2)

    except Exception:
        return "neutral", 0

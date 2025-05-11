# app/webcam_analysis.py
import cv2
from deepface import DeepFace

def analyze_webcam_frame():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        return {
            "dominant_emotion": analysis[0]["dominant_emotion"],
            "emotion_scores": analysis[0]["emotion"]
        }
    else:
        return {"error": "Failed to access webcam."}

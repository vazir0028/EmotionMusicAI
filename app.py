import streamlit as st
import cv2
import numpy as np

from emotion_detector import detect_emotion
from spotify_api import login_spotify, play_music

st.set_page_config(page_title="Emotion Music AI", layout="centered")

st.title("🎧 Emotion Based Music Recommendation")
st.write("Capture image → Detect mood → Auto play Spotify music")

sp = login_spotify()

img = st.camera_input("Take a selfie")

if img:
    bytes_data = img.getvalue()
    np_arr = np.frombuffer(bytes_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    emotion, confidence = detect_emotion(frame)

    st.success(f"Detected Emotion: {emotion.upper()}")
    st.info(f"Confidence: {confidence}%")

    if st.button("▶ Play Music"):
        ok = play_music(sp, emotion)

        if ok:
            st.success("Spotify music started!")
        else:
            st.error("No active Spotify device found. Open Spotify app first.")

from st_audiorec import st_audiorec
import streamlit as st
import wave
import os

def process_audio():
    raw_audio_bytes = st_audiorec()

    if raw_audio_bytes is not None:
        output_dir = os.getcwd()
        filename = "../recorded_audio.wav"
        file_path = os.path.join(output_dir, filename)
        with wave.open(file_path, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(96000)
            wf.writeframes(raw_audio_bytes)
        return file_path

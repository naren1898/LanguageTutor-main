import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import av
import wave
import os


def process_audio():
    output_dir = "audio_output"
    filename = "recorded_audio.raw"
    file_path = os.path.join(output_dir, filename)
    class AudioProcessor(AudioProcessorBase):
        initialized = False
        def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
            try:
                if not AudioProcessor.initialized:
                    os.makedirs(output_dir, exist_ok=True)
                    with open(file_path, "wb"):
                        pass
                    AudioProcessor.initialized = True
                else:
                    with open(file_path, "ab") as f:
                        f.write(frame.to_ndarray().tobytes())
            except Exception as e:
                print(f"AudioProcessor error: {e}")
            return frame

    # WebRTC Streamer UI
    ctx = webrtc_streamer(
        key="audio",
        mode=WebRtcMode.SENDONLY,
        audio_processor_factory=AudioProcessor,
        media_stream_constraints={"audio": True, "video": False}
    )
    with open("audio_output/recorded_audio.raw", "rb") as raw_file:
        raw_data = raw_file.read()

    with wave.open("audio_output/recorded_audio.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(96000)
        wf.writeframes(raw_data)
    return file_path

process_audio()


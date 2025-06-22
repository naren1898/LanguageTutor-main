from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import av
import streamlit as st
import wave
import os


def process_audio():
    output_dir = os.getcwd()
    #"C:\\Users\\naren\\Downloads\\LanguageTutor-main\\pages\\audio_output"
    #os.getcwd()
    print(output_dir)
    #print(st.session_state)
    filename = "recorded_audio.raw"
    file_path = os.path.join(output_dir, filename)
    file_path1 = os.path.join(output_dir, "recorded_audio.wav")
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

    #print(st.session_state)
    if ctx and ctx.state.playing is False and os.path.exists(file_path):
        with open(file_path, "rb") as raw_file:
            raw_data = raw_file.read()

        with wave.open(file_path1, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(96000)
            wf.writeframes(raw_data)
        return file_path1


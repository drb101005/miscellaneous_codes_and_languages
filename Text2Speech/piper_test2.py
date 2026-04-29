import sounddevice as sd
import numpy as np
from huggingface_hub import hf_hub_download
from piper.voice import PiperVoice

# 1. Download both files to the SAME directory
REPO_ID = "rhasspy/piper-voices"
MODEL_FILE = "en/en_US/lessac/medium/en_US-lessac-medium.onnx"
CONFIG_FILE = "en/en_US/lessac/medium/en_US-lessac-medium.onnx.json"

model_path = hf_hub_download(repo_id=REPO_ID, filename=MODEL_FILE)
config_path = hf_hub_download(repo_id=REPO_ID, filename=CONFIG_FILE)

# 2. Load the voice (This takes a second, but we only do it once)
voice = PiperVoice.load(model_path, config_path=config_path)

# 3. Setup the real-time audio stream
# This stays open so we can pipe audio into it instantly
stream = sd.OutputStream(
    samplerate=voice.config.sample_rate,
    channels=1,
    dtype='int16'
)
stream.start()

def speak(text):
    print(f"Jarvis: {text}")
    # synthesize_stream_raw yields chunks as they are generated
    for audio_bytes in voice.synthesize_stream_raw(text):
        int_data = np.frombuffer(audio_bytes, dtype=np.int16)
        stream.write(int_data)

# Test it out
speak("Hello Sir. I am now streaming audio locally without the loading lag.")

# Keep the stream open for the next sentence
# stream.stop() # Only call this when you close Jarvis
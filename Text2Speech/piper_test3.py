import sounddevice as sd
import numpy as np
import re
from huggingface_hub import hf_hub_download
from piper.voice import PiperVoice

# 1. Load ONCE
REPO_ID = "rhasspy/piper-voices"
MODEL_FILE = "en/en_US/lessac/medium/en_US-lessac-medium.onnx"
CONFIG_FILE = "en/en_US/lessac/medium/en_US-lessac-medium.onnx.json"

model_path = hf_hub_download(repo_id=REPO_ID, filename=MODEL_FILE)
config_path = hf_hub_download(repo_id=REPO_ID, filename=CONFIG_FILE)

voice = PiperVoice.load(model_path, config_path=config_path)

def speak(text):
    # Split text into sentences so we can play them one by one
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    for sentence in sentences:
        if not sentence.strip():
            continue
            
        print(f"Jarvis is speaking: {sentence}")
        
        # In this version, we collect the bytes for the current sentence
        audio_data = b""
        for audio_bytes in voice.synthesize(sentence):
            audio_data += audio_bytes
        
        # Convert to numpy and play immediately
        audio_np = np.frombuffer(audio_data, dtype=np.int16)
        sd.play(audio_np, samplerate=voice.config.sample_rate)
        sd.wait() # Waits for the current sentence to finish before starting the next

# Test
speak("Hello Sir. I have fixed the error. I will now process your requests sentence by sentence to keep latency low.")
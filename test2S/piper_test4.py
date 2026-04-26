import sounddevice as sd
import numpy as np
import re
from huggingface_hub import hf_hub_download
from piper.voice import PiperVoice

# 1. Setup & Load (Do this once)
REPO_ID = "rhasspy/piper-voices"
MODEL_FILE = "en/en_US/lessac/medium/en_US-lessac-medium.onnx"
CONFIG_FILE = "en/en_US/lessac/medium/en_US-lessac-medium.onnx.json"

model_path = hf_hub_download(repo_id=REPO_ID, filename=MODEL_FILE)
config_path = hf_hub_download(repo_id=REPO_ID, filename=CONFIG_FILE)

voice = PiperVoice.load(model_path, config_path=config_path)

def speak(text):
    # Split text into sentences for low latency
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    for sentence in sentences:
        if not sentence.strip():
            continue
            
        print(f"Jarvis is speaking: {sentence}")
        
        # Piper's synthesize returns a generator of AudioChunk objects
        audio_data = b""
        for chunk in voice.synthesize(sentence):
            # FIXED: Access the raw bytes within the AudioChunk object
            audio_data += chunk.audio
        
        # Convert raw PCM bytes (int16) to a numpy array for sounddevice
        audio_np = np.frombuffer(audio_data, dtype=np.int16)
        
        # Play the audio
        sd.play(audio_np, samplerate=voice.config.sample_rate)
        sd.wait() # Ensures the sentence finishes before the next one starts

# Test it
speak("Hello Sir. I have fixed the type error. I am now accessing the audio attribute directly from the piper chunks.")
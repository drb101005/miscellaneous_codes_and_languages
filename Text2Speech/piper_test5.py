import sounddevice as sd
import numpy as np
import re
from huggingface_hub import hf_hub_download
from piper.voice import PiperVoice

# 1. Setup & Load
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
            
        print(f"Jarvis: {sentence}")
        
        audio_data = b""
        for chunk in voice.synthesize(sentence):
            # In some versions, chunk is bytes. In others, it's an object.
            if isinstance(chunk, bytes):
                audio_data += chunk
            elif hasattr(chunk, 'audio_int16_bytes'):
                audio_data += chunk.audio_int16_bytes
            else:
                # If both fail, this is the most likely attribute name in older versions
                audio_data += chunk.audio_data 
        
        # Convert raw PCM bytes (int16) to a numpy array
        audio_np = np.frombuffer(audio_data, dtype=np.int16)
        
        # Play the audio
        sd.play(audio_np, samplerate=voice.config.sample_rate)
        sd.wait() 

# Test
speak("Hello Sir. I have corrected the attribute name. I am now checking for bytes or the int 16 audio attribute.")
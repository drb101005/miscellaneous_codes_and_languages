import sounddevice as sd
import numpy as np
from huggingface_hub import hf_hub_download
from piper import PiperVoice

model_path = hf_hub_download(
    repo_id="rhasspy/piper-voices",
    filename="en/en_US/lessac/medium/en_US-lessac-medium.onnx"
)

config_path = hf_hub_download(
    repo_id="rhasspy/piper-voices",
    filename="en/en_US/lessac/medium/en_US-lessac-medium.onnx.json"
)

voice = PiperVoice.load(model_path, config_path)

chunks = []
for chunk in voice.synthesize("Helllooooo"):
    chunks.append(chunk.audio_float_array)   # ✅ correct field

audio = np.concatenate(chunks)

sd.play(audio, samplerate=voice.config.sample_rate)
sd.wait()
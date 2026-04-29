import sounddevice as sd
from kokoro_onnx import Kokoro

# Initialize model (this will download model on first run)
model = Kokoro()

text = "Hello, this is Jarvis speaking."

# Generate audio
audio, sample_rate = model.create(text)

# Play audio
sd.play(audio, samplerate=sample_rate)
sd.wait()
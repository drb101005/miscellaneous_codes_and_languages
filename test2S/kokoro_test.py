from kokoro_tts import KPipeline
import sounddevice as sd

pipeline = KPipeline(lang_code='a')

text = "Hello, this is Jarvis speaking."

for _, _, audio in pipeline(text, voice='af_sarah'):
    sd.play(audio, samplerate=24000)
    sd.wait()
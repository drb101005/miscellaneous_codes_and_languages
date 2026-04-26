from gtts import gTTS
from playsound import playsound

text = "Hello, this is Jarvis speaking."

tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

playsound("output.mp3")
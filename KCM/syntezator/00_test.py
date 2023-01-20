import os
from gtts import gTTS

import playsound

def speak(txt):
    tts = gTTS(text=txt, lang='en')
    filename = "voicePl.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

speak("hello, how are you today? What's your name?")
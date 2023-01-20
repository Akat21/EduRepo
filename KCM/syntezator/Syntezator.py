import pyaudio
from googletrans import Translator
import speech_recognition as sr
import playsound
from gtts import gTTS
import os

def recognize():
    r = sr.Recognizer()
    r.energy_threshold = 800
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = r.recognize_google(audio, language="pl_PL")
    save(said)
    return said

def speak(txt):
    filename = save(txt)
    playsound.playsound(filename)

def save(txt):
    tts = gTTS(text=txt, lang='pl')
    filename = "voicePl.mp3"
    tts.save(filename)
    return filename

def translate(txt):
    translator = Translator()
    txt = "Ładna dziś pogoda"
    translated = translator.translate(txt)
    return translated.text

text = recognize()
# text = translate("dsda")
print(text)
speak(text)


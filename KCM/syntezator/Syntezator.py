from googletrans import Translator
import speech_recognition as sr
import playsound
from gtts import gTTS

def recognize(filename = None, lang = "pl_PL"):
    r = sr.Recognizer()
    r.energy_threshold = 800
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = r.recognize_google(audio, language=lang)
    return said

def speak(txt, filename):
    playsound.playsound(filename)

def save(txt, filename):
    tts = gTTS(text=txt, lang='pl')
    tts.save(filename)
    return filename

def translate(txt):
    translator = Translator()
    translated = translator.translate(txt)
    save(translated.text, "voiceEn.mp3")
    return translated.text

text_pl = recognize("voicePl.mp3")
save(text_pl, "voicePl.mp3")
text_en = translate(text_pl)
speak(text_en, "voiceEn.mp3")


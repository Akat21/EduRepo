from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyautogui
import webbrowser

def recognize(lang = "pl_PL"):
    r = sr.Recognizer()
    r.energy_threshold = 800
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = r.recognize_google(audio, language=lang)
    return said

def open_browser():
    webbrowser.open("http://www.google.com/")

def search_browser(search):
    webbrowser.open('https://www.google.com/search?q={}'.format('+'.join(search.split())))


def run(text):
    if "podgłośnij" in text:
        if text.split(' ')[-1].isalnum():
            iters = int(int(text.split(' ')[-1])/2)
            for i in range(iters):
                pyautogui.press("volumeup")

    if "przycisz" in text:
        if text.split(' ')[-1].isalnum():
            iters = int(int(text.split(' ')[-1])/3)
            for i in range(iters):
                pyautogui.press("volumedown")

    if "włącz przeglądarkę" in text:
        if "wyszukaj" in text:
            res = text.split(' ')
            idx = res.index('wyszukaj')
            print(' '.join(res[(idx+1):]))
            search_browser(' '.join(res[(idx+1):]))
        else:
            open_browser()

run(recognize().lower())
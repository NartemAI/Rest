

import pyttsx3
import random
from rich.console import Console
import webbrowser
import os
import speech_recognition as sr
def out(text):
    tts.say(text)
    text = 'R: ' + text
    console.print(f'[bold cyan]{text}[/bold cyan]')
    tts.runAndWait()
def po():
    r1 = 'С: ' + i
    print(r1)
def p(text):
    return i.find(text,0,len(i)) > -1
def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            return recognizer.recognize_google(audio, language="ru-RU")
        except sr.exceptions.UnknownValueError :
            return None
        except sr.RequestError as e:
            t = 0
            return None

console = Console()
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty("voice", "ru")
tts.say("Привет, я голосовой помощник Рэст! Готов общаться, помогать и поддерживать.")
console.print("[bold cyan]Привет, я голосовой помощник Rest! \nГотов общаться, помогать и поддерживать.[/bold cyan]")
tts.runAndWait()

while True:
    i = input()
    i = str(i)
    i = i.lower()
    if p('rust'):
        if p('здраст') or p('прив') or p('хай') or p('чао'):
            po()
            p_list = ["Привет!", "Здравствуй", "Чао!", "Хай!"]
            random_index = random.randint(0, len(p_list) - 1)
            r = str(p_list[random_index])
            out(r)
        elif p("дел"):
            po()
            p_list = ["Прекрастно!", "Замечательно!", "Неочень", "Так себе", "Великолебно!"]
            random_index = random.randint(0, len(p_list) - 1)
            r = str(p_list[random_index])
            out(r)
        elif p('гугл') or p('браузер') or p('интернет') or p('google'):
            po()
            r = 'Открываю'
            webbrowser.open('https://www.google.com', new=2)
            out(r)
        elif p("поиск") or p("найди"):
            po()
            console.print(f'[bold cyan]R: Что найти? [/bold cyan]')
            wer = input("C: ")
            r = 'Ищу'
            webbrowser.open_new_tab('https://yandex.ru/search/?lr=10735&text={}'.format(wer))
            out(r)
        elif p("выкл") or p("выруби") or p("off"):
            po()
            r = 'Выключаю'
            os.system('shutdown -s')
            out(r)
        elif p("музыка") or p("музыку") or p("жар") or p("жару"):
            po()
            r = 'Включаю, наслаждайтесь!'
            webbrowser.open_new_tab('https://rur.hitmotop.com/')
            out(r)
        elif p('анекдот') or p("рассмеши"):
            po()
            p_list = ["Из комбинации лени и логики получаются программисты.", "Жил—был программист и было у него два сына — Антон и Неантон", "Программисты на работе общаются двумя фразами: «непонятно» и «вроде работает»."]
            random_index = random.randint(0, len(p_list) - 1)
            r = str(p_list[random_index])
            out(r)
        elif p("стоп") or p('хватит') or p('выключись'):
            po()
            break
        else:
            po()
            out("Прости, я тебя не понимаю!")

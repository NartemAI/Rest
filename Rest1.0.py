import pyttsx3
import random
from rich.console import Console
import webbrowser
import os

console = Console()
kd_list = ["как дела", "как дела?","как делишки","как делишки?","как настроение","как настроение?","как настрой","как настрой?","как у тебя дела?","как у тебя дела"]
p1_list = ["привет", "здравствуй", "чао", "хай", "здравствуй!", "привет!", "приветик", "приветик!", "чао!", "хай!"]
web_list = ["браузер","gogle","google","открой гугл","гугл","открой google","открой браузер"]
webp_list = ["поиск","поиск в браузере","найди","найди в браузере","загугли"]
vkl_list =["выключи","выруби","off","выкл","выруби комп","выруби компьютер","выключи комп","выключи компьютер"]

tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty("voice", "ru")
tts.say("Привет, я голосовой помощник Рэст! Готов общаться, помогать и поддерживать.")
console.print("[bold cyan]Привет, я голосовой помощник Rest! \nГотов общаться, помогать и поддерживать.[/bold cyan]")
tts.runAndWait()

while True:
    i = input("C: ")
    i = i.lower()
    if i in p1_list:
        p_list = ["Привет!", "Здравствуй", "Чао!", "Хай!"]
        random_index = random.randint(0, len(p_list) - 1)
        r = str(p_list[random_index])
        tts.say(r)
        r1 = 'R: ' + r
        console.print(f'[bold cyan]{r1}[/bold cyan]')
        tts.runAndWait()
    elif i in kd_list:
        p_list = ["Прекрастно!", "Замечательно!", "Неочень", "Так себе", "Великолебно!"]
        random_index = random.randint(0, len(p_list) - 1)
        r = str(p_list[random_index])
        tts.say(r)
        r1 = 'R: ' + r
        console.print(f'[bold cyan]{r1}[/bold cyan]')
        tts.runAndWait()
    elif i in web_list:
        r = 'Открываю'
        webbrowser.open('https://www.google.com', new=2)
        tts.say(r)
        r1 = 'R: ' + r
        console.print(f'[bold cyan]{r1}[/bold cyan]')
        tts.runAndWait()
    elif i in webp_list:
        wer = input()
        r = 'Ищу'
        webbrowser.open_new_tab('https://yandex.ru/search/?lr=10735&text={}'.format(wer))
        tts.say(r)
        r1 = 'R: ' + r
        console.print(f'[bold cyan]{r1}[/bold cyan]')
        tts.runAndWait()
    elif i in vkl_list:
        r = 'Выключаю'
        os.system('shutdown -s')
        tts.say(r)
        r1 = 'R: ' + r
        console.print(f'[bold cyan]{r1}[/bold cyan]')
        tts.runAndWait()
    else:
        tts.say("Прости, я тебя не понимаю!")
        r1 = 'R: ' + 'Прости, я тебя не понимаю!'
        console.print(f'[bold cyan]{r1}[/bold cyan]')
        tts.runAndWait()

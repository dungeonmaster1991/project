import random
import wikipedia
import pyttsx3
import main
from main import *
from colorama import Fore, Back, Style
import time

# flag variable to print the dots and it's value increases inside the while loop.
flag = 1

# To print the dots we use while loop. In total, 4 dots will be printed.
while flag < 4:
    print("\rЗагрузка, пожалуйста подождите " + ("." * flag), end='')
    time.sleep(1)
    flag = flag + 1
print('')

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def sluchai():
    A = int(input("введи число интервала:"))
    B = int(input("введи конец интервала:"))
    C = int(input("1 - целое,2 - дробное:"))
    if C==1:
        print(random.randit(A,B))
    elif C==2:
        print(random.uniform(A,B))

def wiki():
    wikipedia.set_lang("ru")
    A = input("о чем найти информацию?")
    print(wikipedia.summary(A))

wikipedia.set_lang("ru")
word = ""
print(Fore.LIGHTRED_EX + 'Добрый вечер Господин!')
say("Добрый веер Господин!")
print(Fore.MAGENTA + 'Меня зовут Деламэин')
say("Меня зовут Дэламэин")
print(Fore.BLUE + 'Чего желаете?')
say("Чего желаете?")


while word!="exit":
    print(Fore.LIGHTCYAN_EX + "1 - случайное число, 2 - wikipedia,3 - погода")
# Рассказать пользователю о возможностях: команды, выход и т.д.
    word = input("Введи команду:")
    if word=="1":
        sluchai()
    elif word=="2":
        wiki()
    elif word=="3":
        weather()


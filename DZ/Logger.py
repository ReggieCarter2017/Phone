from datetime import datetime as dt
from time import time

def UserInputLogger(data):
    with open ("log.txt", "a") as file:
        file.write(f"{dt.now().strftime('%H:%M')} — Имя: {data[0]}\nФамилия: {data[1]}\nТелефон: {data[2]}\nОписание: {data[3]}\n\n")

def UserInputLogger2(data):
    with open ("log2.txt", "a") as file:
        file.write(f"{dt.now().strftime('%H:%M')} — Имя: {data[0]} Фамилия: {data[1]} Телефон: {data[2]} Описание: {data[3]}\n")

def SearchingInLog():
    with open ("log2.txt", "r") as file:
        res = input()
        result = [line for line in file.readlines() if res in line]
        return result
def printLog():
    with open("log.txt", "r") as file:
        [print(line) for line in file.readlines()]

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:58:57 2023

@author: V5
"""

import os


# Запись

# import os

# os.environ["MY_VARIABLE"] = "my value"

# os.environ["MY_VARIABLE"] = 1  # Неверно!
# os.environ["MY_VARIABLE"] = str(1)  # Верно

# Чтение переменных окружения
# Для чтения значения переменной окружения также используется os.environ.
# Просто обратитесь к нужному ключу, как если бы это был обычный словарь:


# Чтение переменных окружения

# value = os.environ["MY_VARIABLE"]
# Если переменная окружения не существует, Python выдаст ошибку. Чтобы избежать этого, можно использовать метод get,
# который возвращает None, если переменная не найдена:


# value = os.environ.get("MY_VARIABLE")


def save_fon_color(fon_color):
    os.environ["MY_FON_COLOR"] = "fon_color"


def reed_fon_color():
    fon_color = os.environ.get("MY_FON_COLOR")
    return fon_color


def save_sistema_alarm(sistema_alarm):
    os.environ["MY_SYSTEMA_ALARM"] = "sistema_alarm"


def reed_sistema_alarm():
    sistema_alarm = os.environ.get("MY_SYSTEMA_ALARM")
    if sistema_alarm == None:
        print("None SYTEM_ALARM !!  DEFAULT = QYZM-W")
        sistema_alarm = "QYZM-W"
    return sistema_alarm




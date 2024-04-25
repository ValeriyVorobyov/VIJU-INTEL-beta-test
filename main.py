# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:54:10 2023

@author: V5"""

import os
import sys
import time
from datetime import datetime, timedelta
from tkinter import *
import tkinter
# import tkinter  as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox

# import winsound
# from playsound import playsound
from playsound import playsound  # Version: 1.2.2

import find_system_alarm
# import global_setting
import guard_sound_one
import string_1
import guard_sound
import bd_setting
import string_ess
# import pickle


# from global_setting import *

from threading import Thread

import guard_slovar
# from tkinter.ttk import *
# from PIL import Image, ImageTk
# импорт модуля для преобразования кортежей через format


# import subprocess

# subprocess.run(["python", "другой_скрипт.py"])




path_live = "......./Documents/EVE/logs/Chatlogs/"

path_os = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')

mypath_dir = path_os + "/EVE/logs/Chatlogs/"

geometry_default = "1150x740+100+100"

gl_num_posl_stroki_live_reed = 0
gl_num_posl_stroki_save = 0
gl_last_line_text = ""

# словарь = { ключ1:значение1, ключ2:значение2, ....}
# списорк(Лист) my_list = [1, 2.6, "Hello", True]

list_system = list()
timers_slovar = {}
timers_slovar_green = {}
ess_timers_slovar = {}
shetchik_pustih_slovarey = list()

bufer_intel = list()

image_sound_on_off = "on"
# global int_sound_chouse = 1



# cловарь систем в которых надо озвучивать тревогу (система : дистанция срабатывания тревоги)
save_guard_slovar_sound = {}  # типа система:дистанция
# global save_guard_slovar_sound

guard_list_system_sound = list() # Список всех систем + гейты в них
save_guard_list_system_sound = set()
# global save_guard_list_system_sound
save_id_btn_click = ""
save_event_guard_list_system_sound = Widget
btn_id_set_guard = Button
# save_atr_btn_add = "blue violet", ('Entry', '10', 'bold'), "grey56"
save_atr_btn_add = "blue", ('Entry', '10', 'bold'), "grey56"
save_atr_btn_del = "SystemButtonText", 'TkDefaultFont', "SystemButtonFace", "grey76"
# save_atr_btn_del_region = "SystemButtonText", 'TkDefaultFont', "grey76"
# distance_guard = 5
# save_event_guard_list_system_sound.widget.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")
# save_event_guard_list_system_sound.widget.config(fg="SystemButtonText", font=('TkDefaultFont'), background="SystemButtonFace")
# save_atr_btn = event.widget['fg'], event.widget['font'], event.widget['bg']

# Сontext menu

# check = StringVar()
# check.set("5")

# ///////////////////////////

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     if getattr(sys, 'frozen', False):
#         base_path = sys._MEIPASS
#     else:
#         base_path = os.getcwd()

#     return os.path.join(base_path, relative_path)

# ///////////////////////

# def resource_path(relative):
#     if hasattr(sys, "_MEIPASS"):
#         return os.path.join(sys._MEIPASS, relative)
#         return os.path.join(relative)

# path = resource_path('image.png')
# path = resource_path(os.path.join('Folder', 'image.png'))  #  Если в папке другой
# img = test_6.image.load(path)

# ********************

# def resource_path(relative):
#   if hasattr(sys, "_MEIPASS"):
#       return os.path.join(sys._MEIPASS, relative)
#       return os.path.join(relative)

# filename = 'freesansbold.ttf'

# myfontfile = resource_path(os.path.join(data_dir, filename)

# ***************************

# Эта вся ху... и 3 варианта попыток сверху для того чтобы скомпилировать звук и другие файлы не питона внутрь запускаемого ехе файла
# и вот наконец :


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()

    return os.path.join(base_path, relative_path)


my_path_mp3_01 = resource_path('alarm_1.mp3')
my_path_mp3_02 = resource_path('alarm_2.mp3')
my_path_mp3_03 = resource_path('alarm_3.mp3')
my_path_mp3_04 = resource_path('alarm_4.mp3')
my_path_mp3_05 = resource_path('alarm_5.mp3')
my_path_mp3_06 = resource_path('alarm_6.mp3')
my_path_mp3_07 = resource_path('alarm_7.mp3')
my_path_mp3_08 = resource_path('alarm_8.mp3')
my_path_mp3_09 = resource_path('alarm_9.mp3')
my_path_mp3_10 = resource_path('alarm_10.mp3')
my_path_alarm_on_png = resource_path('alarm_on.png')
my_path_alarm_off_png = resource_path('alarm_off.png')
my_path_icon = resource_path('icon_3.png')
my_path_vol_off_btn = resource_path('volume_off.png')
my_path_bd_setting = resource_path('bd_setting.db')
my_path_bd_sound_one = resource_path('bd_sound_one.db')
# my_path_test_6 = resource_path('test_6.py')


bd_setting.create_bd_all(my_path_bd_setting, my_path_bd_sound_one)

# now = datetime.now()

# # Абстрактный класс Фигура, содержит абстрактные методы для наследников
# class Figure:
#     def area(self):
#         pass

#     def perimeter(self):
#         pass


# # Класс Прямоугольник, является наследником класса Фигура


# class Rectangle(Figure):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)



# class CustomButton(Button):
#     def __init__(self, master=None, **kwargs):
#        super().__init__(master, **kwargs)
#        self.bind_class("CustomButton", "<Button-1>", self.clicked_BTN)



def full_canvas_1(sistem_xx, sistem_yy):
    sistem_x = sistem_xx
    sistem_y = sistem_yy
    # sistem_x = -100
    # sistem_y = 50



    for elements in find_all_canvas:
        btn_id = canva_1.itemcget(elements, "window")
        btn_alarm = root.nametowidget(btn_id)
        btn_alarm.config(background="SystemButtonFace")






    #
    # aQYZMW = canva_1.create_window(sistem_x + 500, sistem_y + 500, anchor=NW, window=btn_aQYZMW, width=btn_window_width,
    #                                tags=["QYZM-W", "I-7JR4", "BU-IU4"])
    #
    # # kv_1=canva_1.create_rectangle(sistem_x+499, sistem_y+499, sistem_x+566, sistem_y+526)
    #
    # # aI7JR4 = canva_1.create_window(sistem_x + 430, sistem_y + 500, anchor=NW, window=btn_aI7JR4, width=btn_window_width,
    # #                                tags=["I-7JR4"])
    # aI7JR4 = canva_1.create_window(sistem_x + 430, sistem_y + 500, anchor=NW, window=btn_aI7JR4, width=btn_window_width,
    #                                tags=["I-7JR4", "QYZM-W", "CH9L-K", "ME-4IU"])
    # aBUIU4 = canva_1.create_window(sistem_x + 500, sistem_y + 470, anchor=NW, window=btn_aBUIU4, width=btn_window_width,
    #                                tags=["BU-IU4", "QYZM-W", "ME-4IU"])
    # # aBUIU4 = canva_1.create_window(sistem_x + 500, sistem_y + 470, anchor=NW, window=btn_aBUIU4, width=btn_window_width,
    # #                                tags=["BU-IU4", "QYZM-W", "ME-4IU"])
    # aME4IU = canva_1.create_window(sistem_x + 430, sistem_y + 470, anchor=NW, window=btn_aME4IU, width=btn_window_width,
    #                                tags=["ME-4IU", "BU-IU4", "9-B1DS", "I-7JR4", "3KNA-N"])
    # aCH9LK = canva_1.create_window(sistem_x + 360, sistem_y + 500, anchor=NW, window=btn_aCH9LK, width=btn_window_width,
    #                                tags=["CH9L-K", "9-B1DS", "I-7JR4", "Q1U-IU"])
    # a9B1DS = canva_1.create_window(sistem_x + 360, sistem_y + 470, anchor=NW, window=btn_a9B1DS, width=btn_window_width,
    #                                tags=["9-B1DS", "CH9L-K", "ME-4IU", "KJ-QWL"])
    # a3KNAN = canva_1.create_window(sistem_x + 430, sistem_y + 440, anchor=NW, window=btn_a3KNAN, width=btn_window_width,
    #                                tags=["3KNA-N", "ME-4IU"])
    # aQ1UIU = canva_1.create_window(sistem_x + 360, sistem_y + 550, anchor=NW, window=btn_aQ1UIU, width=btn_window_width,
    #                                tags=["Q1U-IU", "CH9L-K", "JSI-LL"])
    #
    # aJSILL = canva_1.create_window(sistem_x + 360, sistem_y + 595, anchor=NW, window=btn_aJSILL, width=btn_window_width,
    #                                tags=["JSI-LL", "Q1U-IU", "M-UC05", "U5-XW7"])
    # aSY0W2 = canva_1.create_window(sistem_x + 290, sistem_y + 630, anchor=NW, window=btn_aSY0W2, width=btn_window_width,
    #                                tags=["SY0W-2", "U5-XW7", "M-UC05"])
    # aMUC05 = canva_1.create_window(sistem_x + 290, sistem_y + 595, anchor=NW, window=btn_aMUC05, width=btn_window_width,
    #                                tags=["M-UC05", "JSI-LL", "SY0W-2"])
    # aV7MID = canva_1.create_window(sistem_x + 220, sistem_y + 630, anchor=NW, window=btn_aV7MID, width=btn_window_width,
    #                                tags=["V7-MID", "SY0W-2"])
    # aU5XW7 = canva_1.create_window(sistem_x + 360, sistem_y + 630, anchor=NW, window=btn_aU5XW7, width=btn_window_width,
    #                                tags=["U5-XW7", "SY0W-2", "JSI-LL", "MZPH-W"])
    # aMZPHW = canva_1.create_window(sistem_x + 360, sistem_y + 670, anchor=NW, window=btn_aMZPHW, width=btn_window_width,
    #                                tags=["MZPH-W"])
    #
    # aKJQWL = canva_1.create_window(sistem_x + 360, sistem_y + 390, anchor=NW, window=btn_aKJQWL, width=btn_window_width,
    #                                tags=["KJ-QWL", "9-B1DS", "SVB-RE", "KMQ4-V"])
    # aKMQ4V = canva_1.create_window(sistem_x + 428, sistem_y + 390, anchor=NW, window=btn_aKMQ4V, width=btn_window_width,
    #                                tags=["KMQ4-V", "KJ-QWL", "5-P1Y2"])
    # aSVBRE = canva_1.create_window(sistem_x + 377, sistem_y + 355, anchor=NW, window=btn_aSVBRE, width=btn_window_width,
    #                                tags=["SVB-RE", "KJ-QWL"])
    #
    # a5P1Y2 = canva_1.create_window(sistem_x + 497, sistem_y + 390, anchor=NW, window=btn_a5P1Y2, width=btn_window_width,
    #                                tags=["5-P1Y2", "KMQ4-V", "J52-BH"])
    # aJ52BH = canva_1.create_window(sistem_x + 565, sistem_y + 390, anchor=NW, window=btn_aJ52BH, width=btn_window_width,
    #                                tags=["J52-BH", "5-P1Y2", "C-LBQS"])
    # aCLBQS = canva_1.create_window(sistem_x + 633, sistem_y + 390, anchor=NW, window=btn_aCLBQS, width=btn_window_width,
    #                                tags=["C-LBQS", "J52-BH", "BWI1-9"])
    # aBWI19 = canva_1.create_window(sistem_x + 700, sistem_y + 390, anchor=NW, window=btn_aBWI19, width=btn_window_width,
    #                                tags=["BWI1-9", "C-LBQS", "KL3O-J"])
    # aKL30J = canva_1.create_window(sistem_x + 769, sistem_y + 390, anchor=NW, window=btn_aKL30J, width=btn_window_width,
    #                                tags=["KL3O-J", "R4O-I6", "BWI1-9"])
    # aR40I6 = canva_1.create_window(sistem_x + 768, sistem_y + 355, anchor=NW, window=btn_aR40I6, width=btn_window_width,
    #                                tags=["R4O-I6", "KL3O-J", "Q-NJZ4", "3-TD6L"])
    #
    # aQNJZ4 = canva_1.create_window(sistem_x + 835, sistem_y + 355, anchor=NW, window=btn_aQNJZ4, width=btn_window_width,
    #                                tags=["Q-NJZ4", "R4O-I6", "NLPB-0", "3-TD6L"])
    # aNLPB0 = canva_1.create_window(sistem_x + 835, sistem_y + 310, anchor=NW, window=btn_aNLPB0, width=btn_window_width,
    #                                tags=["NLPB-0", "Q-NJZ4", "3-TD6L"])
    # a3TD6L = canva_1.create_window(sistem_x + 768, sistem_y + 310, anchor=NW, window=btn_a3TD6L, width=btn_window_width,
    #                                tags=["3-TD6L", "NLPB-0", "R4O-I6", "Q-NJZ4", "CX-1XF"])
    # aCX1XF = canva_1.create_window(sistem_x + 680, sistem_y + 295, anchor=NW, window=btn_aCX1XF, width=btn_window_width,
    #                                tags=["CX-1XF", "3-TD6L", "X4UV-Z"])
    # aX4UVZ = canva_1.create_window(sistem_x + 530, sistem_y + 295, anchor=NW, window=btn_aX4UVZ, width=btn_window_width,
    #                                tags=["X4UV-Z", "CX-1XF", "BKG-Q2", "JRZ-B9"])
    # aJRZB9 = canva_1.create_window(sistem_x + 530, sistem_y + 260, anchor=NW, window=btn_aJRZB9, width=btn_window_width,
    #                                tags=["JRZ-B9", "X4UV-Z", "V8W-QS", "S-B7IT"])
    # aV8WQS = canva_1.create_window(sistem_x + 605, sistem_y + 260, anchor=NW, window=btn_aV8WQS, width=btn_window_width,
    #                                tags=["V8W-QS", "JRZ-B9", "XW-2XP", "CS-ZGD", "OJ-A8M"])
    # aXW2XP = canva_1.create_window(sistem_x + 575, sistem_y + 210, anchor=NW, window=btn_aXW2XP, width=btn_window_width,
    #                                tags=["XW-2XP", "V8W-QS", "C-HCGU"])
    #
    # aCSZGD = canva_1.create_window(sistem_x + 680, sistem_y + 210, anchor=NW, window=btn_aCSZGD, width=btn_window_width,
    #                                tags=["CS-ZGD", "V8W-QS", "A-G1FM", "3-N3OO"])
    # a3N3OO = canva_1.create_window(sistem_x + 790, sistem_y + 210, anchor=NW, window=btn_a3N3OO, width=btn_window_width,
    #                                tags=["3-N3OO", "CS-ZGD", "4-BE0M", "ZIU-EP"])
    # aAG1FM = canva_1.create_window(sistem_x + 700, sistem_y + 133, anchor=NW, window=btn_aAG1FM, width=btn_window_width,
    #                                tags=["A-G1FM", "CS-ZGD", "ZIU-EP", "I-7RIS", "P7Z-R3", "4-BE0M"])
    #
    # aZIUEP = canva_1.create_window(sistem_x + 742, sistem_y + 172, anchor=NW, window=btn_aZIUEP, width=btn_window_width,
    #                                tags=["ZIU-EP", "3-N3OO", "A-G1FM", "2-3Q2G"])
    # aP7ZR3 = canva_1.create_window(sistem_x + 735, sistem_y + 95, anchor=NW, window=btn_aP7ZR3, width=btn_window_width,
    #                                tags=["P7Z-R3", "4-BE0M", "A-G1FM"])
    # a4BE0M = canva_1.create_window(sistem_x + 810, sistem_y + 95, anchor=NW, window=btn_a4BE0M, width=btn_window_width,
    #                                tags=["4-BE0M", "P7Z-R3", "A-G1FM", "3-N3OO"])
    # aI7RIS = canva_1.create_window(sistem_x + 655, sistem_y + 95, anchor=NW, window=btn_aI7RIS, width=btn_window_width,
    #                                tags=["I-7RIS", "A-G1FM"])
    # a23Q2G = canva_1.create_window(sistem_x + 836, sistem_y + 140, anchor=NW, window=btn_a23Q2G, width=btn_window_width,
    #                                tags=["2-3Q2G", "ZIU-EP"])
    #
    # a9IPCE = canva_1.create_window(sistem_x + 836, sistem_y - 15, anchor=NW, window=btn_a9IPCE, width=btn_window_width,
    #                                tags=["9IPC-E", "UQ9-3C"])
    #
    # aKMCWI = canva_1.create_window(sistem_x + 825, sistem_y + 30, anchor=NW, window=btn_aKMCWI, width=btn_window_width,
    #                                tags=["KMC-WI", "VL3I-M"])
    # aVL3IM = canva_1.create_window(sistem_x + 750, sistem_y + 30, anchor=NW, window=btn_aVL3IM, width=btn_window_width,
    #                                tags=["VL3I-M", "KMC-WI", "UQ9-3C"])
    # aUQ93C = canva_1.create_window(sistem_x + 750, sistem_y - 15, anchor=NW, window=btn_aUQ93C, width=btn_window_width,
    #                                tags=["UQ9-3C", "VL3I-M", "9IPC-E", "DCI7-7"])
    #
    # aDCI77 = canva_1.create_window(sistem_x + 670, sistem_y - 15, anchor=NW, window=btn_aDCI77, width=btn_window_width,
    #                                tags=["DCI7-7", "UQ9-3C", "J7YR-1"])
    # aJ7YR1 = canva_1.create_window(sistem_x + 600, sistem_y - 15, anchor=NW, window=btn_aJ7YR1, width=btn_window_width,
    #                                tags=["J7YR-1", "DCI7-7", "PKG4-7", "AH-B84"])
    # aPKG47 = canva_1.create_window(sistem_x + 600, sistem_y + 15, anchor=NW, window=btn_aPKG47, width=btn_window_width,
    #                                tags=["PKG4-7", "EWN-2U", "J7YR-1"])
    # aEWN2U = canva_1.create_window(sistem_x + 600, sistem_y + 45, anchor=NW, window=btn_aEWN2U, width=btn_window_width,
    #                                tags=["EWN-2U", "PKG4-7", "4-48K1"])
    #
    # aAHB84 = canva_1.create_window(sistem_x + 505, sistem_y + 15, anchor=NW, window=btn_aAHB84, width=btn_window_width,
    #                                tags=["AH-B84", "DCI7-7", "HB7R-F", "JTAU-5"])
    #
    # aHB7RF = canva_1.create_window(sistem_x + 505, sistem_y - 25, anchor=NW, window=btn_aHB7RF, width=btn_window_width,
    #                                tags=["HB7R-F", "AH-B84", "O-JPKH"])
    # aOJPKH = canva_1.create_window(sistem_x + 435, sistem_y - 25, anchor=NW, window=btn_aOJPKH, width=btn_window_width,
    #                                tags=["O-JPKH", "HB7R-F", "B-GC1T"])
    # aBGC1T = canva_1.create_window(sistem_x + 365, sistem_y - 25, anchor=NW, window=btn_aBGC1T, width=btn_window_width,
    #                                tags=["B-GC1T", "O-JPKH"])
    # aJTAU5 = canva_1.create_window(sistem_x + 435, sistem_y + 15, anchor=NW, window=btn_aJTAU5, width=btn_window_width,
    #                                tags=["JTAU-5", "AH-B84", "F-9F6Q"])
    # aF9F6Q = canva_1.create_window(sistem_x + 365, sistem_y + 15, anchor=NW, window=btn_aF9F6Q, width=btn_window_width,
    #                                tags=["F-9F6Q", "JTAU-5"])
    #
    # # aXW2XP = canva_1.create_window(sistem_x+742, sistem_y+260, anchor=NW, window=btn_aXW2XP, width=btn_window_width, tags=["XW-2XP"])
    #
    # aOJA8M = canva_1.create_window(sistem_x + 742, sistem_y + 260, anchor=NW, window=btn_aOJA8M, width=btn_window_width,
    #                                tags=["OJ-A8M", "V8W-QS", "H1-ESN"])
    # aH1ESN = canva_1.create_window(sistem_x + 836, sistem_y + 260, anchor=NW, window=btn_aH1ESN, width=btn_window_width,
    #                                tags=["H1-ESN", "OJ-A8M"])
    #
    # aCHCGU = canva_1.create_window(sistem_x + 560, sistem_y + 169, anchor=NW, window=btn_aCHCGU, width=btn_window_width,
    #                                tags=["C-HCGU", "XW-2XP", "NTV0-1", "Q-FEEJ"])
    # aNTV01 = canva_1.create_window(sistem_x + 560, sistem_y + 139, anchor=NW, window=btn_aNTV01, width=btn_window_width,
    #                                tags=["NTV0-1", "C-HCGU", "4-48K1"])
    # a448K1 = canva_1.create_window(sistem_x + 560, sistem_y + 108, anchor=NW, window=btn_a448K1, width=btn_window_width,
    #                                tags=["4-48K1", "NTV0-1", "EWN-2U"])
    # aQFEEJ = canva_1.create_window(sistem_x + 475, sistem_y + 169, anchor=NW, window=btn_aQFEEJ, width=btn_window_width,
    #                                tags=["Q-FEEJ", "C-HCGU", "0P9Z-I"])
    # a0P9ZI = canva_1.create_window(sistem_x + 475, sistem_y + 139, anchor=NW, window=btn_a0P9ZI, width=btn_window_width,
    #                                tags=["0P9Z-I", "Q-FEEJ", "Z-K495"])
    #
    # aSB7IT = canva_1.create_window(sistem_x + 455, sistem_y + 260, anchor=NW, window=btn_aSB7IT, width=btn_window_width,
    #                                tags=["S-B7IT", "BKG-Q2", "JRZ-B9"])
    # aBKGQ2 = canva_1.create_window(sistem_x + 455, sistem_y + 295, anchor=NW, window=btn_aBKGQ2, width=btn_window_width,
    #                                tags=["BKG-Q2", "S-B7IT", "Z-K495", "X4UV-Z", "8-4GQM", "LXWN-W"])
    # aZK495 = canva_1.create_window(sistem_x + 365, sistem_y + 139, anchor=NW, window=btn_aZK495, width=btn_window_width,
    #                                tags=["Z-K495", "BKG-Q2", "XM-4L0", "0P9Z-I"])
    #
    # aYG82V = canva_1.create_window(sistem_x + 365, sistem_y + 100, anchor=NW, window=btn_aYG82V, width=btn_window_width,
    #                                tags=["YG-82V", "UB-UQZ"])
    #
    # aUBUQZ = canva_1.create_window(sistem_x + 285, sistem_y + 100, anchor=NW, window=btn_aUBUQZ, width=btn_window_width,
    #                                tags=["UB-UQZ", "YG-82V", "XM-4L0", "B8O-KJ"])
    # aXM4L0 = canva_1.create_window(sistem_x + 285, sistem_y + 139, anchor=NW, window=btn_aXM4L0, width=btn_window_width,
    #                                tags=["XM-4L0", "Z-K495", "UB-UQZ", "B8O-KJ", "QCWA-Z"])
    # aQCWAZ = canva_1.create_window(sistem_x + 285, sistem_y + 179, anchor=NW, window=btn_aQCWAZ, width=btn_window_width,
    #                                tags=["QCWA-Z", "KV-8SM", "XM-4L0", "5LJ-MD", "52G-NZ"])
    # aKV8SM = canva_1.create_window(sistem_x + 285, sistem_y + 220, anchor=NW, window=btn_aKV8SM, width=btn_window_width,
    #                                tags=["KV-8SM", "QCWA-Z", "52G-NZ"])
    # a4DTQK = canva_1.create_window(sistem_x + 205, sistem_y + 70, anchor=NW, window=btn_a4DTQK, width=btn_window_width,
    #                                tags=["4DTQ-K", "B8O-KJ", "EQI2-2", "J9-5MQ"])
    # aB8OKJ = canva_1.create_window(sistem_x + 205, sistem_y + 139, anchor=NW, window=btn_aB8OKJ, width=btn_window_width,
    #                                tags=["B8O-KJ", "XM-4L0", "UB-UQZ", "4DTQ-K", "5LJ-MD"])
    # a5LJMD = canva_1.create_window(sistem_x + 205, sistem_y + 179, anchor=NW, window=btn_a5LJMD, width=btn_window_width,
    #                                tags=["5LJ-MD", "B8O-KJ", "QCWA-Z", "52G-NZ"])
    # a52GNZ = canva_1.create_window(sistem_x + 205, sistem_y + 220, anchor=NW, window=btn_a52GNZ, width=btn_window_width,
    #                                tags=["52G-NZ", "KV-8SM", "QCWA-Z", "5LJ-MD", "6-O5GY"])
    #
    # aEQI22 = canva_1.create_window(sistem_x + 270, sistem_y + 40, anchor=NW, window=btn_aEQI22, width=btn_window_width,
    #                                tags=["EQI2-2", "4DTQ-K", "D4R-H7"])
    # aD4RH7 = canva_1.create_window(sistem_x + 270, sistem_y + 10, anchor=NW, window=btn_aD4RH7, width=btn_window_width,
    #                                tags=["D4R-H7", "EQI2-2", "J9-5MQ"])
    # aJ95MQ = canva_1.create_window(sistem_x + 205, sistem_y + -20, anchor=NW, window=btn_aJ95MQ, width=btn_window_width,
    #                                tags=["J9-5MQ", "D4R-H7", "313I-B", "Q-4DEC"])
    # a313IB = canva_1.create_window(sistem_x + 128, sistem_y + -45, anchor=NW, window=btn_a313IB, width=btn_window_width,
    #                                tags=["313I-B", "J9-5MQ"])
    # aQ4DEC = canva_1.create_window(sistem_x + 128, sistem_y + 10, anchor=NW, window=btn_aQ4DEC, width=btn_window_width,
    #                                tags=["Q-4DEC", "J9-5MQ"])
    # a6O5GY = canva_1.create_window(sistem_x + 115, sistem_y + 220, anchor=NW, window=btn_a6O5GY, width=btn_window_width,
    #                                tags=["6-O5GY", "52G-NZ"])
    #
    # aZXAV6 = canva_1.create_window(sistem_x + 360, sistem_y + 256, anchor=NW, window=btn_aZXAV6, width=btn_window_width,
    #                                tags=["ZXA-V6", "T-Q2DD"])
    #
    # aTQ2DD = canva_1.create_window(sistem_x + 261, sistem_y + 265, anchor=NW, window=btn_aTQ2DD, width=btn_window_width,
    #                                tags=["T-Q2DD", "ZXA-V6", ])
    # aLRWDB = canva_1.create_window(sistem_x + 261, sistem_y + 325, anchor=NW, window=btn_aLRWDB, width=btn_window_width,
    #                                tags=["LRWD-B", "QXQ-BA", "8-4GQM"])
    # aQXQBA = canva_1.create_window(sistem_x + 210, sistem_y + 295, anchor=NW, window=btn_aQXQBA, width=btn_window_width,
    #                                tags=["QXQ-BA", "T-Q2DD", "LRWD-B", "X7R-JW", "M-HU4V"])
    # aX7RJW = canva_1.create_window(sistem_x + 162, sistem_y + 265, anchor=NW, window=btn_aX7RJW, width=btn_window_width,
    #                                tags=["X7R-JW", "QXQ-BA", "M-HU4V"])
    # aMHU4V = canva_1.create_window(sistem_x + 162, sistem_y + 325, anchor=NW, window=btn_aMHU4V, width=btn_window_width,
    #                                tags=["M-HU4V", "X7R-JW", "QXQ-BA", "C-4ZOS"])
    #
    # a84GQM = canva_1.create_window(sistem_x + 315, sistem_y + 295, anchor=NW, window=btn_a84GQM, width=btn_window_width,
    #                                tags=["8-4GQM", "BKG-Q2", "LRWD-B", "T-Q2DD"])
    # aLXWNW = canva_1.create_window(sistem_x + 260, sistem_y + 410, anchor=NW, window=btn_aLXWNW, width=btn_window_width,
    #                                tags=["LXWN-W", "BKG-Q2", "RO90-H", "C-LP3N"])
    #
    # aC4ZOS = canva_1.create_window(sistem_x + 91, sistem_y + 379, anchor=NW, window=btn_aC4ZOS, width=btn_window_width,
    #                                tags=["C-4ZOS", "M-HU4V"])
    #
    # aRO90H = canva_1.create_window(sistem_x + 260, sistem_y + 443, anchor=NW, window=btn_aRO90H, width=btn_window_width,
    #                                tags=["RO90-H", "LXWN-W", "MA-VDX", "WO-AIJ"])
    # aMAVDX = canva_1.create_window(sistem_x + 260, sistem_y + 475, anchor=NW, window=btn_aMAVDX, width=btn_window_width,
    #                                tags=["MA-VDX", "92D-OI", "RO90-H", "1G-MJE"])
    # a92DOI = canva_1.create_window(sistem_x + 260, sistem_y + 524, anchor=NW, window=btn_a92DOI, width=btn_window_width,
    #                                tags=["92D-OI", "MA-VDX"])
    # aWOAIJ = canva_1.create_window(sistem_x + 188, sistem_y + 443, anchor=NW, window=btn_aWOAIJ, width=btn_window_width,
    #                                tags=["WO-AIJ", "1G-MJE", "C-LP3N", "RO90-H"])
    # a1GMJE = canva_1.create_window(sistem_x + 188, sistem_y + 475, anchor=NW, window=btn_a1GMJE, width=btn_window_width,
    #                                tags=["1G-MJE", "MA-VDX", "WO-AIJ"])
    # aCLP3N = canva_1.create_window(sistem_x + 188, sistem_y + 410, anchor=NW, window=btn_aCLP3N, width=btn_window_width,
    #                                tags=["C-LP3N", "WO-AIJ", "9F-7PZ", "LXWN-W", ])
    # a9F7PZ = canva_1.create_window(sistem_x + 188, sistem_y + 379, anchor=NW, window=btn_a9F7PZ, width=btn_window_width,
    #                                tags=["9F-7PZ", "C-LP3N"])
    #
    # aTEST = canva_1.create_window(sistem_x + 731, sistem_y + 624, anchor=NW, window=btn_aTEST, width=btn_window_width,
    #                               tags=["TEST"])
    # aTuKTuK = canva_1.create_window(sistem_x + 800, sistem_y + 624, anchor=NW, window=btn_aTuKTuK, width=btn_window_width,
    #                                 tags=["TuK-TuK"])
    # # =============================================================================
    # #
    # # =============================================================================
    #
    # # canva_1.create_line(10, 10, 20, 20)



def full_canvas_2(sistem_xx, sistem_yy):
    sistem_x = sistem_xx
    sistem_y = sistem_yy

    # sistem_x = -100
    # sistem_y = 50

    # ГЕЙТЫ ЛИНИИ

    # canva_1.create_line(393, 66, 499, 68, fill="black", stipple='warning', splinesteps=1, width=2)

    color_gate_line = "burlywood4"

    my_wwidth_01 = 1.4
    #
    # kl30j_r40i6 = canva_1.create_line(sistem_x + 800, sistem_y + 365, sistem_x + 800, sistem_y + 390, fill="burlywood4",
    #                                   splinesteps=10, width=my_wwidth_01)
    # bwi9_kl30j = canva_1.create_line(sistem_x + 765, sistem_y + 402, sistem_x + 800, sistem_y + 402, fill="burlywood4",
    #                                  splinesteps=10, width=my_wwidth_01)
    #
    # bkgq2_cx1xf = canva_1.create_line(sistem_x + 520, sistem_y + 307, sistem_x + 699, sistem_y + 307, fill="burlywood4", splinesteps=10,
    #                                   width=my_wwidth_01)
    #
    # jrzb9_x4uvz = canva_1.create_line(sistem_x + 560, sistem_y + 285, sistem_x + 560, sistem_y + 294, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    #
    # sb7it_v8wqs = canva_1.create_line(sistem_x + 520, sistem_y + 272, sistem_x + 605, sistem_y + 272, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    # sb7it_bkgq2 = canva_1.create_line(sistem_x + 486, sistem_y + 295, sistem_x + 486, sistem_y + 285, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    #
    # zk_bkg = canva_1.create_line(sistem_x + 396, sistem_y + 160, sistem_x + 455, sistem_y + 306, fill="burlywood4",
    #                              splinesteps=5, width=my_wwidth_01)
    # a84qm_bkg = canva_1.create_line(sistem_x + 380, sistem_y + 307, sistem_x + 455, sistem_y + 307, fill="burlywood4",
    #                                 splinesteps=5, width=my_wwidth_01)
    #
    # lxwnw_bkgq2 = canva_1.create_line(sistem_x + 290, sistem_y + 384, sistem_x + 455, sistem_y + 309, fill="burlywood4",
    #                                   splinesteps=5, width=my_wwidth_01)
    # lxwnw_92doi = canva_1.create_line(sistem_x + 290, sistem_y + 384, sistem_x + 290, sistem_y + 527, fill="burlywood4",
    #                                   splinesteps=5, width=my_wwidth_01)
    #
    # mzphw_svbre = canva_1.create_line(sistem_x + 390, sistem_y + 670, sistem_x + 390, sistem_y + 380, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    #
    # v7mid_u5xw7 = canva_1.create_line(sistem_x + 285, sistem_y + 642, sistem_x + 365, sistem_y + 642, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    # muc05_jsill = canva_1.create_line(sistem_x + 356, sistem_y + 607, sistem_x + 365, sistem_y + 607, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    # muc05_syow2 = canva_1.create_line(sistem_x + 322, sistem_y + 620, sistem_x + 322, sistem_y + 629, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    #
    # ch9lk_qyzmw = canva_1.create_line(sistem_x + 425, sistem_y + 512, sistem_x + 500, sistem_y + 512, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    # buiu4_qyzmw = canva_1.create_line(sistem_x + 530, sistem_y + 490, sistem_x + 530, sistem_y + 512, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    # a9b1ds_buiu4 = canva_1.create_line(sistem_x + 425, sistem_y + 482, sistem_x + 500, sistem_y + 482, fill="burlywood4", splinesteps=0,
    #                                    width=my_wwidth_01)
    # i7jr4_3knan = canva_1.create_line(sistem_x + 461, sistem_y + 456, sistem_x + 461, sistem_y + 500, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    #
    # kjqwl_clbqs = canva_1.create_line(sistem_x + 425, sistem_y + 403, sistem_x + 700, sistem_y + 403, fill="burlywood4", splinesteps=0,
    #                                   width=my_wwidth_01)
    #
    # a3td6l_r40 = canva_1.create_line(sistem_x + 800, sistem_y + 330, sistem_x + 800, sistem_y + 356, fill="burlywood4",
    #                                  splinesteps=0, width=my_wwidth_01)
    # a3td6l_qn = canva_1.create_line(sistem_x + 800, sistem_y + 330, sistem_x + 860, sistem_y + 356, fill="burlywood4",
    #                                 splinesteps=0, width=my_wwidth_01)
    # nlpb_qn = canva_1.create_line(sistem_x + 867, sistem_y + 330, sistem_x + 867, sistem_y + 356, fill="burlywood4",
    #                               splinesteps=0, width=my_wwidth_01)
    #
    # v8wqs_oja8m = canva_1.create_line(sistem_x + 667, sistem_y + 272, sistem_x + 743, sistem_y + 272, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # oja8m_h1esn = canva_1.create_line(sistem_x + 800, sistem_y + 272, sistem_x + 841, sistem_y + 272, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # # canva_1.create_line(563, 120, 670, 120, fill="burlywood4", splinesteps=0, width=my_wwidth_01)
    #
    # cx1xf_3t = canva_1.create_line(sistem_x + 744, sistem_y + 307, sistem_x + 766, sistem_y + 322, fill="burlywood4",
    #                                splinesteps=0, width=my_wwidth_01)
    #
    # v8wqs_xw2xp = canva_1.create_line(sistem_x + 610, sistem_y + 236, sistem_x + 626, sistem_y + 260, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # v8wqs_cszgd = canva_1.create_line(sistem_x + 705, sistem_y + 236, sistem_x + 645, sistem_y + 260, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # cszgd_3n3oo = canva_1.create_line(sistem_x + 745, sistem_y + 221, sistem_x + 790, sistem_y + 221, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    #
    # cszgd_ag1fm = canva_1.create_line(sistem_x + 720, sistem_y + 153, sistem_x + 720, sistem_y + 208, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # ag1fm_i7ris = canva_1.create_line(sistem_x + 693, sistem_y + 118, sistem_x + 720, sistem_y + 137, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # ag1fm_ziueo = canva_1.create_line(sistem_x + 739, sistem_y + 155, sistem_x + 762, sistem_y + 170, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # ag1fm_p7zr3 = canva_1.create_line(sistem_x + 740, sistem_y + 137, sistem_x + 755, sistem_y + 118, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # ag1fm_4be0m = canva_1.create_line(sistem_x + 764, sistem_y + 143, sistem_x + 816, sistem_y + 121, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    #
    # ziueo_23q2g = canva_1.create_line(sistem_x + 785, sistem_y + 170, sistem_x + 837, sistem_y + 152, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    #
    # p7zr3_4be0m = canva_1.create_line(sistem_x + 800, sistem_y + 106, sistem_x + 812, sistem_y + 106, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # a4be0m_3n3oo = canva_1.create_line(sistem_x + 824, sistem_y + 120, sistem_x + 824, sistem_y + 212, fill="burlywood4",
    #                                    splinesteps=0, width=my_wwidth_01)
    # a3n3oo_ziuep = canva_1.create_line(sistem_x + 785, sistem_y + 197, sistem_x + 800, sistem_y + 212, fill="burlywood4",
    #                                    splinesteps=0, width=my_wwidth_01)
    # # canva_1.create_arc(366, 182, 600, 305,   start=160, extent=170,  style=ARC, outline='darkblue', fill='orange',  width=2)
    #
    # xw2xp_448k1 = canva_1.create_line(sistem_x + 595, sistem_y + 123, sistem_x + 595, sistem_y + 215, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # chcgu_qfeej = canva_1.create_line(sistem_x + 540, sistem_y + 180, sistem_x + 562, sistem_y + 180, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # chcgu_op9zi = canva_1.create_line(sistem_x + 507, sistem_y + 164, sistem_x + 507, sistem_y + 175, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # op9zi_zk495 = canva_1.create_line(sistem_x + 430, sistem_y + 151, sistem_x + 472, sistem_y + 151, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # ewn2u_448k1 = canva_1.create_line(sistem_x + 630, sistem_y + 70, sistem_x + 595, sistem_y + 115, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # ewn2u_j7yr1 = canva_1.create_line(sistem_x + 630, sistem_y + -4, sistem_x + 630, sistem_y + 60, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # j7yr1_9ipce = canva_1.create_line(sistem_x + 661, sistem_y + -2, sistem_x + 841, sistem_y + -2, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # ahb84_j7yr1 = canva_1.create_line(sistem_x + 570, sistem_y + 26, sistem_x + 604, sistem_y + -4, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # ahb84_hb7rf = canva_1.create_line(sistem_x + 537, sistem_y + 0, sistem_x + 537, sistem_y + 15, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # f9f6q_ahb84 = canva_1.create_line(sistem_x + 418, sistem_y + 27, sistem_x + 509, sistem_y + 27, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # bgc1t_hb7rf = canva_1.create_line(sistem_x + 420, sistem_y + -12, sistem_x + 507, sistem_y + -12, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    #
    # uq93c_vl3im = canva_1.create_line(sistem_x + 782, sistem_y + 10, sistem_x + 782, sistem_y + 33, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # vl3im_kmcwi = canva_1.create_line(sistem_x + 815, sistem_y + 43, sistem_x + 825, sistem_y + 43, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    #
    # xm4l0_zk495 = canva_1.create_line(sistem_x + 350, sistem_y + 152, sistem_x + 365, sistem_y + 152, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    #
    # ubuqz_kv8sm = canva_1.create_line(sistem_x + 317, sistem_y + 116, sistem_x + 317, sistem_y + 238, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # a52gnz_kv8sm = canva_1.create_line(sistem_x + 265, sistem_y + 232, sistem_x + 294, sistem_y + 232, fill="burlywood4",
    #                                    splinesteps=0, width=my_wwidth_01)
    # a52gnz_qcwaz = canva_1.create_line(sistem_x + 252, sistem_y + 219, sistem_x + 300, sistem_y + 205, fill="burlywood4",
    #                                    splinesteps=0, width=my_wwidth_01)
    # a5ljmd_qcwaz = canva_1.create_line(sistem_x + 252, sistem_y + 191, sistem_x + 290, sistem_y + 191, fill="burlywood4",
    #                                    splinesteps=0, width=my_wwidth_01)
    # j95mq_52gnz = canva_1.create_line(sistem_x + 237, sistem_y + 5, sistem_x + 237, sistem_y + 238, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # a6o5gy_52gnz = canva_1.create_line(sistem_x + 180, sistem_y + 231, sistem_x + 205, sistem_y + 231, fill="burlywood4",
    #                                    splinesteps=0, width=my_wwidth_01)
    #
    # ubuqz_yg82v = canva_1.create_line(sistem_x + 343, sistem_y + 113, sistem_x + 368, sistem_y + 113, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    #
    # b80kj_ubuqz = canva_1.create_line(sistem_x + 252, sistem_y + 137, sistem_x + 290, sistem_y + 112, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # b80kj_xm4l0 = canva_1.create_line(sistem_x + 264, sistem_y + 150, sistem_x + 290, sistem_y + 150, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    #
    # ####################
    # tq2dd_zxav6 = canva_1.create_line(sistem_x + 325, sistem_y + 275, sistem_x + 365, sistem_y + 267, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # tq2dd_84gqm = canva_1.create_line(sistem_x + 300, sistem_y + 291, sistem_x + 315, sistem_y + 305, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # qxqba_tq2dd = canva_1.create_line(sistem_x + 275, sistem_y + 305, sistem_x + 290, sistem_y + 291, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # qxqba_lrwdb = canva_1.create_line(sistem_x + 275, sistem_y + 309, sistem_x + 290, sistem_y + 324, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # lrwdb_84gqm = canva_1.create_line(sistem_x + 300, sistem_y + 324, sistem_x + 315, sistem_y + 310, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    #
    # a4dtqk_eqi22 = canva_1.create_line(sistem_x + 271, sistem_y + 82, sistem_x + 300, sistem_y + 66, fill="burlywood4",
    #                                    splinesteps=0, width=my_wwidth_01)
    # eqi22_d4rh7 = canva_1.create_line(sistem_x + 300, sistem_y + 44, sistem_x + 300, sistem_y + 28, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # d4rh7_j95mq = canva_1.create_line(sistem_x + 300, sistem_y + 13, sistem_x + 270, sistem_y + -9, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # j95mq_313ib = canva_1.create_line(sistem_x + 207, sistem_y + -9, sistem_x + 186, sistem_y + -43, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # j95mq_q4idec = canva_1.create_line(sistem_x + 207, sistem_y + -6, sistem_x + 186, sistem_y + 33, fill="burlywood4",
    #                                    splinesteps=0, width=my_wwidth_01)
    #
    # qxqba_x7rjw = canva_1.create_line(sistem_x + 240, sistem_y + 292, sistem_x + 225, sistem_y + 277, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # qxqba_mhu4v = canva_1.create_line(sistem_x + 240, sistem_y + 321, sistem_x + 225, sistem_y + 338, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # x7rjw_mhu4v = canva_1.create_line(sistem_x + 192, sistem_y + 290, sistem_x + 192, sistem_y + 325, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    # mhu4v_c4zos = canva_1.create_line(sistem_x + 192, sistem_y + 350, sistem_x + 155, sistem_y + 391, fill="burlywood4",
    #                                   splinesteps=0, width=my_wwidth_01)
    #
    # a1gmje_9f7pz = canva_1.create_line(sistem_x + 221, sistem_y + 481, sistem_x + 221, sistem_y + 400, fill="burlywood4",
    #                                    splinesteps=0, width=my_wwidth_01)
    # g_1gmje_9f7pz = canva_1.create_line(sistem_x + 221, sistem_y + 481, sistem_x + 221, sistem_y + 400, fill="burlywood4",
    #                                     splinesteps=0, width=my_wwidth_01)
    # g_1gmje_9f7pz = canva_1.create_line(sistem_x + 245, sistem_y + 486, sistem_x + 269, sistem_y + 486, fill="burlywood4",
    #                                     splinesteps=0, width=my_wwidth_01)
    # g_woaij_ro90h = canva_1.create_line(sistem_x + 245, sistem_y + 455, sistem_x + 269, sistem_y + 455, fill="burlywood4",
    #                                     splinesteps=0, width=my_wwidth_01)
    # g_clp3n_lxwnw = canva_1.create_line(sistem_x + 245, sistem_y + 422, sistem_x + 269, sistem_y + 422, fill="burlywood4",
    #                                     splinesteps=0, width=my_wwidth_01)
    #
    # # canva_1.create_oval(363, 182, 600, 305,               fill='lightgrey',              outline='white')
    #
    # # canva_1.create_rectangle(363, 182, 598, 305 )
    #
    # # БРИДЖИ
    # color_bridge_line = "green"
    # color_bridge_line_active = "red"
    # # bu -- kl
    # canva_1.create_line(sistem_x + 566, sistem_y + 484, sistem_x + 800, sistem_y + 484, activefill="red", fill="green", dash=5)
    # canva_1.create_line(sistem_x + 800, sistem_y + 415, sistem_x + 800, sistem_y + 484, activefill="red", fill="green", dash=5)
    #
    # # me -- 5p
    # canva_1.create_line(sistem_x + 529, sistem_y + 415, sistem_x + 529, sistem_y + 440, activefill="red", fill="green", dash=1)
    # canva_1.create_line(sistem_x + 529, sistem_y + 440, sistem_x + 492, sistem_y + 472, activefill="red", fill="green", dash=1)
    #
    # # j52 -- JRZ
    # canva_1.create_line(sistem_x + 631, sistem_y + 334, sistem_x + 596, sistem_y + 390, activefill="red", fill="green", dash=1)
    # canva_1.create_line(sistem_x + 596, sistem_y + 285, sistem_x + 631, sistem_y + 334, activefill="red", fill="green", dash=1)
    #
    # # ТЕКСТ
    # canva_1.create_text(sistem_x + 705, sistem_y + 474, text="bridje", activefill="red", fill="#004D40")
    # canva_1.create_text(sistem_x + 463, sistem_y + 562, text="region gate", activefill="red", fill="grey50")
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # # global id_canva_alarm_on_off
    # id_canva_alarm_on_off = canva_1.create_image(773, 4, anchor=NW, tags=["img_alarm_on_off"])
    #
    # set_image(my_image_on)
    #
    # # id_canva_alarm_on_off_btn = canva_1.create_window(669, 6, anchor=NW, window=btn_alarm, width=29, height=29, tags=["btn_alarm_on_off"])
    #
    # canva_1.bind("<Button-1>", print_coords)
    # canva_1.tag_bind(id_canva_alarm_on_off, "<Button-1>", alarm_on_off_btn_1_click)
    #
    #
    #





def zoom_in():
    # canva_1.scale(qyzmw, 0, 0, 1.1, 1.1)
    # canva_1.scale(buiu4, 0, 0, 1.1, 1.1)
    # canva_1.scale(i7jr4, 0, 0, 1.1, 1.1)
    # canva_1.scale(me4iu, 0, 0, 1.1, 1.1)
    # canva_1.scale(ch9lk, 0, 0, 1.1, 1.1)
    # canva_1.scale(a9b1ds, 0, 0, 1.1, 1.1)

    # coords = canva_1.coords(qyzmw)
    # new_coords = [coord - 5 for coord in coords]
    # canva_1.coords(qyzmw, *new_coords)
    return 0


def zoom_out():
    # frame_1.scale(canva_1, 0, 0, 0.9, 0.9)
    # canva_1.scale(buiu4, 0, 0, 0.9, 0.9)
    # canva_1.scale(i7jr4, 0, 0, 0.9, 0.9)
    # canva_1.scale(me4iu, 0, 0, 0.9, 0.9)
    # canva_1.scale(ch9lk, 0, 0, 0.9, 0.9)
    # canva_1.scale(a9b1ds, 0, 0, 0.9, 0.9)

    # coords = canva_1.coords(rectangle_id)
    # new_coords = [coord + 5 for coord in coords]
    # canva_1.coords(rectangle_id, *new_coords)
    return 0


def save_window_position():

    # root.geometry('1150x740+100+100')
    w = root.winfo_width()
    h = root.winfo_height()+20
    x = root.winfo_x()
    y = root.winfo_y()
    # w = 1150
    # h = 740

    geometry = ('%dx%d+%d+%d' % (w, h, x, y))
    # print(" geometry =  " + geometry)

    # print("geometry = " + geometry)
    # print(str(type(geometry)))

    bd_setting.save_update_to_base(my_path_bd_setting, "window_position", geometry)


def load_window_position():

    if bd_setting.check_base_setting(my_path_bd_setting, "window_position") == 0:
        return geometry_default

    else:
        geometry = bd_setting.reed_base_setting(my_path_bd_setting, "window_position")
        print(" geometry =  " + geometry)
        return geometry


def window_default():

    root.geometry(geometry_default)
    # root.grab_set()


class Window(Tk):
    def __init__(self):
        super().__init__()

        # конфигурация окна
        # self.title("Новое окно")
        # self.geometry("280x280")

        # MEНЮ

        # определение кнопки
        # self.button = ttk.Button(self, text="закрыть")
        # self.button["command"] = self.button_clicked
        # self.button.pack(anchor="center", expand=1)

    # def button_clicked(self):
    #     self.destroy()


root = Tk()
root.title("VIJU INTEL")
# root.geometry('1150x740+100+100')
root.geometry(load_window_position())
# root.geometry(geometry_default)
# root.grab_set()
icon = PhotoImage(file=my_path_icon)
root.iconphoto(False, icon)


def glb_sett():
    print(" glb_sett(): ")
    # global_setting(root)
    # print(" root_x = " + str(root.winfo_x()) + "  root_y = " + str(root.winfo_y()))

    global_setting_window = Toplevel()
    global_setting_window.title("Глобальные Настройки ")
    w = 600
    h = 400
    x = root.winfo_x()+200
    y = root.winfo_y()+200
    global_setting_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    global_setting_window.grab_set()
    #
    #
    #
    #
    #
    # # создаем набор вкладок
    # notebook = ttk.Notebook(global_setting_window)
    # notebook.pack(expand=True, fill=BOTH)
    #
    # # создаем пару фреймвов
    # frame1 = ttk.Frame(notebook)
    # frame2 = ttk.Frame(notebook)
    #
    # frame1.pack(fill=BOTH, expand=True)
    # frame2.pack(fill=BOTH, expand=True)
    #
    # # добавляем фреймы в качестве вкладок
    # # text_1 = Text(font=('Entry', '25', 'bold'), text="Python")
    # notebook.add(frame1, text="Python")
    # notebook.add(frame2, text="Java")

    # root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # root.grab_set()

    pass


def load_setting():
    print(" *******  def load_setting(): ************")

    # btn_aCHCGU.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")
    # print("btn_aCHCGU = " + str(type(btn_aCHCGU)))
    load_sound_select_mp3()
    load_sound()
    load_color()


def load_color():

    if bd_setting.check_base_setting(my_path_bd_setting, "fon_color") == 0:
        pass
    else:
        fon_color = bd_setting.reed_base_setting(my_path_bd_setting, "fon_color")
        canva_1.config(bg=fon_color)
        my_text.config(bg=fon_color)
        settings_menu.config(bg=fon_color)


def load_sound_select_mp3():
    global int_sound_chouse
    if bd_setting.check_base_setting(my_path_bd_setting, "sound_netral") == 0:
        int_sound_chouse = 1
    else:
        int_sound_chouse = int(bd_setting.reed_base_setting(my_path_bd_setting, "sound_netral"))


def load_sound():
    l_l_s = bd_setting.reed_base_sound_one(my_path_bd_sound_one)
    print("reed_base_my_sound_one ** = " + str(l_l_s))


    # print(" len List_sound = " + str(len(list_sound)))
    # print("List_sound = " + str(list_sound))
    # print("List_sound = " + str(list_sound[1][0]))

    # label_style = ttk.Style()
    # label_style.configure("My.TLabel",  # имя стиля
    #                       font="helvetica 14",  # шрифт
    #                       foreground="#004D40",  # цвет текста
    #                       padding=10,  # отступы
    #                       background="#B2DFDB")  # фоновый цвет
    i = 0
    errors = 0
    while i < len(l_l_s):
        # print(list_sound[i][0])  # применяем индекс для получения элемента
        btn_id = canva_1.itemcget(str(l_l_s[i][0]), "window")
        print("btn_id (" + str(i) + ") = " + str(btn_id) + ",  " + str(l_l_s[i][0]))
        print(type(btn_id))

        for systema in find_all_canvas:
            # print(elements)
            # list_system.append(canva_1.itemcget(elements, "tags"))

            # if ("clr" and canva_1.itemcget(elements, "tags"))  in last_line_text:
            if canva_1.itemcget(systema, "tags")[0:6] in str(l_l_s[i][0]):
                btn_id = canva_1.itemcget(systema, "window")
                b_alarm = root.nametowidget(btn_id)
                # b_alarm2 = root.nametowidget(b_alarm)
                guard_sound_one.click_guard_system_sound_one(str(l_l_s[i][0]))
                print("btn_alarm = " + str(b_alarm) )
                btn_sound_on(b_alarm)

        # btn_alarm = Button().config()
        # btn_alarm = Button().children(btn_id)
        # b_alarm = root.nametowidget(save_id_btn_click)
        # # b_alarm = Button.info
        #
        # # btn_alarm2 = Button.config(btn_id, fg="blue violet")
        # print("btn_alarm = " + str(b_alarm) + ",  " + str(b_alarm['text']))
        # print("type(b_alarm) = " + str(type(b_alarm)))
        # # btn_alarm2 = Button.nametowidget(btn_alarm)
        # # print("type(btn_alarm2) = " + str(type(btn_alarm2)))
        # # btn2_id = getattr(root, str(list_sound[i][0]))
        # # btn2_id = Button.widgetName(str(list_sound[i][0]))
        # # print("btn2_id = " + str(btn2_id))
        #
        # if isinstance(b_alarm, tkinter.Button):
        #     print("ОК")
        #     btn_sound_on(b_alarm)
        #     # b_alarm.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")
        #     guard_sound_one.click_guard_system_sound_one(str(l_l_s[i][0]))
        #     print("str(l_l_s[i][0]['text'] = " + str(l_l_s[i][0]))
        #     print("b_alarm.widget['text'] = " + str(b_alarm['text']))
        # else:
        #     print("btn_id (" + str(i) + ") = " + str(btn_id) + "************ E R R O R  *************")

        # btn3 = "btn_a" + str(list_sound[i][0])
        # print("btn3_id = " + "KMQ4V")
        # btn3.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")

        # btn_alarm.config(background="SystemButtonFace")
        i += 1

        # event.widget.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")

    # btn_aCHCGU.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")
    # print("btn_aCHCGU = " + str(type(btn_aCHCGU)))


def btn_sound_on(b_alarm):

    b_alarm.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")


# Нужно чтобы выводить в консоле координаты на канве куда тыкаешь мышкой во время проектирования
def print_coords(event):
    print("def print_coords(event): ")
    try:
        print(event.x, event.y)

        print("print_coords : " + (str(event)))
        # print("Файл открыт")
    except:
        print("except")


    # print(event.x, event.y)
    #
    # print("print_coords : " + (str(event)))
    # print(" -----'text'  " + (str(event.widget['text'])))
    # print(" --- id :  " + (str(event.widget)))
    # print(" -----'bg'  " + (str(event.widget['bg'])))


def clicked_BTN (event):

    global save_id_btn_click

    # if event.widget = None: print("WIDGET NONE")
    #
    # else:

    try:
        print("clicked_BTN : " + (str(event)) )
        print("event type = " + str(type(event)))
        print(" -----'text'  " + (str(event.widget['text'])))
        print(" --- id :  " + (str(event.widget)))
        print(" -----'bg'  " + (str(event.widget['bg'])))
        print(" -----'fg'  " + (str(event.widget['fg'])))
        print(" -----'font'  " + (str(event.widget['font'])))

        save_id_btn_click = root.nametowidget((str(event.widget)))
        print("save_id_btn_click =  " + (str(save_id_btn_click)))
        # set_btn_system_control(event)
        guard_sound_one_cheek(event)

    except Exception as e:

        print("clicked_BTN (event):  ОШИБКА !")
        print(e)

    # print("clicked_BTN : " + (str(event)))
    # print(" -----'text'  " + (str(event.widget['text'])))
    # print(" --- id :  " + (str(event.widget)))
    # print(" -----'bg'  " + (str(event.widget['bg'])))
    # print(" -----'fg'  " + (str(event.widget['fg'])))
    # print(" -----'font'  " + (str(event.widget['font'])))

    # event.widget.config(background="red")

    # event.widget.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")

    # print(f"Нажата клавиша {event.keysym}")

    # btn["text"] ="11"

def set_btn_system_control(event):

     event.widget.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")


def guard_sound_one_cheek(event):

    print("save_id_btn_click = " + str(event.widget['text']))
    result = guard_sound_one.click_guard_system_sound_one(str(event.widget['text']))
    print("result = " + str(result))

    if result == 0:
        add_guard_sound_one_cheek(event)
        bd_setting.save_del_to_base_sound_one(my_path_bd_sound_one, str(event.widget['text']))

    else:
        del_guard_sound_one_cheek(event)
        bd_setting.save_del_to_base_sound_one(my_path_bd_sound_one, str(event.widget['text']))

    # event.widget.config(fg=save_atr_btn_add[0], font=save_atr_btn_add[1], background=save_atr_btn_add[-1])


def add_guard_sound_one_cheek(event):

    event.widget.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")

    # print("result  event = " + str(type(event)))


def del_guard_sound_one_cheek(event):

    # save_id_btn_click = (str(event.widget['text']))

    if str(event.widget['text']) in ("Q1U-IU" + "2-3Q2G" + "9IPC-E" + "H1-ESN" + "ZXA-V6" + "92D-OI"):
        event.widget.config(fg=save_atr_btn_del[0], font=save_atr_btn_del[1], background=save_atr_btn_del[3])
    else:
        event.widget.config(fg=save_atr_btn_del[0], font=save_atr_btn_del[1], background=save_atr_btn_del[2])
        # print("save_atr_btn_del[2] =  " + (str(save_atr_btn_del[2])))






# btn_alarm.config(background="SystemButtonFace")
##  canva_1.itemcget(elements, "tags"):
# #                  # print(elements)
#   btn_id = canva_1.itemcget(elements, "window")
#   btn_alarm = root.nametowidget(btn_id)

# licked_BTN : <ButtonPress event state=Mod1 num=1 x=33 y=8>
#  -----'text'  QYZM-W
#  --- id :  .!button
#  -----'bg'  SystemButtonFace
#  -----'fg'  SystemButtonText
#  -----'font'  TkDefaultFont
# clicked_BTN : <ButtonPress event state=Mod1 num=1 x=35 y=9>
#  -----'text'  QYZM-W
#  --- id :  .!button
#  -----'bg'  grey76
#  -----'fg'  blue violet
#  -----'font'  Entry 9 bold


# MEНЮ

# root.option_add("*tearOff", FALSE)  # отключает пунктирную линию в подменю, которая совершенно не нужна


def select_color():
    result = colorchooser.askcolor(initialcolor="black")
    # canva_1.configure(canva_1, bg="grey87")
    print("  --- ***************** ---  ")
    print("  --- ***************** ---  ")
    print("  ---  def select_color():  --- > " + (str(result)))
    print("  --- ***************** ---  ")
    print("  --- ***************** ---  ")
    # canva_1["foreground"] = result[1]
    canva_1.config(bg = result[1])
    my_text.config(bg=result[1])
    settings_menu.config(bg=result[1])

    bd_setting.save_update_to_base(my_path_bd_setting, "fon_color", str(result[1]))


def help_click():
 #  top1 = Toplevel(root, bg="light blue")
 #    messagebox.showinfo("'`ёшкарала`", "едрён батон", parent=frame_1)
    messagebox.showinfo("'`ёшкарала`", "едрён батон", parent=root)


def alarm_sound(system_alarm):
    # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA alarm_sound(int_int): =  " + (str)(int_sound_chouse))

    # guard_slovar.poisk_1(guard_list_system_sound, "QYZM-W", 5)

    # on_of_guard = guard_sound.proverka_sound_guard(guard_list_system_sound, system_alarm)
    # print("********************   alarm_sound(): on_of_guard = " + (str( on_of_guard)))
    # if on_of_guard == 1:
    #     return

    # print("********************   alarm_sound(): save_guard_slovar_sound = " + (str(save_guard_slovar_sound)))
    # guard_sound.proverka_sound_guard()

    # ii = bd_setting.reed_base_sound_one_column(my_path_bd_sound_one)
    # print("ii type : " + str(type(ii)))
    # print("ii = " + str(ii[0][0]))

    # если есть система где обнаружен нетрал в безе систем которые надо проверять, то ничего не делаем
    # т.е. проигрываем звук
    if system_alarm in guard_sound_one.get_guard_set_system_sound_one():
        pass
    else:
        # если база систем которые надо проверять, пуста, то ничего не делаем
        # т.е. идёт звук на любую систему на карте
        if int(bd_setting.reed_base_sound_one_column(my_path_bd_sound_one)[0][0]) == 0:
            pass
        else:
        #     # если база систем которые надо проверять, НЕ пуста, то завершаем def метод
            return

    if image_sound_on_off == "on":

        if int_sound_chouse == 1:
            playsound(my_path_mp3_01, FALSE)
        elif int_sound_chouse == 2:
            playsound(my_path_mp3_02, FALSE)
        elif int_sound_chouse == 3:
            playsound(my_path_mp3_03, FALSE)
        elif int_sound_chouse == 4:
            playsound(my_path_mp3_04, FALSE)
        elif int_sound_chouse == 5:
            playsound(my_path_mp3_05, FALSE)
        elif int_sound_chouse == 6:
            playsound(my_path_mp3_06, FALSE)
        elif int_sound_chouse == 7:
            playsound(my_path_mp3_07, FALSE)
        elif int_sound_chouse == 8:
            playsound(my_path_mp3_08, FALSE)
        elif int_sound_chouse == 9:
            playsound(my_path_mp3_09, FALSE)
        elif int_sound_chouse == 10:
            playsound(my_path_mp3_10, FALSE)
        elif int_sound_chouse is None:
            playsound(my_path_mp3_01, FALSE)


def chouse_sound_1():
    global int_sound_chouse
    int_sound_chouse = 1
    bd_setting.save_update_to_base(my_path_bd_setting, "sound_netral", str(int_sound_chouse))
    # alarm_sound()


def chouse_sound_2():
    # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))

    global int_sound_chouse
    int_sound_chouse = 2
    bd_setting.save_update_to_base(my_path_bd_setting, "sound_netral", str(int_sound_chouse))
    # alarm_sound()


def chouse_sound_3():
    # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))

    global int_sound_chouse
    int_sound_chouse = 3
    bd_setting.save_update_to_base(my_path_bd_setting, "sound_netral", str(int_sound_chouse))
    # alarm_sound()


def chouse_sound_4():
    # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))

    global int_sound_chouse
    int_sound_chouse = 4
    bd_setting.save_update_to_base(my_path_bd_setting, "sound_netral", str(int_sound_chouse))
    # alarm_sound()


def chouse_sound_5():
    # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))

    global int_sound_chouse
    int_sound_chouse = 5
    bd_setting.save_update_to_base(my_path_bd_setting, "sound_netral", str(int_sound_chouse))
    # alarm_sound()


def chouse_sound_6():
    # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))

    global int_sound_chouse
    int_sound_chouse = 6
    bd_setting.save_update_to_base(my_path_bd_setting, "sound_netral", str(int_sound_chouse))
    # alarm_sound()


def chouse_sound_7():
    # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))

    global int_sound_chouse
    int_sound_chouse = 7
    bd_setting.save_update_to_base(my_path_bd_setting, "sound_netral", str(int_sound_chouse))
    # alarm_sound()


def chouse_sound_8():
    # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))

    global int_sound_chouse
    int_sound_chouse = 8
    bd_setting.save_update_to_base(my_path_bd_setting, "sound_netral", str(int_sound_chouse))
    # alarm_sound()


def chouse_sound_9():
    # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))

    global int_sound_chouse
    int_sound_chouse = 9
    bd_setting.save_update_to_base(my_path_bd_setting, "sound_netral", str(int_sound_chouse))
    # alarm_sound()


def chouse_sound_10():
    # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))

    global int_sound_chouse
    int_sound_chouse = 10
    bd_setting.save_update_to_base(my_path_bd_setting, "sound_netral", str(int_sound_chouse))
    # alarm_sound()

# def chouse_sound_1():

#       int_sound_chouse = int_int

#       if  int_int == 1:  alarm_sound(1)
#       elif int_int == 2: alarm_sound(2)

# playsound('alarm_1.mp3', winsound.SND_FILENAME | winsound.SND_ASYNC)
# playsound('alarm_1.mp3')


def clear_console():
   
   # os.system('clear')
   if os.name == 'nt':
      os.system('clc')
   else:
      os.system('clear')


def click_TEST_button():
    print("  ---  click_TEST_button():   ---  ")


    # clear_console()

    # last_line_text = " TEST "

    # find_system_alarm.add_alarm_timers(((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M')) , "TEST")

    # proverka_na_sovpadenia()
    global last_line_text
    last_line_text = " 5-P1Y2 ESS "

   # my_text.insert(CURRENT, "\n" + last_line_text)
    my_text.insert('0.0', "\n" + last_line_text)

    proverka_na_sovpadenia()

    # obrabotka_timers_slovar()
#'KJ-QWL', 'KMQ4-V', 'SVB-RE', '5-P1Y2', 'J52-BH',


def click_TuKTuK_button():
    print("  ---  click_TuKTuK_button():   ---  ")

    # last_line_text = " TEST "

    # find_system_alarm.add_alarm_timers(((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M')) , "TEST-2")
    global last_line_text
    last_line_text = " 5-P1Y2* Mistress 5"

   # my_text.insert(CURRENT, "\n" + last_line_text)
    my_text.insert('0.0', "\n" + last_line_text)

    proverka_na_sovpadenia()

    # obrabotka_timers_slovar()


# with Image.open("alarm_on.png") as image:
#     #    im.rotate(45).show()

#      # alarm_on_off = ImageTk.PhotoImage(resized_image_on)
#      resized_image_on = image.reduce(3)
#      alarm_on_off = ImageTk.PhotoImage(resized_image_on)

# def alarm_on_off_btn_1_click():
#     print("К Л И К  - 1")
#     # print(event)

#     global image_sound_on_off
#     # global id_canva_alarm_on_off

#     if image_sound_on_off == "on":

#         print("К Л И К  - ON ")

#         with Image.open("alarm_off.png") as image:

#              resized_image_on = image.reduce(3)
#              alarm_on_off = ImageTk.PhotoImage(resized_image_on)
#              # draw = ImageDraw.Draw(image)
#              # img = PhotoImage(alarm_on_off)
#              image_sound_on_off = "off"
#              # id_canva_alarm_on_off = canva_1.create_image(673, 16, anchor=NW, image=alarm_on_off, tags=["alarm_on_off"] )
#              btn_alarm.config( image=alarm_on_off  )

#     else:

#         print("К Л И К  - OFF ")

#         with Image.open("alarm_on.png") as image:


#              resized_image_on = image.reduce(3)
#              alarm_on_off = ImageTk.PhotoImage(resized_image_on)
#              # draw = ImageDraw.Draw(image)
#              image_sound_on_off = "on"
#              # id_canva_alarm_on_off = canva_1.create_image(673, 16, anchor=NW, image=alarm_on_off, tags=["alarm_on_off"] )
#              btn_alarm.config(  image=alarm_on_off )


# @!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# def alarm_on_off_btn_1_click():
#     print("К Л И К  - 1")
#     # print(event)

#     global image_sound_on_off
#     # global id_canva_alarm_on_off

#     if image_sound_on_off == "on":

#         print("К Л И К  - ON ")

#         set_image(my_image_off)

#         image_sound_on_off = "off"

#     else:

#         print("К Л И К  - OFF ")

#         set_image(my_image_on)

#         image_sound_on_off = "on"


# def load_image(name):
#     with Image.open(name) as img:
#         # img = Image.open(name)
#         img.thumbnail((23, 29), Image.ANTIALIAS)

#         return ImageTk.PhotoImage(img)

# def set_image(image):
#     # canvas.delete("all")
#     # canvas.create_image(100,115,image=image)

#     btn_alarm.config(  image=image )


# my_image_on = load_image(my_path_alarm_on_png)
# my_image_off= load_image(my_path_alarm_off_png)


# @!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# def alarm_on_off_btn_1_click():
#     print("К Л И К  - 1")
#     # print(event)

#     global image_sound_on_off
#     # global id_canva_alarm_on_off

#     if image_sound_on_off == "on":

#         print("К Л И К  - ON ")

#         set_image(my_image_off)


#         image_sound_on_off = "off"

#     else:

#         print("К Л И К  - OFF ")

#         set_image(my_image_on)

# image_sound_on_off = "on"


def alarm_on_off_btn_1_click(event):
    print("К Л И К  - 1")
    # print(event)

    global image_sound_on_off
    # global id_canva_alarm_on_off

    if image_sound_on_off == "on":

        # print("К Л И К  - ON ")

        set_image(my_image_off);
        image_sound_on_off = "off"



    else:

        # print("К Л И К  - OFF ")

        set_image(my_image_on);
        image_sound_on_off = "on"


def load_image_2(name):
    photoImage = PhotoImage(file=name)
    photoImage = photoImage.zoom(1, 1)

    return photoImage


def load_image(name):
    return PhotoImage(file=name)


def set_image(image):
    # canvas.delete("all")
    # canvas.create_image(100,115,image=image)

    # btn_alarm.config ( image=image )

    canva_1.itemconfigure("img_alarm_on_off", image=image)


my_image_on = load_image(my_path_alarm_on_png)
my_image_off = load_image(my_path_alarm_off_png)

my_image_btn_vol_off = load_image_2(my_path_vol_off_btn)

# width=ширина, height=высота


# subprocess.run(["python", "другой_скрипт.py"])


# python = sys.executable
#     os.execl(python, python, *sys.argv)

# def restart_program():
#     subprocess.call(['python', 'main.py'])
#     sys.exit(0)


def compact_mode():
    # finish()
    # os.system(my_path_test_6)
    # subprocess.run(['python', 'test_6.py'])
    # Запуск первого скрипта
    # subprocess.Popen(["python", "test_6.py"])
    # python = sys.executable
    # # os.execl(python, python, *sys.argv)
    # subprocess.call(['python', 'test_6.py'])
    # # sys.exit(0)
    # finish()
    # subprocess.run(["python", my_path_test_6])
    root.geometry('850x489+100+100')
    canva_1.delete("all")
    full_canvas_1(-100, -180)
    full_canvas_2(-100, -180)

def fool_mode():
    # finish()
    # os.system('main.py')
    root.geometry('950x740+100+100')
    canva_1.delete("all")
    full_canvas_1(-100, 50)
    full_canvas_2(-100,50)

# @!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!












#      М Е Н Ю



main_menu = Menu(root, activebackground="red", tearoff=0)

settings_menu = Menu(main_menu, activebackground="red", tearoff=0)

sound_menu = Menu(settings_menu, activebackground="red", tearoff=0)
sound_menu.add_command(label="Alarm sound-1", command=chouse_sound_1)
sound_menu.add_command(label="Alarm sound-2", command=chouse_sound_2)
sound_menu.add_command(label="Alarm sound-3", command=chouse_sound_3)
sound_menu.add_command(label="Alarm sound-4", command=chouse_sound_4)
sound_menu.add_command(label="Alarm sound-5", command=chouse_sound_5)
sound_menu.add_command(label="Alarm sound-6", command=chouse_sound_6)
sound_menu.add_command(label="Alarm sound-7", command=chouse_sound_7)
sound_menu.add_command(label="Alarm sound-8", command=chouse_sound_8)
sound_menu.add_command(label="Alarm sound-9", command=chouse_sound_9)
sound_menu.add_command(label="Alarm sound-10", command=chouse_sound_10)
# sound_menu.add_command(label="Alarm sound-4", command=alarm_sound)
settings_menu.add_cascade(label="Sound", menu=sound_menu)

color_menu = Menu(settings_menu, activebackground="red", tearoff=0)
color_menu.add_command(label="Color Fon", command=select_color)
settings_menu.add_cascade(label="Color", menu=color_menu)

window_menu = Menu(settings_menu, activebackground="red", tearoff=0)
window_menu.add_command(label=" window default size ", command=window_default)
settings_menu.add_cascade(label="Window", menu=window_menu)

view_menu = Menu(main_menu, activebackground="red", tearoff=0)
# view_menu.add_command(label="Fool mode", command=fool_mode)
# view_menu.add_command(label="Compact mode", command=compact_mode)


main_menu.add_cascade(label="Настройки", menu=settings_menu)
main_menu.add_cascade(label="Вид", menu=view_menu)
main_menu.add_cascade(label="Глобальные Настройки", command=glb_sett)

root.config(menu=main_menu)
settings_menu.config(bg="blue")

#    END  M E Н Ю

















#    C O N T E X T     M E N U

# def global_guard_get():
#     # global save_guard_slovar_sound, save_guard_list_system_sound
#     save_guard_slovar_sound = guard_sound.get_save_guard_slovar_sound()
#     save_guard_list_system_sound = guard_sound.save_guard_list_system_sound()



# def compact_mode():
#     finish()
#     os.system('test_6.py')

def pop_up_context_menu_add_system_guard():

    # print("# Сontext menu: " + (distance_guard.get()))
    # print("save_id_btn_click =  " + (str(save_id_btn_click)))

    # save_guard_slovar_sound[save_id_btn_click] = distance_guard.get()
    # print(save_guard_slovar_sound)

    guard_sound.add_sound_system(save_id_btn_click, distance_guard.get())


    # save_event_guard_list_system_sound.widget.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")
    # event.widget.config(fg="blue violet", font=('Entry', '9', 'bold'), background="grey76")
    # btn_id = root.nametowidget(str(save_id_btn_click))

    # btn_id = Button.config()
    # button_identities = []
    # bname = (button_identities[save_id_btn_click])

    # button_identities.config(fg=save_atr_btn_add[0], font=save_atr_btn_add[1], background=save_atr_btn_add[-1])
    btn_id_set_guard.config(fg=save_atr_btn_add[0], font=save_atr_btn_add[1], background=save_atr_btn_add[-1] )

    # save_event_guard_list_system_sound.widget.config(fg=save_atr_btn_add[0], font=save_atr_btn_add[1], background=save_atr_btn_add[-1])


    get_save_guard_slovar_sound()
    # save_guard_list_system_sound

    # global_guard_get()
    # save_guard_slovar_sound = guard_sound.get_save_guard_slovar_sound()
    # save_guard_list_system_sound = guard_sound.save_guard_list_system_sound()

def pop_up_context_menu_del_system_guard():

    # print("# Сontext menu: " + (distance_guard.get()))
    # print("save_id_btn_click =  " + (str(save_id_btn_click)))



    guard_sound.del_sound_system(save_id_btn_click)
    # save_event_guard_list_system_sound.widget.config(fg=save_atr_btn[0], font=save_atr_btn[1], background=save_atr_btn[-1])
    # save_event_guard_list_system_sound.widget.config(fg="SystemButtonText", font=('TkDefaultFont'), background="SystemButtonFace")
    # save_guard_list_system_sound

    if save_id_btn_click in ("Q1U-IU" + "2-3Q2G" + "9IPC-E" + "H1-ESN" + "ZXA-V6" + "92D-OI"):
        save_event_guard_list_system_sound.widget.config(fg=save_atr_btn_del[0], font=save_atr_btn_del[1], background=save_atr_btn_del[3])
    else:
        save_event_guard_list_system_sound.widget.config(fg=save_atr_btn_del[0], font=save_atr_btn_del[1], background=save_atr_btn_del[2])
        # print("save_atr_btn_del[2] =  " + (str(save_atr_btn_del[2])))

    get_save_guard_slovar_sound()
    # global_guard_get()
    # btn_aQ1UIU.config(background="grey76")
    # btn_a23Q2G.config(background="grey76")
    # btn_a9IPCE.config(background="grey76")
    # btn_aH1ESN.config(background="grey76")
    # btn_aZXAV6.config(background="grey76")
    # btn_a92DOI.config(background="grey76")



def pop_up_context_menu_del_all_system_guard():
    print(save_guard_slovar_sound)
    # guard_sound.del_all_sound_system()

    # get_save_guard_slovar_sound()
def get_save_guard_slovar_sound():


    print(" def get_save_guard_slovar_sound():")
    global save_guard_slovar_sound
    save_guard_slovar_sound = guard_sound.get_save_guard_slovar_sound()
    # print(";;;;;;;;;;;;;;get_save_guard_slovar_sound():"+ "\n" +" save_guard_slovar_sound = " + (str(save_guard_slovar_sound)))


# def test_distance():
#     print("@@@@@@@@@@@@@@@@@ def test_distance(): " + (str(distance_guard.get())))
#     # save_event_guard_list_system_sound = event
#     change_distance()
def change_distance():
    get_save_guard_slovar_sound()
    save_guard_slovar_sound = guard_sound.get_save_guard_slovar_sound()
    # print("####### def change_distance(): " + (distance_guard.get()))
    # print("save_id_btn_click =  " + (str(save_id_btn_click)))



    if save_id_btn_click in save_guard_slovar_sound:
        print(" Система уже охранятеся ! новая дистанция : " + (str(distance_guard.get())))
        # перезапись ключа(cистемы) с новой дистанцией срабатываения
        guard_sound.add_sound_system(save_id_btn_click, distance_guard.get())
        get_save_guard_slovar_sound()


# global check
# check = StringVar()
# menu_file.add_checkbutton(label='Check', variable=check, onvalue=1, offvalue=0)
# radio = StringVar()
# menu_file.add_radiobutton(label='One', variable=radio, value=1)
# menu_file.add_radiobutton(label='Two', variable=radio, value=2)


def clear_systema():
    pass


context_menu_BTN = Menu(root, tearoff=0)

context_menu_BTN.add_command(label ="+ установить слежку", command=pop_up_context_menu_add_system_guard)
context_menu_BTN.add_command(label ="- снять слежку", command=pop_up_context_menu_del_system_guard)

distance_guard = StringVar()
distance_guard.set("5")


distance_menu = Menu(context_menu_BTN, activebackground="red", tearoff=0)
distance_menu.add_checkbutton(label ="1", variable=distance_guard, onvalue=1, offvalue=1, command=change_distance)
distance_menu.add_checkbutton(label ="2", variable=distance_guard, onvalue=2, offvalue=2, command=change_distance)
distance_menu.add_checkbutton(label ="3", variable=distance_guard, onvalue=3, offvalue=3, command=change_distance)
distance_menu.add_checkbutton(label ="4", variable=distance_guard, onvalue=4, offvalue=4, command=change_distance)
distance_menu.add_checkbutton(label ="5", variable=distance_guard, onvalue=5, offvalue=5, command=change_distance)
context_menu_BTN.add_cascade(label ="дистанция слежки ", menu=distance_menu)


context_menu_BTN.add_separator()

context_menu_BTN.add_command(label ="-- снять все слежки")
context_menu_BTN.add_separator()
context_menu_BTN.add_command(label=" чисто (clear)", command=clear_systema)

# context_menu_BTN.add_command(label =" вкл/выкл  общего звука", command=alarm_on_off_btn_1_click)

# print("# Сontext menu: " + (check.get()))


#   END  C O N T E X T     M E N U


def pop_up_context_menu_BTN_3(event):

    global btn_id_set_guard
    global save_id_btn_click
    global save_event_guard_list_system_sound
    global save_atr_btn
    error = 0

    # for elements in find_all_canvas:
    # window_id = canva_1.itemcget(elements, "window")
    # print(" -----'canva_1 -----'  " + canva_1.itemcget(str(event.widget['text'])),'tags'          )

    try:
        print("pop_up_context_menu_BTN(event): " + (str(event)))
        print(" -----'text'  " + (str(event.widget['text'])))
        print(" --- id :  " + (str(event.widget)))
        btn_id_set_guard = event.widget
        print(" -----'bg'  " + (str(event.widget['bg'])))
        print(" -----'fg'  " + (str(event.widget['fg'])))
        print(" -----'font'  " + (str(event.widget['font'])))

        # save_id_btn_click = root.nametowidget((str(event.widget)))
        save_id_btn_click = (str(event.widget['text']))
        print("save_id_btn_click =  " + (str(save_id_btn_click)))
        print("##################### Сontext menu: " + (distance_guard.get()))
        print(";;;;;;;;;;;;;;get_save_guard_slovar_sound():" + "\n" + " save_guard_slovar_sound = " + (str(save_guard_slovar_sound)))
        # set_btn_system_control(event)

        # save_event_guard_list_system_sound.widget.config(fg="SystemButtonText", font=('TkDefaultFont'), background="SystemButtonFace")
        # save_atr_btn = event.widget['fg'], event.widget['font'], event.widget['bg']

    except:
        print("pop_up_context_menu_BTN(event):  ОШИБКА !")
        print( save_guard_slovar_sound )
        error = 1

    if error == 0:
        try:
           context_menu_BTN.tk_popup(event.x_root, event.y_root)

        finally:
           save_event_guard_list_system_sound = event
           # change_distance()
           context_menu_BTN.grab_release()
           print("######################### finally: # distance_guard.get() =  " + (distance_guard.get()))

           # save_event_guard_list_system_sound = event
           # change_distance()


# print("##################### Сontext menu: " + (distance_guard.get()))

    # try:
    #    context_menu_BTN.tk_popup(event.x_root, event.y_root)
    # finally:
    #     context_menu_BTN.grab_release()


#   END  C O N T E X T     M E N U  ФУНКЦИЙ





# @!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def select_color():
    result = colorchooser.askcolor(initialcolor="black")
    # canva_1.fill_style(result[1])
    # label["foreground"] = result[1]


def click():
    print("Hello")


# Делаем отдельную функцию с напоминанием
# ЭТО ПРИМЕР
def remind():
    # Спрашиваем текст напоминания, который нужно потом показать пользователю
    print("О чём вам напомнить?")
    # Ждём ответа пользователя и результат помещаем в строковую переменную text
    # text = str(input())
    text = "********************  Н А П О М И Н А Н И Е    *************************"
    # Спрашиваем про время
    print("Через сколько минут?")
    # Тут будем хранить время, через которое нужно показать напоминание
    # local_time = float(input())
    local_time = 0.05
    # Переводим минуты в секунды
    local_time = local_time * 60
    # Ждём нужное количество секунд, программа в это время ничего не делает
    time.sleep(local_time)
    # Показываем текст напоминания
    print(text)
    ess_anim_del()


def ess_manager(tag_system, time):
    print("         ess_manager():   " + str(tag_system) + "  time = " + str(time))

    ess_time = 5 - time

    ess_anim(tag_system, ess_time)

    if time == 5:
        ess_anim_del()


def ess_anim(tag_system, ess_time):
    print("         ess_anim():       " + str(tag_system))
    global ess_msg_1, ess_msg_2, ess_msg_3
    ess_anim_del()

    ess_msg_1 = canva_1.create_rectangle(628, 555, 940, 656, width=4, outline="red", dash=(7, 8,))
    ess_msg_2 = canva_1.create_text(sistem_x + 615, sistem_y + 522, font=('Entry', '14', 'bold'), text="ESS", fill="blue")
    ess_msg_3 = canva_1.create_text(sistem_x + 728, sistem_y + 552, font=('Entry', '25', 'bold'),
                                    text=str(tag_system) + " (" + str(ess_time) + ")", fill="blue")

    # if len(find_system_alarm.ess_timers_slovar) == 1:
    #
    #     ess_msg_3 = canva_1.create_text(sistem_x + 728, sistem_y + 552, font=('Entry', '25', 'bold'), text=str(tag_system) + " ("
    #                                         + str(ess_time) + ")", fill="blue")
    #
    # elif len(find_system_alarm.ess_timers_slovar) == 2:
    #
    #     ess_msg_3 = canva_1.create_text(sistem_x + 728, sistem_y + 552, font=('Entry', '25', 'bold'),
    #                                     text=str(tag_system) + " (" + str(ess_time) + ")", fill="blue")


    # canva_1.delete(ess_msg_1, ess_msg_2, ess_msg_3)
    # th = Thread(target=remind, args=())
    # Создаём новый поток
    # th = Thread(target=remind, args=())
    # th.start()


def ess_anim_del():

    canva_1.delete(ess_msg_1, ess_msg_2, ess_msg_3)


# # Делаем отдельную функцию с напоминанием
# def remind():
#     # Спрашиваем текст напоминания, который нужно потом показать пользователю
#     print("О чём вам напомнить?")
#     # Ждём ответа пользователя и результат помещаем в строковую переменную text
#     # text = str(input())
#     text = "********************  Н А П О М И Н А Н И Е    *************************"
#     # Спрашиваем про время
#     print("Через сколько минут?")
#     # Тут будем хранить время, через которое нужно показать напоминание
#     # local_time = float(input())
#     local_time = 0.05
#     # Переводим минуты в секунды
#     local_time = local_time * 60
#     # Ждём нужное количество секунд, программа в это время ничего не делает
#     time.sleep(local_time)
#     # Показываем текст напоминания
#     print(text)
#     ess_anim_del()


# # Создаём новый поток
# th = Thread(target=remind, args=())
# И запускаем его
# th.start()






main_frame = Frame(root, relief=SOLID)

# btn_zoom_in = Button(root, text="Zoom In", command=zoom_in)
# btn_zoom_in.pack(side=TOP)

# btn_zoom_out = Button(root, text="Zoom Out", command=zoom_out)
# btn_zoom_out.pack(side=TOP)


# main_frame.pack(expand=1, fill=BOTH)

pw = PanedWindow(main_frame, bd=2, orient="horizontal", sashrelief="sunken")

frame_1 = Frame(pw, borderwidth=2, relief=RAISED)

# canva_1 = Canvas(frame_1, width=700, bg="grey87")
canva_1 = Canvas(frame_1, width=951, bg="grey87")
# self.canva.pack(fill=BOTH, expand=TRUE)

# wbtn=8
# hbtn=2

# xbtn=-0.19


# btn_relief=RIDGE # SUNKEN, RAISED, GROOVE, RIDGE

# b1 = Button(bg='white', text="QYZM-W", width=10, height=2).place(relx=0.3, rely=0.5)
# qyzmw = Button(canva_1, bg='white', text="QYZM-W", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.5, rely=0.8)
# buiu4 = Button(canva_1, bg='white', text="BU-IU4", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.5, rely=0.72)
# i7jr4 = Button(canva_1, bg='white', text="I-7JR4", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.35, rely=0.8)
# me4iu = Button(canva_1, bg='white', text="ME-4IU", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.35, rely=0.72)
# ch9lk = Button(canva_1, bg='white', text="CH9L-K", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.20, rely=0.8)
# a9b1ds = Button(canva_1, bg='white', text="9-B1DS", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.20, rely=0.72)
# a3knan = Button(canva_1, bg='white', text="3KNA-N", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.35, rely=0.64)
# q1uiu = Button(canva_1, bg='white', text="Q1U-IU", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.20, rely=0.90)
# kjkwl = Button(canva_1, bg='white', text="KJ-QWL", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.20, rely=0.50)
# kmq4V = Button(canva_1, bg='white', text="KMQ4-V", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.35, rely=0.50)
# svbre = Button(canva_1, bg='white', text="SVB-RE", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.35, rely=0.42)
# a5p1y2 = Button(canva_1, bg='white', text="5-P1Y2", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.5, rely=0.50)
# j52bh = Button(canva_1, bg='white', text="J52-BH", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.65, rely=0.50)
# clbqs = Button(canva_1, bg='white', text="C-LBQS", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.8, rely=0.50)
# bwi19 = Button(canva_1, bg='white', text="BWI1-9", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.8, rely=0.50)
# kl30j = Button(canva_1, bg='white', text="KL30-J", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.8, rely=0.42)
# r40i6 = Button(canva_1, bg='white', text="R40-I6", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.92, rely=0.42)
# qnjz4 = Button(canva_1, bg='white', text="Q-NJZ4", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+1.045, rely=0.42)
# nlpb0= Button(canva_1, bg='white', text="NLPB-0", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+1.045, rely=0.35)
# a3td6l= Button(canva_1, bg='white', text="3-TD9L", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.92, rely=0.35)
# cx1xf= Button(canva_1, bg='white', text="CX-1XF", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.8, rely=0.35)
# x4uvz= Button(canva_1, bg='white', text="X4UV-Z", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.58, rely=0.30)
# bkgq2= Button(canva_1, bg='white', text="BKG-Q2", width=wbtn, height=hbtn, relief=btn_relief).place(relx=xbtn+0.40, rely=0.28)


# btn_aQYZMW = Button(text="QYZM-W")
# btn_aBUIU4 = Button(text="BU-IU4")
# btn_aI7JR4 = Button(text="I-7JR4")
# btn_aME4IU = Button(text="ME-4IU")
# btn_aCH9LK = Button(text="CH9L-K")
# btn_a9B1DS = Button(text="9-B1DS")
# btn_a3KNAN = Button(text="3KNA-N")
# btn_aQ1UIU = Button(text="Q1U-IU")
# btn_aKJQWL = Button(text="KJ-QWL")
# btn_aKMQ4V = Button(text="KMQ4-V")
# btn_aSVBRE = Button(text="SVB-RE")
# btn_a5P1Y2 = Button(text="5-P1Y2")
# btn_aJ52BH = Button(text="J52-BH")
# btn_aCLBQS = Button(text="C-LBQS")
# btn_aBWI19 = Button(text="BWI1-9")
# btn_aKL30J = Button(text="KL30-J")
# btn_aR40I6 = Button(text="R4O-I6")
# btn_aQNJZ4 = Button(text="Q-NJZ4")
# btn_aNLPB0 = Button(text="NLPB-0")
# btn_a3TD9L = Button(text="3-TD9L")
# btn_aCX1XF = Button(text="CX-1XF")
# btn_aX4UVZ = Button(text="X4UV-Z")
# btn_aJRZB9 = Button(text="JRZ-B9")
# btn_aSB7IT = Button(text="S-B7IT")

# btn_aBKGQ2 = Button(text="BKG-Q2")

# btn_aZK495 = Button(text="Z-K495")
# btn_a84GQM = Button(text="8-4GQM")
# btn_aLXWNW = Button(text="LXWN-W")

# btn_aJSILL = Button(text="JSI-LL")
# btn_aU5XW7 = Button(text="U5-XW7")
# btn_aMUC05 = Button(text="M-UC05")
# btn_aSY0W2 = Button(text="SY0W-2")
# btn_aV7MID = Button(text="V7-MID")
# btn_aMZPHW = Button(text="MZPH-W")

# btn_aTEST = Button(text="T E S T", command = click_TEST_button)
# btn_aTuKTuK = Button(text="TuK-TuK", command = click_TuKTuK_button)


# btn_window_width=65

# sistem_x=-200
# sistem_y=-240

# aQYZMW = canva_1.create_window(sistem_x+500, sistem_y+500, anchor=NW, window=btn_aQYZMW, width=btn_window_width, tags=["QYZM-W"])
# aI7JR4 = canva_1.create_window(sistem_x+430, sistem_y+500, anchor=NW, window=btn_aI7JR4, width=btn_window_width, tags=["I-7JR4"])
# aBUIU4 = canva_1.create_window(sistem_x+500, sistem_y+470, anchor=NW, window=btn_aBUIU4, width=btn_window_width, tags=["BU-IU4"])
# aME4IU = canva_1.create_window(sistem_x+430, sistem_y+470, anchor=NW, window=btn_aME4IU, width=btn_window_width, tags=["ME-4IU"])
# aCH9LK = canva_1.create_window(sistem_x+360, sistem_y+500, anchor=NW, window=btn_aCH9LK, width=btn_window_width, tags=["CH9L-K"])
# a9B1DS = canva_1.create_window(sistem_x+360, sistem_y+470, anchor=NW, window=btn_a9B1DS, width=btn_window_width, tags=["9-B1DS"])
# a3KNAN = canva_1.create_window(sistem_x+430, sistem_y+440, anchor=NW, window=btn_a3KNAN, width=btn_window_width, tags=["3KNA-N"])
# aQ1UIU = canva_1.create_window(sistem_x+360, sistem_y+550, anchor=NW, window=btn_aQ1UIU, width=btn_window_width, tags=["Q1U-IU"])

# aJSILL = canva_1.create_window(sistem_x+360, sistem_y+595, anchor=NW, window=btn_aJSILL, width=btn_window_width, tags=["SI-LL"])
# aSY0W2 = canva_1.create_window(sistem_x+290, sistem_y+630, anchor=NW, window=btn_aSY0W2, width=btn_window_width, tags=["SY0W-2"])
# aMUC05 = canva_1.create_window(sistem_x+290, sistem_y+595, anchor=NW, window=btn_aMUC05, width=btn_window_width, tags=["M-UC05"])
# aV7MID = canva_1.create_window(sistem_x+220, sistem_y+630, anchor=NW, window=btn_aV7MID, width=btn_window_width, tags=["V7-MID"])
# aU5XW7 = canva_1.create_window(sistem_x+360, sistem_y+630, anchor=NW, window=btn_aU5XW7, width=btn_window_width, tags=["U5-XW7"])
# aMZPHW = canva_1.create_window(sistem_x+360, sistem_y+670, anchor=NW, window=btn_aMZPHW, width=btn_window_width, tags=["MZPH-W"])

# aKJQWL = canva_1.create_window(sistem_x+360, sistem_y+390, anchor=NW, window=btn_aKJQWL, width=btn_window_width, tags=["KJ-QWL"])
# aKMQ4V = canva_1.create_window(sistem_x+428, sistem_y+390, anchor=NW, window=btn_aKMQ4V, width=btn_window_width, tags=["KMQ4-V"])
# aSVBRE = canva_1.create_window(sistem_x+360, sistem_y+355, anchor=NW, window=btn_aSVBRE, width=btn_window_width, tags=["SVB-RE"])
# a5P1Y2 = canva_1.create_window(sistem_x+497, sistem_y+390, anchor=NW, window=btn_a5P1Y2, width=btn_window_width, tags=["5-P1Y2"])
# aJ52BH = canva_1.create_window(sistem_x+565, sistem_y+390, anchor=NW, window=btn_aJ52BH, width=btn_window_width, tags=["J52-BH"])
# aCLBQS = canva_1.create_window(sistem_x+633, sistem_y+390, anchor=NW, window=btn_aCLBQS, width=btn_window_width, tags=["C-LBQS"])
# aBWI19 = canva_1.create_window(sistem_x+700, sistem_y+390, anchor=NW, window=btn_aBWI19, width=btn_window_width, tags=["BWI1-9"])
# aKL30J = canva_1.create_window(sistem_x+700, sistem_y+355, anchor=NW, window=btn_aKL30J, width=btn_window_width, tags=["KL30-J"])
# aR40I6 = canva_1.create_window(sistem_x+768, sistem_y+340, anchor=NW, window=btn_aR40I6, width=btn_window_width, tags=["R4O-I6"])
# aQNJZ4 = canva_1.create_window(sistem_x+835, sistem_y+340, anchor=NW, window=btn_aQNJZ4, width=btn_window_width, tags=["Q-NJZ4"])
# aNLPB0 = canva_1.create_window(sistem_x+835, sistem_y+310, anchor=NW, window=btn_aNLPB0, width=btn_window_width, tags=["NLPB-0"])
# a3TD9L = canva_1.create_window(sistem_x+768, sistem_y+310, anchor=NW, window=btn_a3TD9L, width=btn_window_width, tags=["3-TD9L"])
# aCX1XF = canva_1.create_window(sistem_x+700, sistem_y+295, anchor=NW, window=btn_aCX1XF, width=btn_window_width, tags=["СX-1XF"])
# aX4UVZ = canva_1.create_window(sistem_x+530, sistem_y+295, anchor=NW, window=btn_aX4UVZ, width=btn_window_width, tags=["X4UV-Z"])
# aJRZB9 = canva_1.create_window(sistem_x+530, sistem_y+260, anchor=NW, window=btn_aJRZB9, width=btn_window_width, tags=["JRZ-B9"])
# aSB7IT = canva_1.create_window(sistem_x+455, sistem_y+260, anchor=NW, window=btn_aSB7IT, width=btn_window_width, tags=["S-B7IT"])
# aBKGQ2 = canva_1.create_window(sistem_x+455, sistem_y+295, anchor=NW, window=btn_aBKGQ2, width=btn_window_width, tags=["BKG-Q2"])
# aZK495 = canva_1.create_window(sistem_x+325, sistem_y+245, anchor=NW, window=btn_aZK495, width=btn_window_width, tags=["Z-K495"])
# a84GQM = canva_1.create_window(sistem_x+315, sistem_y+285, anchor=NW, window=btn_a84GQM, width=btn_window_width, tags=["8-4GQM"])
# aLXWNW = canva_1.create_window(sistem_x+325, sistem_y+320, anchor=NW, window=btn_aLXWNW, width=btn_window_width, tags=["LXWN-W"])


# aTEST = canva_1.create_window(sistem_x+220, sistem_y+280, anchor=NW, window=btn_aTEST, width=btn_window_width, tags=["TEST"])
# aTuKTuK = canva_1.create_window(sistem_x+220, sistem_y+320, anchor=NW, window=btn_aTuKTuK, width=btn_window_width, tags=["TuK-TuK"])


# canva_1.create_line(sistem_x+350, sistem_y+280, sistem_x+360, sistem_y+280, fill="blue")
# canva_1.create_line(10, 10, 20, 20, fill="blue")


# coord_CH = []
# coord_CH = canva_1.coords(aCH9LK)
# print(coord_CH)
# coord_CH_x1 = coords(aCH9LK)[0]
# print("**************** coord_CH_x1 = " + coord_CH_x1)
# canvas.create_line(10, 10, 200, 50)

# find_all_canvas = canva_1.find_all()
# print ("find_all_canvas  = " )
# print (find_all_canvas)
# print ("Всего элементов  = " )
# print (len(find_all_canvas))
# # Получаем
# CH_width = canva_1.itemcget(aCH9LK, "width")
# CH_height = canva_1.itemcget(aCH9LK, "height")

# print ("CH_width = " +  CH_width + ";   CH_height = " + CH_height)


# item_config = canva_1.itemconfig(1)


# print ("item_config = ")
# print (item_config)

# reed_tag = canva_1.itemcget(aCH9LK, "tags")
# print ("reed_tag = " + reed_tag )

# Button().
# .itemconfig(1, background ="red")

# btn_insert_id = canva_1.itemcget(aCH9LK, "window")
# print ("reed_BTN = ")
# print ( btn_insert_id )

# # listbox_name = str(listbox)

# lb = root.nametowidget(btn_insert_id)
# lb.config(background="red")


# btn_aBUIU4.flash()

# btn_aBUIU4.flash()

# print (" background = ")
# print (btn_aBUIU4.cget("background"))  # = SystemButtonFace


# btn_id = canva_1.itemcget(1, "window")
# btn_alarm = root.nametowidget(btn_id)
# btn_alarm.config(background="SystemButtonFace")

# find_all_canvas = canva_1.find_all()

# for elements in find_all_canvas:
#           print(elements)
#           list_system.append(canva_1.itemcget(elements, "tags"))


# поиск элемента по тэгу
# for elements in find_all_canvas:
#           # print(elements)
#           # list_system.append(canva_1.itemcget(elements, "tags"))
#           if "Q-NJZ4" == canva_1.itemcget(elements, "tags"):
#               # print(elements)
#               btn_id = canva_1.itemcget(elements, "window")
#               btn_alarm = root.nametowidget(btn_id)
#               btn_alarm.config(background="orange red")


canva_1.pack(anchor=CENTER, expand=1, fill=BOTH)
frame_1.pack(fill="both", expand=1)

pw.add(frame_1)

# canva_1.pack()


wbtn = 8

hbtn = 2

xbtn = -0.19


# adding weights so the button is center on the frame.
# frame.columnconfigure(0, weight=1)
# frame.rowconfigure(0, weight=1)
# style = Style(root)
# style.theme_use('clam')
# style.configure('my.TButton', bordercolor="red")

btn_aQYZMW = Button( text="QYZM-W")

# btn_aQYZMW = CustomButton( text="QYZM-W", class_="CustomButton")

# btn_aQYZMW.config(fg="blue violet", font = ('Entry','9','bold')     , background="grey76")

btn_aBUIU4 = Button(text="BU-IU4")
btn_aI7JR4 = Button(text="I-7JR4")
btn_aME4IU = Button(text="ME-4IU")
btn_aCH9LK = Button(text="CH9L-K")
btn_a9B1DS = Button(text="9-B1DS")
btn_a3KNAN = Button(text="3KNA-N")
btn_aQ1UIU = Button(relief=RIDGE, text="Q1U-IU", background="grey76")
btn_aKJQWL = Button(text="KJ-QWL")
btn_aKMQ4V = Button(text="KMQ4-V")
btn_aSVBRE = Button(text="SVB-RE")
btn_a5P1Y2 = Button(text="5-P1Y2")
btn_aJ52BH = Button(text="J52-BH")
btn_aCLBQS = Button(text="C-LBQS")
btn_aBWI19 = Button(text="BWI1-9")
btn_aKL30J = Button(text="KL3O-J")
btn_aR40I6 = Button(text="R4O-I6")
btn_aQNJZ4 = Button(text="Q-NJZ4")
btn_aNLPB0 = Button(text="NLPB-0")
btn_a3TD6L = Button(text="3-TD6L")
btn_aCX1XF = Button(text="CX-1XF")
btn_aX4UVZ = Button(text="X4UV-Z")
btn_aJRZB9 = Button(text="JRZ-B9")
btn_aV8WQS = Button(text="V8W-QS")
btn_aXW2XP = Button(text="XW-2XP")

btn_aCSZGD = Button(text="CS-ZGD")
btn_a3N3OO = Button(text="3-N3OO")
btn_aAG1FM = Button(text="A-G1FM")

btn_aZIUEP = Button(text="ZIU-EP")
btn_aP7ZR3 = Button(text="P7Z-R3")
btn_a4BE0M = Button(text="4-BE0M")
btn_aI7RIS = Button(text="I-7RIS")
btn_a23Q2G = Button(relief=RIDGE, text="2-3Q2G", background="grey76")

btn_a9IPCE = Button(relief=RIDGE, text="9IPC-E", background="grey76")

btn_aKMCWI = Button(text="KMC-WI")
btn_aVL3IM = Button(text="VL3I-M")
btn_aUQ93C = Button(text="UQ9-3C")

btn_aDCI77 = Button(text="DCI7-7")
btn_aJ7YR1 = Button(text="J7YR-1")
btn_aPKG47 = Button(text="PKG4-7")
btn_aEWN2U = Button(text="EWN-2U")

btn_aAHB84 = Button(text="AH-B84")

btn_aHB7RF = Button(text="HB7R-F")
btn_aOJPKH = Button(text="O-JPKH")
btn_aBGC1T = Button(text="B-GC1T")
btn_aJTAU5 = Button(text="JTAU-5")
btn_aF9F6Q = Button(text="F-9F6Q")

btn_aOJA8M = Button(text="OJ-A8M")
btn_aH1ESN = Button(relief=RIDGE, text="H1-ESN")
btn_aH1ESN.config(background="grey76")

btn_aCHCGU = Button(text="C-HCGU")
btn_aNTV01 = Button(text="NTV0-1")
btn_a448K1 = Button(text="4-48K1")
btn_aQFEEJ = Button(text="Q-FEEJ")
btn_a0P9ZI = Button(text="0P9Z-I")

btn_aSB7IT = Button(text="S-B7IT")

btn_aBKGQ2 = Button(text="BKG-Q2")

btn_aZK495 = Button(text="Z-K495")
btn_aYG82V = Button(text="YG-82V")

btn_aUBUQZ = Button(text="UB-UQZ")
btn_aXM4L0 = Button(text="XM-4L0")
btn_aQCWAZ = Button(text="QCWA-Z")
btn_aKV8SM = Button(text="KV-8SM")
btn_a4DTQK = Button(text="4DTQ-K")
btn_aB8OKJ = Button(text="B8O-KJ")
btn_a5LJMD = Button(text="5LJ-MD")
btn_a52GNZ = Button(text="52G-NZ")

btn_aEQI22 = Button(text="EQI2-2")
btn_aD4RH7 = Button(text="D4R-H7")
btn_aJ95MQ = Button(text="J9-5MQ")
btn_a313IB = Button(text="313I-B")
btn_aQ4DEC = Button(text="Q-4DEC")

btn_a6O5GY = Button(text="6-O5GY")

# $#########################
btn_aZXAV6 = Button(relief=RIDGE, text="ZXA-V6")
btn_aZXAV6.config(background="grey76")

btn_aTQ2DD = Button(text="T-Q2DD")
btn_aLRWDB = Button(text="LRWD-B")
btn_aQXQBA = Button(text="QXQ-BA")
btn_aX7RJW = Button(text="X7R-JW")
btn_aMHU4V = Button(text="M-HU4V")

btn_a84GQM = Button(text="8-4GQM")
btn_aLXWNW = Button(text="LXWN-W")

btn_aJSILL = Button(text="JSI-LL")
btn_aU5XW7 = Button(text="U5-XW7")
btn_aMUC05 = Button(text="M-UC0S")
btn_aSY0W2 = Button(text="SY0W-2")
btn_aV7MID = Button(text="V7-MID")
btn_aMZPHW = Button(text="MZPH-W")

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
btn_aXWJHT = Button(text="XW-JHT")
btn_aO94UA = Button(text="O94U-A")
btn_aCVGYO = Button(text="C-VGYO")
btn_aK8SQS = Button(text="K-8SQS")
btn_aNEHCS = Button(text="NEH-CS")

btn_aC4ZOS = Button(text="C-4ZOS")

btn_a3FJZF = Button(text="3F-JZF")
btn_a50WB9 = Button(text="5-0WB9")
btn_a2B7A3 = Button(text="2B7A-3")
btn_aW4FA9 = Button(text="W-4FA9")
btn_aPUWL4 = Button(text="PUWL-4")
btn_a1IXC0 = Button(text="1IX-C0")
btn_aY1918 = Button(text="Y-1918")
btn_aUJYHE = Button(relief=RIDGE,text="UJY-HE"); btn_aUJYHE.config(background="grey76")
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

btn_aRO90H = Button(text="RO90-H")
btn_aMAVDX = Button(text="MA-VDX")
btn_aWOAIJ = Button(text="WO-AIJ")
btn_a1GMJE = Button(text="1G-MJE")
btn_aCLP3N = Button(text="C-LP3N")
btn_a9F7PZ = Button(text="9F-7PZ")
btn_a92DOI = Button(relief=RIDGE,text="92D-OI"); btn_a92DOI.config(background="grey76")

btn_aZKYQ3 = Button(text="ZK-YQ3")





# btn_aTEST = Button(highlightbackground = "orange", highlightcolor= "red", bd=2, anchor=SW, image=my_image_btn_vol_off,  text="T E S T", compound="left", command = click_TEST_button)
btn_aTEST = Button(fg="blue violet", font=('Entry', '10', 'bold'), text="TEST", compound="left",
                   command=click_TEST_button)
# btn_aTuKTuK = Button(image=my_image_btn_vol_off, anchor="sw",  compound="left", text="TuK-TuK", command = click_TuKTuK_button)
btn_aTuKTuK = Button(anchor="se", image=my_image_btn_vol_off, text="TUK", compound="right", command=click_TuKTuK_button)

# canva_1.create_line(10, 10, 20, 20)

btn_window_width = 65

sistem_x = 50
sistem_y = 50

# aQYZMW = canva_1.create_window(sistem_x + 500, sistem_y + 500, anchor=NW, window=btn_aQYZMW, width=btn_window_width,
#                                tags=["QYZM-W"])

aQYZMW = canva_1.create_window(sistem_x + 500, sistem_y + 500, anchor=NW, window=btn_aQYZMW, width=btn_window_width,
                               tags=["QYZM-W", "I-7JR4", "BU-IU4"])

# kv_1=canva_1.create_rectangle(sistem_x+499, sistem_y+499, sistem_x+566, sistem_y+526)

# aI7JR4 = canva_1.create_window(sistem_x + 430, sistem_y + 500, anchor=NW, window=btn_aI7JR4, width=btn_window_width,
#                                tags=["I-7JR4"])
aI7JR4 = canva_1.create_window(sistem_x + 430, sistem_y + 500, anchor=NW, window=btn_aI7JR4, width=btn_window_width,
                               tags=["I-7JR4", "QYZM-W", "CH9L-K", "ME-4IU"])
aBUIU4 = canva_1.create_window(sistem_x + 500, sistem_y + 470, anchor=NW, window=btn_aBUIU4, width=btn_window_width,
                               tags=["BU-IU4", "QYZM-W", "ME-4IU"])
# aBUIU4 = canva_1.create_window(sistem_x + 500, sistem_y + 470, anchor=NW, window=btn_aBUIU4, width=btn_window_width,
#                                tags=["BU-IU4", "QYZM-W", "ME-4IU"])
aME4IU = canva_1.create_window(sistem_x + 430, sistem_y + 470, anchor=NW, window=btn_aME4IU, width=btn_window_width,
                               tags=["ME-4IU", "BU-IU4", "9-B1DS", "I-7JR4", "3KNA-N"])
aCH9LK = canva_1.create_window(sistem_x + 360, sistem_y + 500, anchor=NW, window=btn_aCH9LK, width=btn_window_width,
                               tags=["CH9L-K", "9-B1DS", "I-7JR4", "Q1U-IU"])
a9B1DS = canva_1.create_window(sistem_x + 360, sistem_y + 470, anchor=NW, window=btn_a9B1DS, width=btn_window_width,
                               tags=["9-B1DS", "CH9L-K", "ME-4IU", "KJ-QWL"])
a3KNAN = canva_1.create_window(sistem_x + 430, sistem_y + 440, anchor=NW, window=btn_a3KNAN, width=btn_window_width,
                               tags=["3KNA-N", "ME-4IU"])
aQ1UIU = canva_1.create_window(sistem_x + 360, sistem_y + 550, anchor=NW, window=btn_aQ1UIU, width=btn_window_width,
                               tags=["Q1U-IU", "CH9L-K","JSI-LL"])

aJSILL = canva_1.create_window(sistem_x + 360, sistem_y + 595, anchor=NW, window=btn_aJSILL, width=btn_window_width,
                               tags=["JSI-LL", "Q1U-IU", "M-UC0S", "U5-XW7"])
aSY0W2 = canva_1.create_window(sistem_x + 290, sistem_y + 630, anchor=NW, window=btn_aSY0W2, width=btn_window_width,
                               tags=["SY0W-2", "U5-XW7", "M-UC0S"])
aMUC05 = canva_1.create_window(sistem_x + 290, sistem_y + 595, anchor=NW, window=btn_aMUC05, width=btn_window_width,
                               tags=["M-UC0S", "JSI-LL", "SY0W-2"])
aV7MID = canva_1.create_window(sistem_x + 220, sistem_y + 630, anchor=NW, window=btn_aV7MID, width=btn_window_width,
                               tags=["V7-MID", "SY0W-2"])
aU5XW7 = canva_1.create_window(sistem_x + 360, sistem_y + 630, anchor=NW, window=btn_aU5XW7, width=btn_window_width,
                               tags=["U5-XW7", "SY0W-2", "JSI-LL", "MZPH-W" ])
aMZPHW = canva_1.create_window(sistem_x + 360, sistem_y + 670, anchor=NW, window=btn_aMZPHW, width=btn_window_width,
                               tags=["MZPH-W"])

aKJQWL = canva_1.create_window(sistem_x + 360, sistem_y + 390, anchor=NW, window=btn_aKJQWL, width=btn_window_width,
                               tags=["KJ-QWL", "9-B1DS", "SVB-RE","KMQ4-V"])
aKMQ4V = canva_1.create_window(sistem_x + 428, sistem_y + 390, anchor=NW, window=btn_aKMQ4V, width=btn_window_width,
                               tags=["KMQ4-V", "KJ-QWL", "5-P1Y2"])
aSVBRE = canva_1.create_window(sistem_x + 377, sistem_y + 355, anchor=NW, window=btn_aSVBRE, width=btn_window_width,
                               tags=["SVB-RE", "KJ-QWL"])

a5P1Y2 = canva_1.create_window(sistem_x + 497, sistem_y + 390, anchor=NW, window=btn_a5P1Y2, width=btn_window_width,
                               tags=["5-P1Y2", "KMQ4-V", "J52-BH"])
aJ52BH = canva_1.create_window(sistem_x + 565, sistem_y + 390, anchor=NW, window=btn_aJ52BH, width=btn_window_width,
                               tags=["J52-BH", "5-P1Y2","C-LBQS"])
aCLBQS = canva_1.create_window(sistem_x + 633, sistem_y + 390, anchor=NW, window=btn_aCLBQS, width=btn_window_width,
                               tags=["C-LBQS", "J52-BH", "BWI1-9"])
aBWI19 = canva_1.create_window(sistem_x + 700, sistem_y + 390, anchor=NW, window=btn_aBWI19, width=btn_window_width,
                               tags=["BWI1-9", "C-LBQS", "KL3O-J"])
aKL30J = canva_1.create_window(sistem_x + 769, sistem_y + 390, anchor=NW, window=btn_aKL30J, width=btn_window_width,
                               tags=["KL3O-J", "R4O-I6", "BWI1-9"])
aR40I6 = canva_1.create_window(sistem_x + 768, sistem_y + 355, anchor=NW, window=btn_aR40I6, width=btn_window_width,
                               tags=["R4O-I6", "KL3O-J", "Q-NJZ4", "3-TD6L"])

aQNJZ4 = canva_1.create_window(sistem_x + 835, sistem_y + 355, anchor=NW, window=btn_aQNJZ4, width=btn_window_width,
                               tags=["Q-NJZ4", "R4O-I6", "NLPB-0", "3-TD6L"])
aNLPB0 = canva_1.create_window(sistem_x + 835, sistem_y + 310, anchor=NW, window=btn_aNLPB0, width=btn_window_width,
                               tags=["NLPB-0", "Q-NJZ4", "3-TD6L"])
a3TD6L = canva_1.create_window(sistem_x + 768, sistem_y + 310, anchor=NW, window=btn_a3TD6L, width=btn_window_width,
                               tags=["3-TD6L", "NLPB-0", "R4O-I6", "Q-NJZ4", "CX-1XF"])
aCX1XF = canva_1.create_window(sistem_x + 680, sistem_y + 295, anchor=NW, window=btn_aCX1XF, width=btn_window_width,
                               tags=["CX-1XF", "3-TD6L", "X4UV-Z"])
aX4UVZ = canva_1.create_window(sistem_x + 530, sistem_y + 295, anchor=NW, window=btn_aX4UVZ, width=btn_window_width,
                               tags=["X4UV-Z", "CX-1XF", "BKG-Q2", "JRZ-B9"])
aJRZB9 = canva_1.create_window(sistem_x + 530, sistem_y + 260, anchor=NW, window=btn_aJRZB9, width=btn_window_width,
                               tags=["JRZ-B9", "X4UV-Z", "V8W-QS", "S-B7IT"])
aV8WQS = canva_1.create_window(sistem_x + 605, sistem_y + 260, anchor=NW, window=btn_aV8WQS, width=btn_window_width,
                               tags=["V8W-QS", "JRZ-B9", "XW-2XP", "CS-ZGD", "OJ-A8M"])
aXW2XP = canva_1.create_window(sistem_x + 575, sistem_y + 210, anchor=NW, window=btn_aXW2XP, width=btn_window_width,
                               tags=["XW-2XP", "V8W-QS", "C-HCGU"])

aCSZGD = canva_1.create_window(sistem_x + 680, sistem_y + 210, anchor=NW, window=btn_aCSZGD, width=btn_window_width,
                               tags=["CS-ZGD", "V8W-QS", "A-G1FM", "3-N3OO"])
a3N3OO = canva_1.create_window(sistem_x + 790, sistem_y + 210, anchor=NW, window=btn_a3N3OO, width=btn_window_width,
                               tags=["3-N3OO", "CS-ZGD", "4-BE0M", "ZIU-EP"])
aAG1FM = canva_1.create_window(sistem_x + 700, sistem_y + 133, anchor=NW, window=btn_aAG1FM, width=btn_window_width,
                               tags=["A-G1FM", "CS-ZGD", "ZIU-EP", "I-7RIS", "P7Z-R3", "4-BE0M"])

aZIUEP = canva_1.create_window(sistem_x + 742, sistem_y + 172, anchor=NW, window=btn_aZIUEP, width=btn_window_width,
                               tags=["ZIU-EP", "3-N3OO", "A-G1FM", "2-3Q2G"])
aP7ZR3 = canva_1.create_window(sistem_x + 735, sistem_y + 95, anchor=NW, window=btn_aP7ZR3, width=btn_window_width,
                               tags=["P7Z-R3", "4-BE0M", "A-G1FM"])
a4BE0M = canva_1.create_window(sistem_x + 810, sistem_y + 95, anchor=NW, window=btn_a4BE0M, width=btn_window_width,
                               tags=["4-BE0M", "P7Z-R3", "A-G1FM", "3-N3OO"])
aI7RIS = canva_1.create_window(sistem_x + 655, sistem_y + 95, anchor=NW, window=btn_aI7RIS, width=btn_window_width,
                               tags=["I-7RIS", "A-G1FM"])
a23Q2G = canva_1.create_window(sistem_x + 836, sistem_y + 140, anchor=NW, window=btn_a23Q2G, width=btn_window_width,
                               tags=["2-3Q2G", "ZIU-EP"])

a9IPCE = canva_1.create_window(sistem_x + 836, sistem_y - 15, anchor=NW, window=btn_a9IPCE, width=btn_window_width,
                               tags=["9IPC-E", "UQ9-3C"])

aKMCWI = canva_1.create_window(sistem_x + 825, sistem_y + 30, anchor=NW, window=btn_aKMCWI, width=btn_window_width,
                               tags=["KMC-WI", "VL3I-M"])
aVL3IM = canva_1.create_window(sistem_x + 750, sistem_y + 30, anchor=NW, window=btn_aVL3IM, width=btn_window_width,
                               tags=["VL3I-M", "KMC-WI", "UQ9-3C"])
aUQ93C = canva_1.create_window(sistem_x + 750, sistem_y - 15, anchor=NW, window=btn_aUQ93C, width=btn_window_width,
                               tags=["UQ9-3C", "VL3I-M", "9IPC-E", "DCI7-7"])

aDCI77 = canva_1.create_window(sistem_x + 670, sistem_y - 15, anchor=NW, window=btn_aDCI77, width=btn_window_width,
                               tags=["DCI7-7", "UQ9-3C", "J7YR-1"])
aJ7YR1 = canva_1.create_window(sistem_x + 600, sistem_y - 15, anchor=NW, window=btn_aJ7YR1, width=btn_window_width,
                               tags=["J7YR-1", "DCI7-7", "PKG4-7", "AH-B84"])
aPKG47 = canva_1.create_window(sistem_x + 600, sistem_y + 15, anchor=NW, window=btn_aPKG47, width=btn_window_width,
                               tags=["PKG4-7", "EWN-2U", "J7YR-1"])
aEWN2U = canva_1.create_window(sistem_x + 600, sistem_y + 45, anchor=NW, window=btn_aEWN2U, width=btn_window_width,
                               tags=["EWN-2U", "PKG4-7", "4-48K1"])

aAHB84 = canva_1.create_window(sistem_x + 505, sistem_y + 15, anchor=NW, window=btn_aAHB84, width=btn_window_width,
                               tags=["AH-B84", "DCI7-7", "HB7R-F", "JTAU-5"])

aHB7RF = canva_1.create_window(sistem_x + 505, sistem_y - 25, anchor=NW, window=btn_aHB7RF, width=btn_window_width,
                               tags=["HB7R-F", "AH-B84", "O-JPKH"])
aOJPKH = canva_1.create_window(sistem_x + 435, sistem_y - 25, anchor=NW, window=btn_aOJPKH, width=btn_window_width,
                               tags=["O-JPKH", "HB7R-F", "B-GC1T"])
aBGC1T = canva_1.create_window(sistem_x + 365, sistem_y - 25, anchor=NW, window=btn_aBGC1T, width=btn_window_width,
                               tags=["B-GC1T", "O-JPKH"])
aJTAU5 = canva_1.create_window(sistem_x + 435, sistem_y + 15, anchor=NW, window=btn_aJTAU5, width=btn_window_width,
                               tags=["JTAU-5", "AH-B84", "F-9F6Q"])
aF9F6Q = canva_1.create_window(sistem_x + 365, sistem_y + 15, anchor=NW, window=btn_aF9F6Q, width=btn_window_width,
                               tags=["F-9F6Q", "JTAU-5"])

# aXW2XP = canva_1.create_window(sistem_x+742, sistem_y+260, anchor=NW, window=btn_aXW2XP, width=btn_window_width, tags=["XW-2XP"])

aOJA8M = canva_1.create_window(sistem_x + 742, sistem_y + 260, anchor=NW, window=btn_aOJA8M, width=btn_window_width,
                               tags=["OJ-A8M", "V8W-QS", "H1-ESN"])
aH1ESN = canva_1.create_window(sistem_x + 836, sistem_y + 260, anchor=NW, window=btn_aH1ESN, width=btn_window_width,
                               tags=["H1-ESN", "OJ-A8M"])

aCHCGU = canva_1.create_window(sistem_x + 560, sistem_y + 169, anchor=NW, window=btn_aCHCGU, width=btn_window_width,
                               tags=["C-HCGU", "XW-2XP", "NTV0-1", "Q-FEEJ"])
aNTV01 = canva_1.create_window(sistem_x + 560, sistem_y + 139, anchor=NW, window=btn_aNTV01, width=btn_window_width,
                               tags=["NTV0-1", "C-HCGU", "4-48K1"])
a448K1 = canva_1.create_window(sistem_x + 560, sistem_y + 108, anchor=NW, window=btn_a448K1, width=btn_window_width,
                               tags=["4-48K1", "NTV0-1", "EWN-2U"])
aQFEEJ = canva_1.create_window(sistem_x + 475, sistem_y + 169, anchor=NW, window=btn_aQFEEJ, width=btn_window_width,
                               tags=["Q-FEEJ", "C-HCGU", "0P9Z-I"])
a0P9ZI = canva_1.create_window(sistem_x + 475, sistem_y + 139, anchor=NW, window=btn_a0P9ZI, width=btn_window_width,
                               tags=["0P9Z-I", "Q-FEEJ", "Z-K495"])

aSB7IT = canva_1.create_window(sistem_x + 455, sistem_y + 260, anchor=NW, window=btn_aSB7IT, width=btn_window_width,
                               tags=["S-B7IT", "BKG-Q2", "JRZ-B9"])
aBKGQ2 = canva_1.create_window(sistem_x + 455, sistem_y + 295, anchor=NW, window=btn_aBKGQ2, width=btn_window_width,
                               tags=["BKG-Q2", "S-B7IT", "Z-K495", "X4UV-Z", "8-4GQM", "LXWN-W"])
aZK495 = canva_1.create_window(sistem_x + 365, sistem_y + 139, anchor=NW, window=btn_aZK495, width=btn_window_width,
                               tags=["Z-K495", "BKG-Q2", "XM-4L0", "0P9Z-I"])

aYG82V = canva_1.create_window(sistem_x + 365, sistem_y + 100, anchor=NW, window=btn_aYG82V, width=btn_window_width,
                               tags=["YG-82V", "UB-UQZ"])

aUBUQZ = canva_1.create_window(sistem_x + 285, sistem_y + 100, anchor=NW, window=btn_aUBUQZ, width=btn_window_width,
                               tags=["UB-UQZ", "YG-82V", "XM-4L0", "B8O-KJ"])
aXM4L0 = canva_1.create_window(sistem_x + 285, sistem_y + 139, anchor=NW, window=btn_aXM4L0, width=btn_window_width,
                               tags=["XM-4L0", "Z-K495", "UB-UQZ", "B8O-KJ", "QCWA-Z"])
aQCWAZ = canva_1.create_window(sistem_x + 285, sistem_y + 179, anchor=NW, window=btn_aQCWAZ, width=btn_window_width,
                               tags=["QCWA-Z", "KV-8SM", "XM-4L0", "5LJ-MD", "52G-NZ"])
aKV8SM = canva_1.create_window(sistem_x + 285, sistem_y + 220, anchor=NW, window=btn_aKV8SM, width=btn_window_width,
                               tags=["KV-8SM", "QCWA-Z", "52G-NZ"])
a4DTQK = canva_1.create_window(sistem_x + 205, sistem_y + 70, anchor=NW, window=btn_a4DTQK, width=btn_window_width,
                               tags=["4DTQ-K", "B8O-KJ", "EQI2-2", "J9-5MQ"])
aB8OKJ = canva_1.create_window(sistem_x + 205, sistem_y + 139, anchor=NW, window=btn_aB8OKJ, width=btn_window_width,
                               tags=["B8O-KJ", "XM-4L0", "UB-UQZ", "4DTQ-K", "5LJ-MD"])
a5LJMD = canva_1.create_window(sistem_x + 205, sistem_y + 179, anchor=NW, window=btn_a5LJMD, width=btn_window_width,
                               tags=["5LJ-MD", "B8O-KJ", "QCWA-Z", "52G-NZ"])
a52GNZ = canva_1.create_window(sistem_x + 205, sistem_y + 220, anchor=NW, window=btn_a52GNZ, width=btn_window_width,
                               tags=["52G-NZ", "KV-8SM", "QCWA-Z","5LJ-MD", "6-O5GY"])

aEQI22 = canva_1.create_window(sistem_x + 270, sistem_y + 40, anchor=NW, window=btn_aEQI22, width=btn_window_width,
                               tags=["EQI2-2", "4DTQ-K", "D4R-H7"])
aD4RH7 = canva_1.create_window(sistem_x + 270, sistem_y + 10, anchor=NW, window=btn_aD4RH7, width=btn_window_width,
                               tags=["D4R-H7", "EQI2-2", "J9-5MQ"])
aJ95MQ = canva_1.create_window(sistem_x + 205, sistem_y + -20, anchor=NW, window=btn_aJ95MQ, width=btn_window_width,
                               tags=["J9-5MQ", "D4R-H7", "313I-B", "Q-4DEC"])
a313IB = canva_1.create_window(sistem_x + 128, sistem_y + -45, anchor=NW, window=btn_a313IB, width=btn_window_width,
                               tags=["313I-B", "J9-5MQ"])
aQ4DEC = canva_1.create_window(sistem_x + 128, sistem_y + 10, anchor=NW, window=btn_aQ4DEC, width=btn_window_width,
                               tags=["Q-4DEC", "J9-5MQ"])
a6O5GY = canva_1.create_window(sistem_x + 115, sistem_y + 220, anchor=NW, window=btn_a6O5GY, width=btn_window_width,
                               tags=["6-O5GY", "52G-NZ"])

aZXAV6 = canva_1.create_window(sistem_x + 360, sistem_y + 256, anchor=NW, window=btn_aZXAV6, width=btn_window_width,
                               tags=["ZXA-V6", "T-Q2DD"])

aTQ2DD = canva_1.create_window(sistem_x + 261, sistem_y + 265, anchor=NW, window=btn_aTQ2DD, width=btn_window_width,
                               tags=["T-Q2DD", "ZXA-V6",])
aLRWDB = canva_1.create_window(sistem_x + 261, sistem_y + 325, anchor=NW, window=btn_aLRWDB, width=btn_window_width,
                               tags=["LRWD-B", "QXQ-BA", "8-4GQM"])
aQXQBA = canva_1.create_window(sistem_x + 210, sistem_y + 295, anchor=NW, window=btn_aQXQBA, width=btn_window_width,
                               tags=["QXQ-BA", "T-Q2DD", "LRWD-B", "X7R-JW", "M-HU4V"])
aX7RJW = canva_1.create_window(sistem_x + 162, sistem_y + 265, anchor=NW, window=btn_aX7RJW, width=btn_window_width,
                               tags=["X7R-JW", "QXQ-BA", "M-HU4V"])
aMHU4V = canva_1.create_window(sistem_x + 162, sistem_y + 325, anchor=NW, window=btn_aMHU4V, width=btn_window_width,
                               tags=["M-HU4V", "X7R-JW", "QXQ-BA", "C-4ZOS"])

a84GQM = canva_1.create_window(sistem_x + 315, sistem_y + 295, anchor=NW, window=btn_a84GQM, width=btn_window_width,
                               tags=["8-4GQM", "BKG-Q2", "LRWD-B", "T-Q2DD"])
aLXWNW = canva_1.create_window(sistem_x + 260, sistem_y + 410, anchor=NW, window=btn_aLXWNW, width=btn_window_width,
                               tags=["LXWN-W", "BKG-Q2", "RO90-H", "C-LP3N"])



aO94UA = canva_1.create_window(sistem_x + 45, sistem_y + 280, anchor=NW, window=btn_aO94UA, width=btn_window_width,
                              tags=["O94U-A", "C-VGYO"])
aXWJHT = canva_1.create_window(sistem_x +- 30, sistem_y + 280, anchor=NW, window=btn_aXWJHT, width=btn_window_width,
                              tags=["XW-JHT", "C-VGYO"])
aCVGYO = canva_1.create_window(sistem_x +- 10, sistem_y + 320, anchor=NW, window=btn_aCVGYO, width=btn_window_width,
                              tags=["C-VGYO", "K-8SQS", "XW-JHT", "O94U-A"])
aK8SQS = canva_1.create_window(sistem_x +- 10, sistem_y + 359, anchor=NW, window=btn_aK8SQS, width=btn_window_width,
                              tags=["K-8SQS", "C-4ZOS", "C-VGYO"])
aNEHCS = canva_1.create_window(sistem_x + 70, sistem_y + 320, anchor=NW, window=btn_aNEHCS, width=btn_window_width,
                              tags=["NEH-CS", "C-4ZOS"])


aC4ZOS = canva_1.create_window(sistem_x + 63, sistem_y + 359, anchor=NW, window=btn_aC4ZOS, width=btn_window_width,
                              tags=["C-4ZOS", "M-HU4V", "K-8SQS", "3F-JZF", "NEH-CS"])


a3FJZF = canva_1.create_window(sistem_x + 32, sistem_y + 410, anchor=NW, window=btn_a3FJZF, width=btn_window_width,
                              tags=["3F-JZF", "C-4ZOS", "5-0WB9", "2B7A-3", "W-4FA9"])
a50WB9 = canva_1.create_window(sistem_x + 106, sistem_y + 410, anchor=NW, window=btn_a50WB9, width=btn_window_width,
                              tags=["5-0WB9", "3F-JZF"])
a2B7A3 = canva_1.create_window(sistem_x +- 40, sistem_y + 410, anchor=NW, window=btn_a2B7A3, width=btn_window_width,
                              tags=["2B7A-3", "3F-JZF"])
aW4FA9 = canva_1.create_window(sistem_x + 32, sistem_y + 450, anchor=NW, window=btn_aW4FA9, width=btn_window_width,
                              tags=["W-4FA9", "3F-JZF", "PUWL-4", "1IX-C0"])
aPUWL4 = canva_1.create_window(sistem_x + 100, sistem_y + 490, anchor=NW, window=btn_aPUWL4, width=btn_window_width,
                              tags=["PUWL-4", "W-4FA9"])
a1IXC0 = canva_1.create_window(sistem_x + 20, sistem_y + 490, anchor=NW, window=btn_a1IXC0, width=btn_window_width,
                              tags=["1IX-C0", "W-4FA9"])
aY1918 = canva_1.create_window(sistem_x + 20, sistem_y + 530, anchor=NW, window=btn_aY1918, width=btn_window_width,
                              tags=["Y-1918", "1IX-C0", "UJY-HE"])
aUJYHE = canva_1.create_window(sistem_x + 20, sistem_y + 580, anchor=NW, window=btn_aUJYHE, width=btn_window_width,
                              tags=["UJY-HE", "1IX-C0"])


aRO90H = canva_1.create_window(sistem_x + 260, sistem_y + 443, anchor=NW, window=btn_aRO90H, width=btn_window_width,
                               tags=["RO90-H", "LXWN-W", "MA-VDX", "WO-AIJ"])
aMAVDX = canva_1.create_window(sistem_x + 260, sistem_y + 475, anchor=NW, window=btn_aMAVDX, width=btn_window_width,
                               tags=["MA-VDX", "92D-OI", "RO90-H", "1G-MJE"])
a92DOI = canva_1.create_window(sistem_x + 260, sistem_y + 524, anchor=NW, window=btn_a92DOI, width=btn_window_width,
                               tags=["92D-OI", "MA-VDX"])
aWOAIJ = canva_1.create_window(sistem_x + 188, sistem_y + 443, anchor=NW, window=btn_aWOAIJ, width=btn_window_width,
                               tags=["WO-AIJ", "1G-MJE", "C-LP3N", "RO90-H"])
a1GMJE = canva_1.create_window(sistem_x + 188, sistem_y + 475, anchor=NW, window=btn_a1GMJE, width=btn_window_width,
                               tags=["1G-MJE", "MA-VDX", "WO-AIJ"])
aCLP3N = canva_1.create_window(sistem_x + 188, sistem_y + 410, anchor=NW, window=btn_aCLP3N, width=btn_window_width,
                               tags=["C-LP3N", "WO-AIJ", "9F-7PZ", "LXWN-W",])
a9F7PZ = canva_1.create_window(sistem_x + 188, sistem_y + 379, anchor=NW, window=btn_a9F7PZ, width=btn_window_width,
                               tags=["9F-7PZ", "C-LP3N"])


aZKYQ3 = canva_1.create_window(sistem_x + 360, sistem_y + 720, anchor=NW, window=btn_aZKYQ3, width=btn_window_width,
                               tags=["ZK-YQ3", "MZPH-W"])



aTEST = canva_1.create_window(sistem_x + 731, sistem_y + 624, anchor=NW, window=btn_aTEST, width=btn_window_width,
                              tags=["TEST"])
aTuKTuK = canva_1.create_window(sistem_x + 800, sistem_y + 624, anchor=NW, window=btn_aTuKTuK, width=btn_window_width,
                                tags=["TuK-TuK"])

ess_msg_1 = canva_1.create_rectangle(628, 555, 940, 656, width=2, outline="red", dash=(4, 4,))
ess_msg_2 = canva_1.create_text(sistem_x + 615, sistem_y + 522, font=('Entry', '14', 'bold'), text="ESS", fill="blue")
ess_msg_3 = canva_1.create_text(sistem_x + 728, sistem_y + 552, font=('Entry', '25', 'bold'),  fill="blue")

canva_1.delete(ess_msg_1, ess_msg_2, ess_msg_3)
# =============================================================================
#
# =============================================================================

# full_canvas_1(-100,50)

# canva_1.create_line(10, 10, 20, 20)


find_all_canvas = canva_1.find_all()

for elements in find_all_canvas:
    # print(elements)
    guard_list_system_sound.append((canva_1.itemcget(elements, "tags")))

for elements in find_all_canvas:
    # print(elements)
    list_system.append((canva_1.itemcget(elements, "tags"))[0:6])

stroka_1=(canva_1.itemcget(1, "tags"))[0:6]
stroka_2=(canva_1.itemcget(1, "tags")).split()

print(canva_1.itemcget(1, "tags"))
print(stroka_1)
print(stroka_2)
print(len(stroka_2))  # длина списка
print(stroka_2[0])  # первый элемент списка начинается с 0.  конечный типа "лен-1"

# coord_CH = []
# coord_CH = canva_1.coords(aSVBRE)
# print(coord_CH)

# coord_CH = canva_1.coords(aMZPHW)
# print(coord_CH)

# canva_1.bind("<Button-1>", print_coords)




# full_canvas_2(-100,50)










# ГЕЙТЫ ЛИНИИ

# canva_1.create_line(393, 66, 499, 68, fill="black", stipple='warning', splinesteps=1, width=2)



color_gate_line = "burlywood4"

my_wwidth_01 = 1.4

kl30j_r40i6 = canva_1.create_line(sistem_x + 800, sistem_y + 365, sistem_x + 800, sistem_y + 390, fill="burlywood4",
                                  splinesteps=10, width=my_wwidth_01)
bwi9_kl30j = canva_1.create_line(sistem_x + 765, sistem_y + 402, sistem_x + 800, sistem_y + 402, fill="burlywood4",
                                 splinesteps=10, width=my_wwidth_01)

bkgq2_cx1xf = canva_1.create_line(sistem_x + 520, sistem_y + 307, sistem_x + 699, sistem_y + 307, fill="burlywood4", splinesteps=10,
                    width=my_wwidth_01)

jrzb9_x4uvz = canva_1.create_line(sistem_x + 560, sistem_y + 285, sistem_x + 560, sistem_y + 294, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)

sb7it_v8wqs = canva_1.create_line(sistem_x + 520, sistem_y + 272, sistem_x + 605, sistem_y + 272, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)
sb7it_bkgq2 = canva_1.create_line(sistem_x + 486, sistem_y + 295, sistem_x + 486, sistem_y + 285, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)

zk_bkg = canva_1.create_line(sistem_x + 396, sistem_y + 160, sistem_x + 455, sistem_y + 306, fill="burlywood4",
                             splinesteps=5, width=my_wwidth_01)
a84qm_bkg = canva_1.create_line(sistem_x + 380, sistem_y + 307, sistem_x + 455, sistem_y + 307, fill="burlywood4",
                                splinesteps=5, width=my_wwidth_01)

lxwnw_bkgq2 = canva_1.create_line(sistem_x + 290, sistem_y + 384, sistem_x + 455, sistem_y + 309, fill="burlywood4",
                                  splinesteps=5, width=my_wwidth_01)
lxwnw_92doi = canva_1.create_line(sistem_x + 290, sistem_y + 384, sistem_x + 290, sistem_y + 527, fill="burlywood4",
                                  splinesteps=5, width=my_wwidth_01)

mzphw_svbre = canva_1.create_line(sistem_x + 390, sistem_y + 670, sistem_x + 390, sistem_y + 380, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)

v7mid_u5xw7 = canva_1.create_line(sistem_x + 285, sistem_y + 642, sistem_x + 365, sistem_y + 642, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)
muc05_jsill = canva_1.create_line(sistem_x + 356, sistem_y + 607, sistem_x + 365, sistem_y + 607, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)
muc05_syow2 = canva_1.create_line(sistem_x + 322, sistem_y + 620, sistem_x + 322, sistem_y + 629, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)

ch9lk_qyzmw = canva_1.create_line(sistem_x + 425, sistem_y + 512, sistem_x + 500, sistem_y + 512, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)
buiu4_qyzmw = canva_1.create_line(sistem_x + 530, sistem_y + 490, sistem_x + 530, sistem_y + 512, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)
a9b1ds_buiu4 = canva_1.create_line(sistem_x + 425, sistem_y + 482, sistem_x + 500, sistem_y + 482, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)
i7jr4_3knan = canva_1.create_line(sistem_x + 461, sistem_y + 456, sistem_x + 461, sistem_y + 500, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)

kjqwl_clbqs = canva_1.create_line(sistem_x + 425, sistem_y + 403, sistem_x + 700, sistem_y + 403, fill="burlywood4", splinesteps=0,
                    width=my_wwidth_01)

a3td6l_r40 = canva_1.create_line(sistem_x + 800, sistem_y + 330, sistem_x + 800, sistem_y + 356, fill="burlywood4",
                                 splinesteps=0, width=my_wwidth_01)
a3td6l_qn = canva_1.create_line(sistem_x + 800, sistem_y + 330, sistem_x + 860, sistem_y + 356, fill="burlywood4",
                                splinesteps=0, width=my_wwidth_01)
nlpb_qn = canva_1.create_line(sistem_x + 867, sistem_y + 330, sistem_x + 867, sistem_y + 356, fill="burlywood4",
                              splinesteps=0, width=my_wwidth_01)

v8wqs_oja8m = canva_1.create_line(sistem_x + 667, sistem_y + 272, sistem_x + 743, sistem_y + 272, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
oja8m_h1esn = canva_1.create_line(sistem_x + 800, sistem_y + 272, sistem_x + 841, sistem_y + 272, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
# canva_1.create_line(563, 120, 670, 120, fill="burlywood4", splinesteps=0, width=my_wwidth_01)

cx1xf_3t = canva_1.create_line(sistem_x + 744, sistem_y + 307, sistem_x + 766, sistem_y + 322, fill="burlywood4",
                               splinesteps=0, width=my_wwidth_01)

v8wqs_xw2xp = canva_1.create_line(sistem_x + 610, sistem_y + 236, sistem_x + 626, sistem_y + 260, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
v8wqs_cszgd = canva_1.create_line(sistem_x + 705, sistem_y + 236, sistem_x + 645, sistem_y + 260, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
cszgd_3n3oo = canva_1.create_line(sistem_x + 745, sistem_y + 221, sistem_x + 790, sistem_y + 221, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)

cszgd_ag1fm = canva_1.create_line(sistem_x + 720, sistem_y + 153, sistem_x + 720, sistem_y + 208, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
ag1fm_i7ris = canva_1.create_line(sistem_x + 693, sistem_y + 118, sistem_x + 720, sistem_y + 137, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
ag1fm_ziueo = canva_1.create_line(sistem_x + 739, sistem_y + 155, sistem_x + 762, sistem_y + 170, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
ag1fm_p7zr3 = canva_1.create_line(sistem_x + 740, sistem_y + 137, sistem_x + 755, sistem_y + 118, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
ag1fm_4be0m = canva_1.create_line(sistem_x + 764, sistem_y + 143, sistem_x + 816, sistem_y + 121, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)

ziueo_23q2g = canva_1.create_line(sistem_x + 785, sistem_y + 170, sistem_x + 837, sistem_y + 152, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)

p7zr3_4be0m = canva_1.create_line(sistem_x + 800, sistem_y + 106, sistem_x + 812, sistem_y + 106, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
a4be0m_3n3oo = canva_1.create_line(sistem_x + 824, sistem_y + 120, sistem_x + 824, sistem_y + 212, fill="burlywood4",
                                   splinesteps=0, width=my_wwidth_01)
a3n3oo_ziuep = canva_1.create_line(sistem_x + 785, sistem_y + 197, sistem_x + 800, sistem_y + 212, fill="burlywood4",
                                   splinesteps=0, width=my_wwidth_01)
# canva_1.create_arc(366, 182, 600, 305,   start=160, extent=170,  style=ARC, outline='darkblue', fill='orange',  width=2)

xw2xp_448k1 = canva_1.create_line(sistem_x + 595, sistem_y + 123, sistem_x + 595, sistem_y + 215, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
chcgu_qfeej = canva_1.create_line(sistem_x + 540, sistem_y + 180, sistem_x + 562, sistem_y + 180, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
chcgu_op9zi = canva_1.create_line(sistem_x + 507, sistem_y + 164, sistem_x + 507, sistem_y + 175, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
op9zi_zk495 = canva_1.create_line(sistem_x + 430, sistem_y + 151, sistem_x + 472, sistem_y + 151, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
ewn2u_448k1 = canva_1.create_line(sistem_x + 630, sistem_y + 70, sistem_x + 595, sistem_y + 115, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
ewn2u_j7yr1 = canva_1.create_line(sistem_x + 630, sistem_y + -4, sistem_x + 630, sistem_y + 60, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
j7yr1_9ipce = canva_1.create_line(sistem_x + 661, sistem_y + -2, sistem_x + 841, sistem_y + -2, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
ahb84_j7yr1 = canva_1.create_line(sistem_x + 570, sistem_y + 26, sistem_x + 604, sistem_y + -4, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
ahb84_hb7rf = canva_1.create_line(sistem_x + 537, sistem_y + 0, sistem_x + 537, sistem_y + 15, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
f9f6q_ahb84 = canva_1.create_line(sistem_x + 418, sistem_y + 27, sistem_x + 509, sistem_y + 27, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
bgc1t_hb7rf = canva_1.create_line(sistem_x + 420, sistem_y + -12, sistem_x + 507, sistem_y + -12, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)

uq93c_vl3im = canva_1.create_line(sistem_x + 782, sistem_y + 10, sistem_x + 782, sistem_y + 33, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
vl3im_kmcwi = canva_1.create_line(sistem_x + 815, sistem_y + 43, sistem_x + 825, sistem_y + 43, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)

xm4l0_zk495 = canva_1.create_line(sistem_x + 350, sistem_y + 152, sistem_x + 365, sistem_y + 152, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)

ubuqz_kv8sm = canva_1.create_line(sistem_x + 317, sistem_y + 116, sistem_x + 317, sistem_y + 238, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
a52gnz_kv8sm = canva_1.create_line(sistem_x + 265, sistem_y + 232, sistem_x + 294, sistem_y + 232, fill="burlywood4",
                                   splinesteps=0, width=my_wwidth_01)
a52gnz_qcwaz = canva_1.create_line(sistem_x + 252, sistem_y + 219, sistem_x + 300, sistem_y + 205, fill="burlywood4",
                                   splinesteps=0, width=my_wwidth_01)
a5ljmd_qcwaz = canva_1.create_line(sistem_x + 252, sistem_y + 191, sistem_x + 290, sistem_y + 191, fill="burlywood4",
                                   splinesteps=0, width=my_wwidth_01)
j95mq_52gnz = canva_1.create_line(sistem_x + 237, sistem_y + 5, sistem_x + 237, sistem_y + 238, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
a6o5gy_52gnz = canva_1.create_line(sistem_x + 180, sistem_y + 231, sistem_x + 205, sistem_y + 231, fill="burlywood4",
                                   splinesteps=0, width=my_wwidth_01)

ubuqz_yg82v = canva_1.create_line(sistem_x + 343, sistem_y + 113, sistem_x + 368, sistem_y + 113, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)

b80kj_ubuqz = canva_1.create_line(sistem_x + 252, sistem_y + 137, sistem_x + 290, sistem_y + 112, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
b80kj_xm4l0 = canva_1.create_line(sistem_x + 264, sistem_y + 150, sistem_x + 290, sistem_y + 150, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)

####################
tq2dd_zxav6 = canva_1.create_line(sistem_x + 325, sistem_y + 275, sistem_x + 365, sistem_y + 267, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
tq2dd_84gqm = canva_1.create_line(sistem_x + 300, sistem_y + 291, sistem_x + 315, sistem_y + 305, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
qxqba_tq2dd = canva_1.create_line(sistem_x + 275, sistem_y + 305, sistem_x + 290, sistem_y + 291, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
qxqba_lrwdb = canva_1.create_line(sistem_x + 275, sistem_y + 309, sistem_x + 290, sistem_y + 324, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
lrwdb_84gqm = canva_1.create_line(sistem_x + 300, sistem_y + 324, sistem_x + 315, sistem_y + 310, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)




a4dtqk_eqi22 = canva_1.create_line(sistem_x + 271, sistem_y + 82, sistem_x + 300, sistem_y + 66, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
eqi22_d4rh7 = canva_1.create_line(sistem_x + 300, sistem_y + 44, sistem_x + 300, sistem_y + 28, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
d4rh7_j95mq = canva_1.create_line(sistem_x + 300, sistem_y + 13, sistem_x + 270, sistem_y + -9, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
j95mq_313ib = canva_1.create_line(sistem_x + 207, sistem_y + -9, sistem_x + 186, sistem_y + -43, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
j95mq_q4idec = canva_1.create_line(sistem_x + 207, sistem_y + -6, sistem_x + 186, sistem_y + 33, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)


qxqba_x7rjw = canva_1.create_line(sistem_x + 240, sistem_y + 292, sistem_x + 225, sistem_y + 277, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
qxqba_mhu4v = canva_1.create_line(sistem_x + 240, sistem_y + 321, sistem_x + 225, sistem_y + 338, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
x7rjw_mhu4v = canva_1.create_line(sistem_x + 192, sistem_y + 290, sistem_x + 192, sistem_y + 325, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
mhu4v_c4zos = canva_1.create_line(sistem_x + 189, sistem_y + 350, sistem_x + 125, sistem_y + 373, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)


c4zos_NEHCS = canva_1.create_line(sistem_x + 96, sistem_y + 357, sistem_x + 96, sistem_y + 340, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
k8sqs_c4zos = canva_1.create_line(sistem_x + 25, sistem_y + 373, sistem_x + 95, sistem_y + 373, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
k8sqs_xwjht = canva_1.create_line(sistem_x + 23, sistem_y + 373, sistem_x + 23, sistem_y + 295, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
cvgyo_o94ua = canva_1.create_line(sistem_x + 30, sistem_y + 328, sistem_x + 70, sistem_y + 294, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
c4zos_3fjzf = canva_1.create_line(sistem_x + 95, sistem_y + 374, sistem_x + 62, sistem_y + 423, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
a2b7a3_50wb9 = canva_1.create_line(sistem_x + 13, sistem_y + 422, sistem_x + 120, sistem_y + 422, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
a3fjzf_w4fa9 = canva_1.create_line(sistem_x + 62, sistem_y + 430, sistem_x + 62, sistem_y + 459, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
w4fa9_1ixc0 = canva_1.create_line(sistem_x + 60, sistem_y + 460, sistem_x + 58, sistem_y + 500, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
w4fa9_puwl4 = canva_1.create_line(sistem_x + 65, sistem_y + 467, sistem_x + 120, sistem_y + 500, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
a1ixc0_ujyhe = canva_1.create_line(sistem_x + 53, sistem_y + 504, sistem_x + 53, sistem_y + 590, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)



a1gmje_9f7pz = canva_1.create_line(sistem_x + 221, sistem_y + 481, sistem_x + 221, sistem_y + 400, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
g_1gmje_9f7pz = canva_1.create_line(sistem_x + 221, sistem_y + 481, sistem_x + 221, sistem_y + 400, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
g_1gmje_9f7pz = canva_1.create_line(sistem_x + 245, sistem_y + 486, sistem_x + 269, sistem_y + 486, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
g_woaij_ro90h = canva_1.create_line(sistem_x + 245, sistem_y + 455, sistem_x + 269, sistem_y + 455, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)
g_clp3n_lxwnw = canva_1.create_line(sistem_x + 245, sistem_y + 422, sistem_x + 269, sistem_y + 422, fill="burlywood4",
                                  splinesteps=0, width=my_wwidth_01)

# canva_1.create_oval(363, 182, 600, 305,               fill='lightgrey',              outline='white')

# canva_1.create_rectangle(363, 182, 598, 305 )


# БРИДЖИ
color_bridge_line = "green"
color_bridge_line_active = "red"
# bu -- kl
canva_1.create_line(sistem_x + 566, sistem_y + 484, sistem_x + 800, sistem_y + 484, activefill="red", fill="green", dash=5)
canva_1.create_line(sistem_x + 800, sistem_y + 415, sistem_x + 800, sistem_y + 484, activefill="red", fill="green", dash=5)

# me -- 5p
canva_1.create_line(sistem_x + 529, sistem_y + 415, sistem_x + 529, sistem_y + 440, activefill="red", fill="green", dash=1)
canva_1.create_line(sistem_x + 529, sistem_y + 440, sistem_x + 492, sistem_y + 472, activefill="red", fill="green", dash=1)

# j52 -- JRZ
canva_1.create_line(sistem_x + 631, sistem_y + 334, sistem_x + 596, sistem_y + 390, activefill="red", fill="green", dash=1)
canva_1.create_line(sistem_x + 596, sistem_y + 285, sistem_x + 631, sistem_y + 334, activefill="red", fill="green", dash=1)





# ТЕКСТ
canva_1.create_text(sistem_x + 705, sistem_y + 474, text="bridje", activefill="red", fill="#004D40")
canva_1.create_text(sistem_x + 463, sistem_y + 562, text="region gate", activefill="red", fill="grey50")








# image_on_alarm = Image.open("alarm_on.png")
# image_off_alarm = Image.open("alarm_off.png")

# resized_image = image2.resize((24, 24))
#
# resized_image_on = image_on_alarm.reduce(3)
# resized_image_off = image_on_alarm.reduce(3)

# alarm_on_off = ImageTk.PhotoImage(resized_image_on)
#
#
# alarm_off_ = ImageTk.PhotoImage(resized_image_on)


# image_alarm_on = PhotoImage(file="alarm_on.png" , width=1, height=1)
# image_alarm_on = PhotoImage(file="alarm_on.png", width=0, height=0 )

# image_alarm_on.subsample(0, 0)
# image_alarm_off = PhotoImage(file="alarm_off.png")

# alarm_on = canva_1.create_image(668, 4, anchor=NW, image=image_alarm_on)
# alarm_on.scale(0, 0, 1.1, 1.1)


# btn_alarm = Button( command =  alarm_on_off_btn_1_click)
#
#
# image_alarm_on = PhotoImage(file=my_path_alarm_on_png)
# image_alarm_on = image_alarm_on.zoom(-2) #with 250, I ended up running out of memory
#
btn_alarm = Button(command=alarm_on_off_btn_1_click)
#
# imgpath = '/path/to/img.png'
# img = PhotoImage(file=imgpath)
# img = img.zoom(25) #with 250, I ended up running out of memory
# img = img.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
# panel = Label(root, image = img)
#
#
# btn_alarm.grid()
# btn_alarm.place(relx=0.5, rely=0.8)


id_canva_alarm_on_off = canva_1.create_image(773, 4, anchor=NW, tags=["img_alarm_on_off"])

set_image(my_image_on)

# id_canva_alarm_on_off_btn = canva_1.create_window(669, 6, anchor=NW, window=btn_alarm, width=29, height=29, tags=["btn_alarm_on_off"])


canva_1.bind("<Button-1>", print_coords)
canva_1.tag_bind(id_canva_alarm_on_off, "<Button-1>", alarm_on_off_btn_1_click)

# canva_1.bind_class("Button", "<ButtonPress-1>", clicked_BTN)
#
# root.bind_class("Button", "<ButtonPress-1>", clicked_BTN)
# canva_1.tag_bind( "<Button-1>", clicked_BTN)
#
# canva_1.bind("<Button-1>", clicked_BTN)
#
# # widget.bind_class("Button", "<Button-1>", clicked_BTN)
# root.bind_class("Button", "<Button-1>", clicked_BTN)
# canva_1.bind_class("Button", "<Button-1>", clicked_BTN)
#
# # canva_1.bind_all("Button", "<Button-1>", clicked_BTN)
#
# canva_1.bind_all("<Button-1>", clicked_BTN)
#
# canva_1.bind("Button", clicked_BTN)

# canva_1.bind("window", "<Button-1>", clicked_BTN)

root.bind("<Button-1>", clicked_BTN)
root.bind("<Button-3>", pop_up_context_menu_BTN_3)


#   canva_1.itemcget(elements, "tags"):
# #                  # print(elements)
#   btn_id = canva_1.itemcget(elements, "window")
#   btn_alarm = root.nametowidget(btn_id)


# id_canva_alarm_on_off = canva_1.create_image(673, 16, anchor=NW, image=alarm_on_off, tags=["img_alarm_on_off"] )

# привязка событий к элементу с идентификатором id
# canva_1.tag_bind(id_canva_alarm_on_off, "<Button-1>", alarm_on_off_btn_1_click)

# CAR_1 = 0
# photo_list = [tk.PhotoImage(file="car1.png")]
# btn_xxxx = Button(text = "", image = photo_list[0], width=100, height=100,)
# btn_xxxx.place(x = 0, y = 0)


# canva_1.create_oval(10, 10, 100, 50, fill="#80CBC4", outline="#004D40")
# qyzm = canva_1.create_rectangle(10, 10, 200, 50)
# btn = Button(canva, text="ффффффф")
# btn.pack()


# frame_1.pack()

# pw.add(frame_1)


# bt2 = ttk.Button(frame_1, text="Добавить", command=lambda:add("Добавить"))

# bt2 = ttk.Button(canva_1, text="Добавить", command=add)
# bt2 = ttk.Button(frame_1, text="Добавить", command=add)

# bt2.pack(expand=1)

frame_2 = Frame(pw, borderwidth=2, relief=RAISED)

label_2 = Label(frame_2, text='     INTEL')


# string = ( datetime.now() +  timedelta( hours=-3 )).strftime('%H:%M:%S') + "                      INTEL"
# label_2.config(text=string)

# функция отображения времени


def time():
    # string = ( datetime.now() +  timedelta( hours=-3 )).strftime('%H:%M:%S %p') + "                      INTEL"
    string = (datetime.now() + timedelta(hours=-3)
              ).strftime('%H:%M:%S') + "              INTEL"
    label_2.config(text=string)
    label_2.after(1000, time)


label_2.pack()

# my_text = ScrolledText (frame_2, wrap="word", bg="grey87")
my_text = Text(frame_2, wrap="word", bg="grey87")
# my_text.config()

# scroll = Scrollbar(command = my_tex.yview)

# scroll.pack(side=LEFT, fill=Y)


# frame_2.pack(fill=X)
frame_2.pack(fill="both", expand=1)

pw.add(frame_2)

pw.pack(fill="both", expand=1)

main_frame.pack(expand=1, fill=BOTH)


# добавление нового элемента
# def add(text):

#     print("**** def add(text) *****")

#     my_text.insert(END, "111"+"\n" + text)


# def proverka_num():

#     print("**** proverka_num() *****")

#     global gl_num_posl_stroki_save

#     if (gl_num_posl_stroki_live_reed == gl_num_posl_stroki_save):
#         print("НЕТ Новой строки")

#         # proverka_num()

#     else:
#         print("ECТЬ Новая строка")

#         gl_num_posl_stroki_save = string_1.kol_strok()

#         # add_line(last_line_text)
















def add_line():
    print("                                  ")
    print("                                  ")
    print("                                  ")
    print("                                  ")
    print("****  test_6  ->  add_line()   *****  ")
    print("                                    ")
    print("                                  ")
    print("                                  ")
    print("                                  ")
    string_1.go()
    global last_line_text
    last_line_text = string_1.last_line()
    path_live = string_1.max_path_live()
    gl_num_posl_stroki_live_reed = string_1.kol_strok()

    global gl_num_posl_stroki_save

    local_time = (datetime.now() + timedelta(hours=-3)).strftime('%H:%M:%S')
    print("**** add_line() *****  " + local_time)
    print("last_line_text= " + last_line_text)
    # print("path_live= " + path_live )
    print("test_6 -> def add_line(): -> num_posl_stroki_save= " + str(gl_num_posl_stroki_save))
    print("test_6 -> def add_line(): -> num_posl_stroki_live_reed= " + str(gl_num_posl_stroki_live_reed))
    print("РАЗНИЦА =  " + (str(gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save)))

    if (gl_num_posl_stroki_live_reed == gl_num_posl_stroki_save):
        print("НЕТ Новой строки ")

        # proverka_num()
        # searh_alarm_timers_systems()
        obrabotka_timers_slovar()

    # ЭТО НЕ РАБОТАЕТ И НЕ ДОЛЖНО ВРОДЕ СУДАЯ ПО ЛОГИКЕ ))))
    # elif ( gl_num_posl_stroki_save - gl_num_posl_stroki_live_reed ) > 1 :
    #     print("НЕТ Новой строки2 Разница =  " + (str(gl_num_posl_stroki_save - gl_num_posl_stroki_live_reed)))
    #     print("НЕТ Новой строки2 ")
    #     print("НЕТ Новой строки2 ")

    # elif ( gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save ) > 2 :
    #     print("НЕТ Новой строки2 Разница =  " + (str(gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save)))
    #     print("НЕТ Новой строки2 ")
    #     print("НЕТ Новой строки2 ")
    #     print("______________________________ +++    А Л Ё    +++___________________________________________ ")

    #     proverka_na_sovpadenia()

    # задаём диапазон строк которые хотим считатть из интела начианя с конца
    elif (gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save) > 1 and (
            gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save) < 10:
        print("НЕТ Новой строки2 Разница =  " + (str(gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save)))
        print("НЕТ Новой строки2 ")
        print("НЕТ Новой строки2 ")
        print("______________________________ +++    А Л Ё    +++___________________________________________ ")
        print("______________________________ +++    А Л Ё    +++___________________________________________ ")
        print("______________________________ +++    А Л Ё    +++___________________________________________ ")

        # 186 - 184 = 2

        raznica = gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save  # 5

        last_line_text = string_1.shouse_line_intel_stroka(gl_num_posl_stroki_live_reed - (raznica))

        # Добовляем новую строку
        # my_text.insert(END, "\n" + last_line_text)  # РАБОЧИЙ ВАРИАНТ

      #  my_text.insert(CURRENT, "\n" + last_line_text)
        my_text.insert('0.0', "\n" + last_line_text)

        # new = gl_num_posl_stroki_live_reed - (raznica+1)

        # 186-2 + 1
        gl_num_posl_stroki_save = (gl_num_posl_stroki_live_reed - raznica) + 1

        proverka_na_sovpadenia()

    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   ECТЬ Новая строка  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        # podsvedka_sistem()
        proverka_na_sovpadenia()

        # ТУТ НАДО ДЕЛАТЬ ПРОВЕРКУ НА КОЛИЧЕСТВО НОВЫХ СТРОК

        # Добовляем новую строку
        # my_text.insert(END, "\n" + last_line_text)  # РАБОЧИЙ ВАРИАНТ END - вставка в низ списка
       # my_text.insert(CURRENT, "\n" + last_line_text)  # РАБОЧИЙ ВАРИАНТ CURRENT - вставка в верх списка,а точнее по курсору~примерно
       # my_text.mark_set("insert", "%d.%d" % (1, 1))


        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        # ОПределяем кол строк в виджете my_text  ОЧИЧСТКА ИНТЕЛА (my_text) от нагромождения записей
        kol_strok_v_my_text = int(my_text.index('end').split('.')[0]) - 1

        print("КОЛ СТРОК В ИНТЕЛЕ = " + str(kol_strok_v_my_text))  # returns line count

        if kol_strok_v_my_text > 30:
            my_text.delete(1.0, END)
            print("ОЧИСТКА ИНТЕЛА ЗАВЕРШЕНА")

        my_text.insert('0.0', "\n" + last_line_text)

        gl_num_posl_stroki_save = string_1.kol_strok()

    my_text.after(5000, add_line)


# my_text.pack(fill=BOTH, expand=1)
# my_text.config(yscrollcommand=scroll.set)

my_text.pack(fill=BOTH, side=LEFT, expand=True)


# ПОПЫТКА СРОЛЛБАРА ДЛЯ ТЕКСТА В ИНТЕЛЕ


# my_text.config(yscrollcommand=scroll.set)

# ПОПЫТКА СРОЛЛБАРА ДЛЯ ТЕКСТА В ИНТЕЛЕ
# ys = Scrollbar(my_text, orient = "vertical", command = my_text.yview)
# ys.pack()
# my_text["yscrollcommand"] = ys.set


# def searh_alarm_timers_systems():
#      print("searh_alarm_timers_systems()")

#      # find_system_alarm.searh_alarm_timers(list_system)
#      rezult = ""
#      for odna_system in list_system:

#         # print("ПРОВЕРЯЕМАЯ СИСТЕМА = " + system)
#         rezult = find_system_alarm.searh_alarm_timers(odna_system)

#      if rezult == "ok":

#           poluchaem_slovar_alarm()


# def poluchaem_slovar_alarm():

#     timers_slovar  =  find_system_alarm.peredaem_alarm_slovar()

#     print("def poluchaem_slovar_alarm():  " + (str(timers_slovar)))

#     obrabotka_timers_slovar()


def obrabotka_timers_slovar():
    print(" ---------  def obrabotka_timers_slovar(): ")

    timers_slovar = find_system_alarm.peredaem_alarm_slovar()

    for system_tag in timers_slovar:

        print(f"Sytem: {system_tag}  Timer {timers_slovar[system_tag]} ")

        tekuhee_datatime = ((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M'))
        i = find_system_alarm.sravnivaem_datatime(tekuhee_datatime, system_tag)

        print("  i =  " + (str(i)) + ", Sytem: " + system_tag)

        if i == 4:

            # поиск элемента по тэгу
            for elements in find_all_canvas:
                #               # print(elements)

                if system_tag == canva_1.itemcget(elements, "tags")[0:6]:
                    #                      # print(elements)
                    btn_id = canva_1.itemcget(elements, "window")
                    bt_alarm = root.nametowidget(btn_id)
                    bt_alarm.config(background="SystemButtonFace")

            break  # прерываем весь цикл из за удаления элемента из timers_slovar

        # # поиск элемента по тэгу
        for elements in find_all_canvas:
            #               # print(elements)

            if system_tag == canva_1.itemcget(elements, "tags")[0:6]:
                #                  # print(elements)
                btn_id = canva_1.itemcget(elements, "window")
                bt_alarm = root.nametowidget(btn_id)
                # btn_alarm.config(background="red")
                if i == 0:
                    bt_alarm.config(background="red")
                elif i == 1:
                    bt_alarm.config(background="orange")
                elif i == 2:
                    bt_alarm.config(background="yellow")
                elif i == 3:
                    bt_alarm.config(background="antique white")
                elif i == 4:
                    if str(bt_alarm['text']) in guard_sound_one.get_guard_set_system_sound_one():
                        btn_sound_on(bt_alarm)
                    else:
                        bt_alarm.config(background="SystemButtonFace")

    print("ИТОГОВЫЙ СЛОВАРЬ:" + (str(timers_slovar)))

    # btn_id = canva_1.itemcget(system_tag, "window")
    # btn_alarm = root.nametowidget(btn_id)
    # if i == 4: btn_alarm.config(background="SystemButtonFace")
    if len(timers_slovar) == 0 and len(timers_slovar_green) != 0:
        schetchi_pustih_slovarey()

    obrabotka__ess__timers_slovar()


def obrabotka__ess__timers_slovar():
    print("  ---------  def obrabotka__ess__timers_slovar():   -----------")
    ess_timers_slovar = find_system_alarm.peredaem_ess_alarm_slovar()
    print("есс количество записей = " + str(len(ess_timers_slovar)))
    # global ess_time
    # ess_time = 5

    for system_tag in ess_timers_slovar:

        print(f"Sytem: {system_tag}  Timer {ess_timers_slovar[system_tag]} ")

        tekuhee_datatime = ((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M'))
        i = find_system_alarm.ess_sravnivaem_datatime(tekuhee_datatime, system_tag)[1]
        # ess_time = ess_time - i

        print("ess  i =  " + (str(i)) + ", Sytem: " + system_tag)

        if i == 5:
            ess_manager(system_tag, i)
            break

            # поиск элемента по тэгу
            # for elements in find_all_canvas:
            #     #               # print(elements)
            #     ess_manager(system_tag, i)
            #     break

            #     if system_tag == canva_1.itemcget(elements, "tags")[0:6]:
            #         #                      # print(elements)
            #         btn_id = canva_1.itemcget(elements, "window")
            #         bt_alarm = root.nametowidget(btn_id)
            #         bt_alarm.config(background="SystemButtonFace")
            #
            # break  # прерываем весь цикл из за удаления элемента из ess_timers_slovar

        # # поиск элемента по тэгу
        for elements in find_all_canvas:
            #               # print(elements)

            if system_tag == canva_1.itemcget(elements, "tags")[0:6]:
                #                  # print(elements)
                btn_id = canva_1.itemcget(elements, "window")
                bt_alarm = root.nametowidget(btn_id)
                # btn_alarm.config(background="red")

                if i >= 0 and i < 5:
                    ess_manager(system_tag, i)
                    # bt_alarm.config(background="red")
                # elif i == 1:
                #     bt_alarm.config(background="orange")
                # elif i == 2:
                #     bt_alarm.config(background="yellow")
                # elif i == 3:
                #     bt_alarm.config(background="antique white")
                # elif i >= 5:
                #     ess_manager(system_tag, i)
                #     break
                    # if str(bt_alarm['text']) in guard_sound_one.get_guard_set_system_sound_one():
                    #     btn_sound_on(bt_alarm)
                    # else:
                    #     bt_alarm.config(background="SystemButtonFace")

    print("ИТОГОВЫЙ ESS СЛОВАРЬ:" + (str(ess_timers_slovar)))

def schetchi_pustih_slovarey():
    i = len(shetchik_pustih_slovarey)

    shetchik_pustih_slovarey.append(i)

    print("СЛОВАРЬ ПУСТ  = " + (str(shetchik_pustih_slovarey[i])))

    print("ЗЕЛЁНЫЙ СЛОВАРЬ:" + (str(timers_slovar_green)))

    if len(shetchik_pustih_slovarey) == 50:
        default_btn_background_all_system()


def default_btn_background_all_system():
    for elements in find_all_canvas:
        btn_id = canva_1.itemcget(elements, "window")
        btn_alarm = root.nametowidget(btn_id)
        btn_alarm.config(background="SystemButtonFace")

    shetchik_pustih_slovarey.clear()
    timers_slovar_green.clear()
    btn_aQ1UIU.config(background="grey76")
    btn_a23Q2G.config(background="grey76")
    btn_a9IPCE.config(background="grey76")
    btn_aH1ESN.config(background="grey76")
    btn_aZXAV6.config(background="grey76")
    btn_a92DOI.config(background="grey76")
    btn_aUJYHE.config(background="grey76")


def proverka_na_sovpadenia():
    string_1.kontrol_close_file()

    print(" ----------- def proverka_na_sovpadenia(): ")

    # find_all_canvas = canva_1.find_all()

    print(" ----------- last_line_text: " + last_line_text)

    # append(item): добавляет элемент item в конец списка

    # splitted_last_line_text = last_line_text.split()

    for elements in find_all_canvas:
        # print(elements)
        # list_system.append(canva_1.itemcget(elements, "tags"))
        if canva_1.itemcget(elements, "tags")[0:6] in last_line_text:

            if string_ess.ess_check(last_line_text) == 1:
                # [07: 54:36] Dragon
                # Smart > < url = showinfo:1377 // 2116038957 > Amaranth
                # Amatin < / url > < url = showinfo:53451 // 9002034731002001777 > Needlejack            Trace < / url >

                print("!!!!!!!!!!       Е С Т Ь  ЕЩЁ  *****  ESS *****        С О В П А Д Е Н И Е         !!!!!!!!!")
                # ess_manager(canva_1.itemcget(elements, "tags")[0:6])
                # добавляем систему и текущее время срабатывания в ESS словарь

                find_system_alarm.add_ess_alarm_timers(((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M')),
                                                       canva_1.itemcget(elements, "tags")[0:6])

        # if ("clr" and canva_1.itemcget(elements, "tags"))  in last_line_text:
        # if canva_1.itemcget(elements, "tags")[0:6] in last_line_text and (
        #         "ess" in last_line_text or "ESS" in last_line_text or "Ess" in last_line_text):
        #     # [07: 54:36] Dragon
        #     # Smart > < url = showinfo:1377 // 2116038957 > Amaranth
        #     # Amatin < / url > < url = showinfo:53451 // 9002034731002001777 > Needlejack            Trace < / url >
        #
        #     print("!!!!!!!!!!       Е С Т Ь  ЕЩЁ  *****  ESS *****        С О В П А Д Е Н И Е         !!!!!!!!!")
        #     # ess_manager(canva_1.itemcget(elements, "tags")[0:6])
        #     # добавляем систему и текущее время срабатывания в ESS словарь
        #
        #     find_system_alarm.add_ess_alarm_timers(((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M')),
        #                                        canva_1.itemcget(elements, "tags")[0:6])

        if canva_1.itemcget(elements, "tags")[0:6] in last_line_text and (
                "clr" in last_line_text or "сlr" in last_line_text or "CLR" in last_line_text or
                "СLR" in last_line_text or
                "left" in last_line_text or
                "сдк" in last_line_text or
                "СДК" in last_line_text or
                "Needlejack Trace" in last_line_text or
                "сlear" in last_line_text or
                "clear" in last_line_text):

            # [07: 54:36] Dragon
            # Smart > < url = showinfo:1377 // 2116038957 > Amaranth
            # Amatin < / url > < url = showinfo:53451 // 9002034731002001777 > Needlejack            Trace < / url >

            print("!!!!!!!!!!       Е С Т Ь  ЕЩЁ  *****  CLR *****        С О В П А Д Е Н И Е         !!!!!!!!!")

            # canva_1.itemconfig(elements, fill="red")

            btn_id = canva_1.itemcget(elements, "window")
            btn_alarm = root.nametowidget(btn_id)
            btn_alarm.config(background="green yellow")
            # btn_alarm.flash()
            find_system_alarm.del_system_alarm(canva_1.itemcget(elements, "tags")[0:6])
            find_system_alarm.del_ess_system_alarm(canva_1.itemcget(elements, "tags")[0:6])
            ess_manager(canva_1.itemcget(elements, "tags")[0:6], 5)

            add_green_timers(((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M')),
                             canva_1.itemcget(elements, "tags")[0:6])

        elif canva_1.itemcget(elements, "tags")[0:6] in last_line_text:
            print("!!!!!!!!!!       Е С Т Ь              С О В П А Д Е Н И Е         !!!!!!!!!")
            # добавляем систему и текущее время срабатывания в словарь
            find_system_alarm.add_alarm_timers(((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M')),
                                               canva_1.itemcget(elements, "tags")[0:6])
            # добавляем систему в гуард соунд список, можеи лишнее, не забыть удалить)))
            # проигрываем звук
            # guard_sound.add_alarm_sound(canva_1.itemcget(elements, "tags")[0:6])
            alarm_sound(canva_1.itemcget(elements, "tags")[0:6])
        # else: alarm_sound()  # проигрываем звук

    # reed_tag = canva_1.itemcget(elements, "tags")
    print("ОТСЛЕЖИВАЕМЕ СИСТЕМЫ : " + (str(list_system)))
    print("ОТСЛЕЖИВАЕМЕ СИСТЕМЫ SOUND: " + (str(guard_list_system_sound)))
    obrabotka_timers_slovar()

    # find_system_alarm.find_alarm_system(list_system, last_line_text, find_all_canvas)


def del_green_system_slovar(systema_alarm_tag):
    if systema_alarm_tag in timers_slovar_green:
        timers_slovar_green.clear()
        # del timers_slovar_green[systema_alarm_tag]
        print(f"Элемент с ключом {systema_alarm_tag} удален из Зелёного СЛОВАРЯ")
    else:
        print("Элемент не найден! при попытке удалить из Зелёного СЛОВАРЯ систему  " + systema_alarm_tag)


def add_green_timers(datatime, tag_system):
    shetchik_pustih_slovarey.clear()

    print("------------------------------------")
    print("     add_green_timers()       ")
    print("------------------------------------")

    # проверка на наличие записи ключа(тега) сиситемы
    print("# проверка на наличие записи ключа(Tега) сиситемы = " + tag_system)

    if tag_system in timers_slovar_green:
        print("ЗАПИСЬ ECТЬ = " + tag_system + " : " + (str(timers_slovar_green[tag_system])))

        # Обновляем запись всёравно
        timers_slovar_green[tag_system] = datatime

        # если запись есть надо проверить сколько прошло времени с того момента и отреагировать на это
        # sravnivaem_datatime_green (datatime, tag_system)

    else:
        print("ЗАПИСЕЙ ДЛЯ ДАННОЙ СИСТЕМЫ НЕ Найдено  - ДОбАВЛЯЕМ НОВЫЙ ТАЙМЕР и Систему как ключ")
        timers_slovar_green[tag_system] = datatime

        # sravnivaem_datatime_green (datatime, tag_system)

    print("ИТОГОВЫЙ      З Е Л Ё Н Ы Й    СЛОВАРЬ:" + (str(timers_slovar_green)))
    # print(timers_slovar)


def sravnivaem_datatime_green(may_datatime, tag_system):
    print("  ******  def sravnivaem_datatime GREEN ********** ")

    save_data = timers_slovar[tag_system]
    print(save_data)
    # save_data_str = save_data.strftime('%Y, %m, %d, %H, %M')
    # print( save_data_str )
    naw_data = datetime.strptime(may_datatime, "%Y, %m, %d, %H, %M");
    print(naw_data)

    if save_data == naw_data:
        print(tag_system + " - ДАТЫ РАВНЫ")

    else:
        print("ДАТЫ   НЕ  РАВНЫ: ")

        # print("save_data.minute: " ); print( save_data ); print("Type: " ); print(type(save_data))
        # print("naw_data_minute: " ); print( naw_data ); print("Type: " ); print(type(naw_data))

        if isinstance(save_data, str):
            # print("ПРЕОБРАЗОВАНИЕ save_data ТИПА str В datatime ")
            test_datatime_2_save = datetime.strptime(save_data, "%Y, %m, %d, %H, %M")
            # print(type(test_datatime_2_save))
        else:
            test_datatime_2_save = save_data

        if isinstance(naw_data, str):
            # print("ПРЕОБРАЗОВАНИЕ naw_data ТИПА str В datatime ")
            test_datatime_3_naw = datetime.strptime(naw_data, "%Y, %m, %d, %H, %M")
            # print(type(test_datatime_3_naw))
        else:
            test_datatime_3_naw = naw_data

        # # test_datatime_1 = (2023,10,18,15,30)  Преобразование из строки в дату
        # # test_datatime_2_save = datetime.strptime(save_data, "%Y, %m, %d, %H, %M")

        test_datatime_4 = test_datatime_3_naw - test_datatime_2_save
        # print("ИТОГИ ВЫИЧТАНИЯ: ")
        # print(test_datatime_4)
        # print(test_datatime_4.seconds/60)

        # print( type (test_datatime_4) )
        # print(test_datatime_4.timedelta.minite)

        i = int(test_datatime_4.seconds / 60)

        print("прошло " + (str(i)) + " минут, для системы: " + tag_system)

        # print(save_data.)

        # raznica = naw_data - save_data

        # print("разница");print(raznica)

        if i >= 20:
            del_green_system_slovar(tag_system)
            ess_anim_del()
            return 4

        # def click():


#     window = Window()

# open_button = ttk.Button(canva_1, text="Создать окно", command=click)
# open_button.pack(anchor="center", expand=1)


# def gate(x1,y1,my_outline, my_fill):

#     canva_1.create_rectangle(x1,y1,x1+60,y1+40, outline=my_outline, fill=my_fill)


# qyzm_ID = gate(800,800,"#fb0", "#fb0")


# canva_1.create_rectangle(30,10,100,80, outline = "#fb0" , fill = "#fb0")

# import gate_test

# gate_test_1 = gate_test("#fb0", "#fb0")

# print(gate_test_1)

# # canva_1.create_rectangle(gate_test_1)

# import modyfy_file

# bd_setting.create_bd_all(my_path_bd_setting, my_path_bd_sound_one)
load_setting()

# if bd_setting.check_base_setting("sound_netral") == 0:
#     int_sound_chouse = 1
# else:
#     int_sound_chouse = int(bd_setting.reed_base_setting("sound_netral"))

time()

# string_1.go()
# last_line_text = string_1.last_line()
# path_live = string_1.max_path_live()
# gl_num_posl_stroki_live_reed = string_1.kol_strok()

add_line()

print("last_line_text= " + last_line_text)
# print("path_live= " + path_live )
print("num_posl_stroki_save= " + str(gl_num_posl_stroki_save))
print("num_posl_stroki_live_reed= " + str(gl_num_posl_stroki_live_reed))

# add_line(last_line_text)

# opros_file_cikl()

# modyfy_file.Watcher(path_live)

print(type(gl_num_posl_stroki_live_reed))

print(type(gl_num_posl_stroki_save))

print(gl_num_posl_stroki_live_reed == gl_num_posl_stroki_save)

# def proverka_num():

#         string_1.go()
#         print ("**** proverka_num() *****")

#         global gl_num_posl_stroki_save

#         if (gl_num_posl_stroki_live_reed == gl_num_posl_stroki_save):
#             print ("НЕТ Новой строки")

#             # proverka_num()

#         else:
#             print ("ECТЬ Новая строка")

#             gl_num_posl_stroki_save = string_1.kol_strok()

#             add_line(last_line_text)

# def tttt():

#     def proverka_num():

#         string_1.go()
#         print ("**** proverka_num() *****")

#         global gl_num_posl_stroki_save

#         if (gl_num_posl_stroki_live_reed == gl_num_posl_stroki_save):
#             print ("НЕТ Новой строки")

#             # proverka_num()

#         else:
#            print ("ECТЬ Новая строка")


#            gl_num_posl_stroki_save = string_1.kol_strok()

#            add_line(last_line_text)

#         time.sleep(60)

#     while True:
#       try:
#             #code here
#             proverka_num()
#       except KeyboardInterrupt:
#             print('\nDone')
#             break
#       except FileNotFoundError:
#             # Action on file not found
#             pass
#       except:
#             print('Unhandled error: %s' % sys.exc_info()[0])

# proverka_num()
# def executeSomething():
#     print ("**** proverka_num() *****")
#     #code here
#     time.sleep(60)

# while True:
#     executeSomething()

# def opros_file_cikl():

#     if (num_posl_stroki_live_reed == num_posl_stroki_save):

#         print ("НЕТ Новой строки")

#     else:
#           num_posl_stroki_live_reed = string_1.kol_strok().after(10, opros_file_cikl)

# label_2.configure(width=0)
# label_2.pack


def finish():

    # string_1.string_exit()
    # label_2.configure(width=0)
    # label_2.config(width=1)
    # print("label_2.winfo_x() = " + str(label_2.winfo_x()))

    save_window_position()
    root.destroy()  # ручное закрытие окна и всего приложения
    #
    # tkinter.Tk.quit()
    print("Закрытие приложения")

    # root.quit()
    # root.destroy()
    # sys.exit()

    # exit()


if __name__ == "__main__":
    # root.after(3000, proverka_num())
    # proverka_num()
    root.protocol("WM_DELETE_WINDOW", finish)
    root.mainloop()

# root.mainloop()

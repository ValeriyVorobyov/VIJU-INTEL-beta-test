# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:54:10 2023

@author: V5"""





from datetime import datetime, timedelta
import os
import sys
import asyncio
import time
from tkinter import *
# import tkinter  as tk
# from tkinter import ttk
from tkinter import colorchooser
# import winsound
# from playsound import playsound
from playsound import playsound
# from tkinter.ttk import *

# from PIL import Image, ImageTk

# импорт модуля для преобразования кортежей через format
from time import strftime

import string_1
import save_settings
import find_system_alarm


path_live = "......./Documents/EVE/logs/Chatlogs/"

path_os = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')

mypath_dir = path_os + "/EVE/logs/Chatlogs/"



gl_num_posl_stroki_live_reed = 0
gl_num_posl_stroki_save = 0
gl_last_line_text = ""

list_system = list()
timers_slovar = {}
timers_slovar_green = {}
shetchik_pustih_slovarey = list()

bufer_intel = list()

image_sound_on_off = "on"
int_sound_chouse = 1



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
my_path_alarm_on_png = resource_path('alarm_on.png')
my_path_alarm_off_png = resource_path('alarm_off.png')
my_path_icon = resource_path('icon_1.png')









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
root.geometry('850x489+100+100')
icon = PhotoImage(file = my_path_icon)
root.iconphoto(False, icon)




# Нужно чтобы выводить в консоле координаты на канве куда тыкаешь мышкой во время проектирования
def print_coords(event):
    print(event.x, event.y)





# MEНЮ


# root.option_add("*tearOff", FALSE)  # отключает пунктирную линию в подменю, которая совершенно не нужна 










def select_color():
    
    result = colorchooser.askcolor(initialcolor="black")
    # canva_1.configure(canva_1, bg="grey87")
    print("  --- ***************** ---  ")
    print("  --- ***************** ---  ")
    print("  ---  def select_color():  --- > " +  (str(result))         )
    print("  --- ***************** ---  ") 
    print("  --- ***************** ---  ") 
    # canva_1["foreground"] = result[1]
    canva_1.config( bg = result[1])
    my_text.config( bg = result[1])
    settings_menu.config(  bg = result[1] )
    
def help_click():
    messagebox.showinfo("GUI Python", "едрён батон")
 
   
    
def alarm_sound():
    
     # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA alarm_sound(int_int): =  " + (str)(int_sound_chouse))         
       
     if image_sound_on_off == "on":            
         
         if int_sound_chouse == 1: playsound(my_path_mp3_01, FALSE)
         elif int_sound_chouse == 2: playsound(my_path_mp3_02, FALSE)
         elif int_sound_chouse == 3: playsound(my_path_mp3_03, FALSE)
         

def chouse_sound_1():
      global  int_sound_chouse 
      int_sound_chouse = 1
      alarm_sound()
      
def chouse_sound_2():
    
      # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))
      
      global  int_sound_chouse 
      int_sound_chouse = 2
      alarm_sound()  

def chouse_sound_3():
    
      # print("  ---AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA chouse_sound_2: =  " + (str)(a))
      
      global  int_sound_chouse 
      int_sound_chouse = 3
      alarm_sound()               
          
# def chouse_sound_1():
    
#       int_sound_chouse = int_int
      
#       if  int_int == 1:  alarm_sound(1)
#       elif int_int == 2: alarm_sound(2)            
       
     
    # playsound('alarm_1.mp3', winsound.SND_FILENAME | winsound.SND_ASYNC)
    # playsound('alarm_1.mp3')

    
def click_TEST_button():
    
     print("  ---  click_TEST_button():   ---  ")
     
     # last_line_text = " TEST "
     
     # find_system_alarm.add_alarm_timers(((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M')) , "TEST")
     
     # proverka_na_sovpadenia()
     global last_line_text
     last_line_text = " TuK-TuK* "
     
     my_text.insert(CURRENT, "\n" + last_line_text)
     
     proverka_na_sovpadenia()
   
     # obrabotka_timers_slovar()
     
def click_TuKTuK_button():
    
     print("  ---  click_TuKTuK_button():   ---  ")
     
     # last_line_text = " TEST "
     
     # find_system_alarm.add_alarm_timers(((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M')) , "TEST-2")
     global last_line_text
     last_line_text = " TuK-TuK* clr"
     
     my_text.insert(CURRENT, "\n" + last_line_text)
     
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
        
        set_image(my_image_off) ;   image_sound_on_off = "off"   
              
        
                          
    else: 
        
        # print("К Л И К  - OFF ")
        
        set_image(my_image_on) ;    image_sound_on_off = "on"     
       



def load_image (name):    
    
        return PhotoImage(file=name)  
 
def set_image (image):
    # canvas.delete("all")
    # canvas.create_image(100,115,image=image)
    
    # btn_alarm.config ( image=image )
    
    canva_1.itemconfigure("img_alarm_on_off", image=image)
    
    
    
my_image_on  = load_image (my_path_alarm_on_png) 
my_image_off = load_image (my_path_alarm_off_png)
      


    
    
    
# @!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
#      МЕНЮ
main_menu = Menu(root, activebackground="red", tearoff=0)

settings_menu = Menu(main_menu, activebackground="red", tearoff=0)

sound_menu = Menu(settings_menu, activebackground="red", tearoff=0)
sound_menu.add_command(label="Alarm sound-1",  command=chouse_sound_1)
sound_menu.add_command(label="Alarm sound-2",  command=chouse_sound_2)
sound_menu.add_command(label="Alarm sound-3",  command=chouse_sound_3)
# sound_menu.add_command(label="Alarm sound-4", command=alarm_sound)
settings_menu.add_cascade(label="Sound", menu=sound_menu)

color_menu = Menu(settings_menu, activebackground="red", tearoff=0)
color_menu.add_command(label="Color Fon",  command=select_color)
settings_menu.add_cascade(label="Color",  menu=color_menu)

main_menu.add_cascade(label="Настройки",  menu=settings_menu)
main_menu.add_cascade(label="Справка",  command=help_click)

root.config(menu=main_menu)
settings_menu.config( bg="blue" )

# @!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 










def select_color():
    result = colorchooser.askcolor(initialcolor="black")
    # canva_1.fill_style(result[1])
    # label["foreground"] = result[1]

def click(): 
    print("Hello")




main_frame = Frame(root, relief=SOLID)

# btn_zoom_in = Button(root, text="Zoom In", command=zoom_in)
# btn_zoom_in.pack(side=TOP)

# btn_zoom_out = Button(root, text="Zoom Out", command=zoom_out)
# btn_zoom_out.pack(side=TOP)


main_frame.pack(expand=2, fill=BOTH)

pw = PanedWindow(main_frame,  bd=2, orient="horizontal")

frame_1 = Frame(pw, borderwidth=2, relief=RAISED)

canva_1 = Canvas(frame_1, width=700, bg="grey87")
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
# canva_1.pack()


wbtn=8

hbtn=2

xbtn=-0.19





btn_aQYZMW = Button(text="QYZM-W")
btn_aBUIU4 = Button(text="BU-IU4")
btn_aI7JR4 = Button(text="I-7JR4")
btn_aME4IU = Button(text="ME-4IU")
btn_aCH9LK = Button(text="CH9L-K")
btn_a9B1DS = Button(text="9-B1DS")
btn_a3KNAN = Button(text="3KNA-N")
btn_aQ1UIU = Button(text="Q1U-IU")
btn_aKJQWL = Button(text="KJ-QWL")
btn_aKMQ4V = Button(text="KMQ4-V")
btn_aSVBRE = Button(text="SVB-RE")
btn_a5P1Y2 = Button(text="5-P1Y2")
btn_aJ52BH = Button(text="J52-BH")
btn_aCLBQS = Button(text="C-LBQS")
btn_aBWI19 = Button(text="BWI1-9")
btn_aKL30J = Button(text="KL30-J")
btn_aR40I6 = Button(text="R4O-I6")
btn_aQNJZ4 = Button(text="Q-NJZ4")
btn_aNLPB0 = Button(text="NLPB-0")
btn_a3TD6L = Button(text="3-TD6L")
btn_aCX1XF = Button(text="CX-1XF")
btn_aX4UVZ = Button(text="X4UV-Z")
btn_aJRZB9 = Button(text="JRZ-B9")
btn_aV8WQS = Button(text="V8W-QS")

btn_aSB7IT = Button(text="S-B7IT")

btn_aBKGQ2 = Button(text="BKG-Q2")

btn_aZK495 = Button(text="Z-K495")
btn_a84GQM = Button(text="8-4GQM")
btn_aLXWNW = Button(text="LXWN-W")

btn_aJSILL = Button(text="JSI-LL")
btn_aU5XW7 = Button(text="U5-XW7")
btn_aMUC05 = Button(text="M-UC05")
btn_aSY0W2 = Button(text="SY0W-2")
btn_aV7MID = Button(text="V7-MID")
btn_aMZPHW = Button(text="MZPH-W")

btn_aTEST = Button(text="T E S T", command = click_TEST_button)
btn_aTuKTuK = Button(text="TuK-TuK", command = click_TuKTuK_button)


# canva_1.create_line(10, 10, 20, 20)

btn_window_width=65

sistem_x=-200
sistem_y=-240

aQYZMW = canva_1.create_window(sistem_x+500, sistem_y+500, anchor=NW, window=btn_aQYZMW, width=btn_window_width, tags=["QYZM-W"])
aI7JR4 = canva_1.create_window(sistem_x+430, sistem_y+500, anchor=NW, window=btn_aI7JR4, width=btn_window_width, tags=["I-7JR4"])
aBUIU4 = canva_1.create_window(sistem_x+500, sistem_y+470, anchor=NW, window=btn_aBUIU4, width=btn_window_width, tags=["BU-IU4"])
aME4IU = canva_1.create_window(sistem_x+430, sistem_y+470, anchor=NW, window=btn_aME4IU, width=btn_window_width, tags=["ME-4IU"])
aCH9LK = canva_1.create_window(sistem_x+360, sistem_y+500, anchor=NW, window=btn_aCH9LK, width=btn_window_width, tags=["CH9L-K"])
a9B1DS = canva_1.create_window(sistem_x+360, sistem_y+470, anchor=NW, window=btn_a9B1DS, width=btn_window_width, tags=["9-B1DS"])
a3KNAN = canva_1.create_window(sistem_x+430, sistem_y+440, anchor=NW, window=btn_a3KNAN, width=btn_window_width, tags=["3KNA-N"])
aQ1UIU = canva_1.create_window(sistem_x+360, sistem_y+550, anchor=NW, window=btn_aQ1UIU, width=btn_window_width, tags=["Q1U-IU"])

aJSILL = canva_1.create_window(sistem_x+360, sistem_y+595, anchor=NW, window=btn_aJSILL, width=btn_window_width, tags=["SI-LL"])
aSY0W2 = canva_1.create_window(sistem_x+290, sistem_y+630, anchor=NW, window=btn_aSY0W2, width=btn_window_width, tags=["SY0W-2"])
aMUC05 = canva_1.create_window(sistem_x+290, sistem_y+595, anchor=NW, window=btn_aMUC05, width=btn_window_width, tags=["M-UC05"])
aV7MID = canva_1.create_window(sistem_x+220, sistem_y+630, anchor=NW, window=btn_aV7MID, width=btn_window_width, tags=["V7-MID"])
aU5XW7 = canva_1.create_window(sistem_x+360, sistem_y+630, anchor=NW, window=btn_aU5XW7, width=btn_window_width, tags=["U5-XW7"])
aMZPHW = canva_1.create_window(sistem_x+360, sistem_y+670, anchor=NW, window=btn_aMZPHW, width=btn_window_width, tags=["MZPH-W"])

aKJQWL = canva_1.create_window(sistem_x+360, sistem_y+390, anchor=NW, window=btn_aKJQWL, width=btn_window_width, tags=["KJ-QWL"])
aKMQ4V = canva_1.create_window(sistem_x+428, sistem_y+390, anchor=NW, window=btn_aKMQ4V, width=btn_window_width, tags=["KMQ4-V"])
aSVBRE = canva_1.create_window(sistem_x+370, sistem_y+355, anchor=NW, window=btn_aSVBRE, width=btn_window_width, tags=["SVB-RE"])

a5P1Y2 = canva_1.create_window(sistem_x+497, sistem_y+390, anchor=NW, window=btn_a5P1Y2, width=btn_window_width, tags=["5-P1Y2"])
aJ52BH = canva_1.create_window(sistem_x+565, sistem_y+390, anchor=NW, window=btn_aJ52BH, width=btn_window_width, tags=["J52-BH"])
aCLBQS = canva_1.create_window(sistem_x+633, sistem_y+390, anchor=NW, window=btn_aCLBQS, width=btn_window_width, tags=["C-LBQS"])
aBWI19 = canva_1.create_window(sistem_x+700, sistem_y+390, anchor=NW, window=btn_aBWI19, width=btn_window_width, tags=["BWI1-9"])
aKL30J = canva_1.create_window(sistem_x+769, sistem_y+390, anchor=NW, window=btn_aKL30J, width=btn_window_width, tags=["KL3O-J"])
aR40I6 = canva_1.create_window(sistem_x+768, sistem_y+355, anchor=NW, window=btn_aR40I6, width=btn_window_width, tags=["R4O-I6"])

aQNJZ4 = canva_1.create_window(sistem_x+835, sistem_y+355, anchor=NW, window=btn_aQNJZ4, width=btn_window_width, tags=["Q-NJZ4"])
aNLPB0 = canva_1.create_window(sistem_x+835, sistem_y+310, anchor=NW, window=btn_aNLPB0, width=btn_window_width, tags=["NLPB-0"])
a3TD6L = canva_1.create_window(sistem_x+768, sistem_y+310, anchor=NW, window=btn_a3TD6L, width=btn_window_width, tags=["3-TD6L"])
aCX1XF = canva_1.create_window(sistem_x+680, sistem_y+295, anchor=NW, window=btn_aCX1XF, width=btn_window_width, tags=["CX-1XF"])
aX4UVZ = canva_1.create_window(sistem_x+530, sistem_y+295, anchor=NW, window=btn_aX4UVZ, width=btn_window_width, tags=["X4UV-Z"])
aJRZB9 = canva_1.create_window(sistem_x+530, sistem_y+260, anchor=NW, window=btn_aJRZB9, width=btn_window_width, tags=["JRZ-B9"])
aV8WQS = canva_1.create_window(sistem_x+605, sistem_y+260, anchor=NW, window=btn_aV8WQS, width=btn_window_width, tags=["V8W-QS"])

aSB7IT = canva_1.create_window(sistem_x+455, sistem_y+260, anchor=NW, window=btn_aSB7IT, width=btn_window_width, tags=["S-B7IT"])
aBKGQ2 = canva_1.create_window(sistem_x+455, sistem_y+295, anchor=NW, window=btn_aBKGQ2, width=btn_window_width, tags=["BKG-Q2"])
aZK495 = canva_1.create_window(sistem_x+325, sistem_y+245, anchor=NW, window=btn_aZK495, width=btn_window_width, tags=["Z-K495"])
a84GQM = canva_1.create_window(sistem_x+315, sistem_y+285, anchor=NW, window=btn_a84GQM, width=btn_window_width, tags=["8-4GQM"])
aLXWNW = canva_1.create_window(sistem_x+220, sistem_y+364, anchor=NW, window=btn_aLXWNW, width=btn_window_width, tags=["LXWN-W"])


aTEST = canva_1.create_window(sistem_x+220, sistem_y+280, anchor=NW, window=btn_aTEST, width=btn_window_width, tags=["TEST"])
aTuKTuK = canva_1.create_window(sistem_x+220, sistem_y+320, anchor=NW, window=btn_aTuKTuK, width=btn_window_width, tags=["TuK-TuK"])



# canva_1.create_line(10, 10, 20, 20)




find_all_canvas = canva_1.find_all()

for elements in find_all_canvas:
          print(elements)
          list_system.append(canva_1.itemcget(elements, "tags"))






# coord_CH = []
# coord_CH = canva_1.coords(aSVBRE)
# print(coord_CH)

# coord_CH = canva_1.coords(aMZPHW)
# print(coord_CH)

canva_1.bind("<Button-1>", print_coords)


# canva_1.create_line(393, 66, 499, 68, fill="black", stipple='warning', splinesteps=1, width=2)

my_wwidth_01 = 1.4

kl30j_r40i6 = canva_1.create_line(600, 125, 600, 150, fill="burlywood4", splinesteps=10, width=my_wwidth_01)
bwi9_kl30j = canva_1.create_line(565, 162, 600, 162, fill="burlywood4", splinesteps=10, width=my_wwidth_01)

canva_1.create_line(320, 67, 499, 67, fill="burlywood4", splinesteps=10, width=my_wwidth_01)

canva_1.create_line(360, 45, 360, 54, fill="burlywood4", splinesteps=0, width=my_wwidth_01)

canva_1.create_line(320, 32, 405, 32, fill="burlywood4", splinesteps=0, width=my_wwidth_01)
canva_1.create_line(286, 55, 286, 45, fill="burlywood4", splinesteps=0, width=my_wwidth_01)

zk_bkg=canva_1.create_line(190, 17, 255, 61, fill="burlywood4", splinesteps=5, width=my_wwidth_01)
a84qm_bkg = canva_1.create_line(180, 57, 255, 66, fill="burlywood4", splinesteps=5, width=my_wwidth_01)

line_LXWNW_BKG = canva_1.create_line(85, 134, 255, 69, fill="burlywood4", splinesteps=5, width=my_wwidth_01)

canva_1.create_line(190, 430, 190, 140, fill="burlywood4", splinesteps=0, width=my_wwidth_01)


canva_1.create_line(85, 402, 165, 402, fill="burlywood4", splinesteps=0, width=my_wwidth_01)
canva_1.create_line(156, 367, 165, 367, fill="burlywood4", splinesteps=0, width=my_wwidth_01)
canva_1.create_line(122, 380, 122, 389, fill="burlywood4", splinesteps=0, width=my_wwidth_01)

canva_1.create_line(225, 272, 300, 272, fill="burlywood4", splinesteps=0, width=my_wwidth_01)
canva_1.create_line(225, 242, 300, 242, fill="burlywood4", splinesteps=0, width=my_wwidth_01)
canva_1.create_line(261, 216, 261, 260, fill="burlywood4", splinesteps=0, width=my_wwidth_01)

canva_1.create_line(225, 163, 500, 163, fill="burlywood4", splinesteps=0, width=my_wwidth_01)

a3td6l_r40 = canva_1.create_line(600, 90, 600, 116, fill="burlywood4", splinesteps=0, width=my_wwidth_01)
a3td6l_qn = canva_1.create_line(600, 90, 660, 116, fill="burlywood4", splinesteps=0, width=my_wwidth_01)
nlpb_qn = canva_1.create_line(667, 90, 667, 116, fill="burlywood4", splinesteps=0, width=my_wwidth_01)

# canva_1.create_line(563, 120, 670, 120, fill="burlywood4", splinesteps=0, width=my_wwidth_01)

cx1xf_3t=canva_1.create_line(544, 67, 566, 82, fill="burlywood4", splinesteps=0, width=my_wwidth_01)


# canva_1.create_arc(366, 182, 600, 305,   start=160, extent=170,  style=ARC, outline='darkblue', fill='orange',  width=2)

# canva_1.create_oval(363, 182, 600, 305,               fill='lightgrey',              outline='white')

# canva_1.create_rectangle(363, 182, 598, 305 )

# bu -- kl
canva_1.create_line(366, 244, 600, 244, activefill="red", fill="green", dash=5)
canva_1.create_line(600, 175, 600, 244, activefill="red", fill="green", dash=5)

# me -- 5p
canva_1.create_line(329, 175, 329, 200, activefill="red", fill="green", dash=1)
canva_1.create_line(329, 200, 292, 232, activefill="red", fill="green", dash=1)





canva_1.create_text(505, 234, text="bridje", activefill="red", fill="#004D40")







# image_on_alarm = Image.open("alarm_on.png")
# image_off_alarm = Image.open("alarm_off.png")

# # resized_image = image2.resize((24, 24))

# resized_image_on = image_on_alarm.reduce(3)
# resized_image_off = image_on_alarm.reduce(3)

# alarm_on_off = ImageTk.PhotoImage(resized_image_on)


# alarm_off_ = ImageTk.PhotoImage(resized_image_on)


# image_alarm_on = PhotoImage(file="alarm_on.png" , width=1, height=1)
# image_alarm_on = PhotoImage(file="alarm_on.png", width=0, height=0 )

# image_alarm_on.subsample(0, 0)
# image_alarm_off = PhotoImage(file="alarm_off.png")
 
# alarm_on = canva_1.create_image(668, 4, anchor=NW, image=image_alarm_on)
# alarm_on.scale(0, 0, 1.1, 1.1)




# btn_alarm = Button( command =  alarm_on_off_btn_1_click)



# image_alarm_on = PhotoImage(file=my_path_alarm_on_png)
# image_alarm_on = image_alarm_on.zoom(-2) #with 250, I ended up running out of memory

btn_alarm = Button ( command =  alarm_on_off_btn_1_click  )

# imgpath = '/path/to/img.png'
# img = PhotoImage(file=imgpath)
# img = img.zoom(25) #with 250, I ended up running out of memory
# img = img.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
# panel = Label(root, image = img)





# btn_alarm.grid()
# btn_alarm.place(relx=0.5, rely=0.8)



id_canva_alarm_on_off = canva_1.create_image(673, 6, anchor=NW, tags=["img_alarm_on_off"] )





set_image(my_image_on)


# id_canva_alarm_on_off_btn = canva_1.create_window(669, 6, anchor=NW, window=btn_alarm, width=29, height=29, tags=["btn_alarm_on_off"])



canva_1.tag_bind(id_canva_alarm_on_off, "<Button-1>", alarm_on_off_btn_1_click)










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
frame_1.pack()


# bt2 = ttk.Button(frame_1, text="Добавить", command=lambda:add("Добавить"))

# bt2 = ttk.Button(canva_1, text="Добавить", command=add)
# bt2 = ttk.Button(frame_1, text="Добавить", command=add)

# bt2.pack(expand=1)

pw.add(frame_1)

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
my_text = Text (frame_2, wrap="word", bg="grey87")
# my_text.config()

# scroll = Scrollbar(command = my_tex.yview)

# scroll.pack(side=LEFT, fill=Y)


# frame_2.pack(fill=X)
frame_2.pack()


pw.add(frame_2)

pw.pack(fill="both", expand=1)


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
    elif ( gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save ) > 1  and ( gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save ) < 10:
        print("НЕТ Новой строки2 Разница =  " + (str(gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save)))
        print("НЕТ Новой строки2 ")
        print("НЕТ Новой строки2 ")    
        print("______________________________ +++    А Л Ё    +++___________________________________________ ")    
        print("______________________________ +++    А Л Ё    +++___________________________________________ ") 
        print("______________________________ +++    А Л Ё    +++___________________________________________ ") 
        
        
        # 186 - 184 = 2         
        
        raznica = gl_num_posl_stroki_live_reed - gl_num_posl_stroki_save # 5            
                
        last_line_text = string_1.shouse_line_intel_stroka(gl_num_posl_stroki_live_reed-(raznica)) 
        
        # Добовляем новую строку
        # my_text.insert(END, "\n" + last_line_text)  # РАБОЧИЙ ВАРИАНТ
        
        my_text.insert(CURRENT, "\n" + last_line_text)
        
        
        # new = gl_num_posl_stroki_live_reed - (raznica+1)

                                         # 186-2 + 1               
        gl_num_posl_stroki_save =  (gl_num_posl_stroki_live_reed - raznica) + 1
        
        
        
        
        proverka_na_sovpadenia()


    else: 
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   ECТЬ Новая строка  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        
       
        
        # podsvedka_sistem()
        proverka_na_sovpadenia()
        
        
        # ТУТ НАДО ДЕЛАТЬ ПРОВЕРКУ НА КОЛИЧЕСТВО НОВЫХ СТРОК
        
        
        

        # Добовляем новую строку
        # my_text.insert(END, "\n" + last_line_text)  # РАБОЧИЙ ВАРИАНТ END - вставка в низ списка
        my_text.insert(CURRENT, "\n" + last_line_text) # РАБОЧИЙ ВАРИАНТ CURRENT - вставка в верх списка
        
        
        

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
     
     timers_slovar  =  find_system_alarm.peredaem_alarm_slovar()
    
     for system_tag in timers_slovar:
        
            print (f"Sytem: {system_tag}  Timer {timers_slovar[system_tag]} ")      
            
            tekuhee_datatime = ((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M'))
            i = find_system_alarm.sravnivaem_datatime(tekuhee_datatime, system_tag)
            
            print ("  i =  " + (str(i)) + ", Sytem: " + system_tag ) 
            
            if i == 4:             
                
                # поиск элемента по тэгу
                for elements in find_all_canvas:
#               # print(elements)
                
                   if system_tag == canva_1.itemcget(elements, "tags"):
#                      # print(elements)
                       btn_id = canva_1.itemcget(elements, "window")
                       btn_alarm = root.nametowidget(btn_id)
                       btn_alarm.config(background="SystemButtonFace") 
                       
                break  # прерываем весь цыкл из за удаления элемента из timers_slovar
                
            # # поиск элемента по тэгу
            for elements in find_all_canvas:
#               # print(elements)
                
                if system_tag == canva_1.itemcget(elements, "tags"):
#                  # print(elements)
                   btn_id = canva_1.itemcget(elements, "window")
                   btn_alarm = root.nametowidget(btn_id)
                   # btn_alarm.config(background="red")  
            
                   if i == 0: btn_alarm.config(background="red") 
                   elif i == 1: btn_alarm.config(background="orange") 
                   elif i == 2: btn_alarm.config(background="yellow") 
                   elif i == 3: btn_alarm.config(background="antique white") 
                   elif i == 4: 
                       btn_alarm.config(background="SystemButtonFace") 
     


                       
     
         
                   
                
                
     
     print("ИТОГОВЫЙ СЛОВАРЬ:" + (str(timers_slovar)))
     
     # btn_id = canva_1.itemcget(system_tag, "window")
     # btn_alarm = root.nametowidget(btn_id)
     # if i == 4: btn_alarm.config(background="SystemButtonFace") 
     if len(timers_slovar) == 0 and len(timers_slovar_green) != 0  :
        
        schetchi_pustih_slovarey()       
           
         
def schetchi_pustih_slovarey():
    
    i = len (shetchik_pustih_slovarey)
    
    shetchik_pustih_slovarey.append(i)
    
    print("СЛОВАРЬ ПУСТ  = " + (str(shetchik_pustih_slovarey[i])))
    
    print("ЗЕЛЁНЫЙ СЛОВАРЬ:" + (str(timers_slovar_green)))
    
    if len (shetchik_pustih_slovarey) == 50: default_btn_background_all_system()
        
def default_btn_background_all_system():
    
     for elements in find_all_canvas:
         
         btn_id = canva_1.itemcget(elements, "window")
         btn_alarm = root.nametowidget(btn_id)
         btn_alarm.config(background="SystemButtonFace")
         
     shetchik_pustih_slovarey.clear()
     timers_slovar_green.clear()
       




def proverka_na_sovpadenia():
    
     string_1.kontrol_close_file()
    
     print(" ----------- def proverka_na_sovpadenia(): ")
     
     # find_all_canvas = canva_1.find_all()
     
     print(" ----------- last_line_text: " + last_line_text)
     
     
     
     # append(item): добавляет элемент item в конец списка
     
     for elements in find_all_canvas:
          print(elements)
          # list_system.append(canva_1.itemcget(elements, "tags"))
          
          # if ("clr" and canva_1.itemcget(elements, "tags"))  in last_line_text:   
          
          if  canva_1.itemcget(elements, "tags") in last_line_text and ( "clr"  in last_line_text or "сlr"  in last_line_text ) :   
                   
                   print("!!!!!!!!!!       Е С Т Ь  ЕЩЁ  *****  CLR *****        С О В П А Д Е Н И Е         !!!!!!!!!")
               
               # canva_1.itemconfig(elements, fill="red")
                     
                   btn_id = canva_1.itemcget(elements, "window")
                   btn_alarm = root.nametowidget(btn_id)
                   btn_alarm.config(background="green yellow")
                   # btn_alarm.flash()
                   find_system_alarm.del_system_alarm(canva_1.itemcget(elements, "tags"))
                   
                   add_green_timers(((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M')) , canva_1.itemcget(elements, "tags"))
             
          
          
         
         
          elif canva_1.itemcget(elements, "tags") in last_line_text:
               print("!!!!!!!!!!       Е С Т Ь              С О В П А Д Е Н И Е         !!!!!!!!!")
                # добавляем систему и текущее время срабатывания в словарь
               find_system_alarm.add_alarm_timers(((datetime.now() + timedelta(hours=-3)).strftime('%Y, %m, %d, %H, %M')) , canva_1.itemcget(elements, "tags"))
               # проигрываем звук
               alarm_sound()
               
               
                   
          # else: alarm_sound()  # проигрываем звук
               
               
               
               
               
               
               
              
         # reed_tag = canva_1.itemcget(elements, "tags")
     print("ОТСЛЕЖИВАЕМЕ СИСТЕМЫ : " + (str(list_system)))  
     obrabotka_timers_slovar()
     
     # find_system_alarm.find_alarm_system(list_system, last_line_text, find_all_canvas)

    
def del_green_system_slovar (systema_alarm_tag):
    
   
    
    if systema_alarm_tag in timers_slovar_green:
        timers_slovar_green.clear()
        # del timers_slovar_green[systema_alarm_tag]
        print(f"Элемент с ключом {systema_alarm_tag} удален из Зелёного СЛОВАРЯ")
    else:
        print("Элемент не найден! при попытке удалить из Зелёного СЛОВАРЯ систему  " + systema_alarm_tag )


def add_green_timers (datatime, tag_system):
    
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

def sravnivaem_datatime_green (may_datatime, tag_system):
    
    print("  ******  def sravnivaem_datatime GREEN ********** ")
    
    save_data = timers_slovar[tag_system]; print( save_data )
    # save_data_str = save_data.strftime('%Y, %m, %d, %H, %M')
    # print( save_data_str )
    naw_data = datetime.strptime(may_datatime, "%Y, %m, %d, %H, %M") ; print( naw_data )
    
    if save_data == naw_data: print(tag_system + " - ДАТЫ РАВНЫ")
   
    else:
        print("ДАТЫ   НЕ  РАВНЫ: ")
        
        # print("save_data.minute: " ); print( save_data ); print("Type: " ); print(type(save_data))
        # print("naw_data_minute: " ); print( naw_data ); print("Type: " ); print(type(naw_data))
        
        if isinstance(save_data, str):
            # print("ПРЕОБРАЗОВАНИЕ save_data ТИПА str В datatime ")
            test_datatime_2_save = datetime.strptime(save_data, "%Y, %m, %d, %H, %M")
            # print(type(test_datatime_2_save))
        else:test_datatime_2_save = save_data
            
        if isinstance(naw_data, str):
            # print("ПРЕОБРАЗОВАНИЕ naw_data ТИПА str В datatime ")
            test_datatime_3_naw = datetime.strptime(naw_data, "%Y, %m, %d, %H, %M")
            # print(type(test_datatime_3_naw))
        else:test_datatime_3_naw = naw_data
        
        # # test_datatime_1 = (2023,10,18,15,30)  Преобразование из строки в дату
        # # test_datatime_2_save = datetime.strptime(save_data, "%Y, %m, %d, %H, %M")
        
        test_datatime_4 = test_datatime_3_naw  -  test_datatime_2_save 
        # print("ИТОГИ ВЫИЧТАНИЯ: ")
        # print(test_datatime_4)
        # print(test_datatime_4.seconds/60)
        
        # print( type (test_datatime_4) )
        # print(test_datatime_4.timedelta.minite)
        
        i = int(test_datatime_4.seconds/60)
       
        print("прошло " + (str(i)) + " минут, для системы: " + tag_system  )
        
        # print(save_data.)
        
        # raznica = naw_data - save_data
        
        # print("разница");print(raznica)
        
     
        if i >= 20: 
            del_green_system_slovar(tag_system)
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

def finish():
    # string_1.string_exit()
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

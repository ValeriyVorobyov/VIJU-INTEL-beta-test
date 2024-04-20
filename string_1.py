# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:00:23 2023

@author: V5
"""

import os

import glob
# import datetime
from datetime import datetime

mypath_dir = "C:/......./Documents/EVE/logs/Chatlogs/"
path_live = "C:/......./Documents/EVE/logs/Chatlogs/"
num_posl_stroki_live_reed = 0
num_posl_stroki_save = 0
last_line_text = ""
# print("string_1.py - > last_line_text= " + last_line_text)

list_path_files = list()
save_format_data_perebora_files = datetime(2000, 1, 1, 0, 0)

path_os = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
# print(path_os)
mypath_dir = path_os + "/EVE/logs/Chatlogs/"


# print(mypath_dir)

# people = ["Tom", "Sam", "Bob"]
# for person in people:
#     print(person)


def perebor_files(list_path_files):
    global path_live

    try:

        for one_file_path in list_path_files:

            # print(one_file_path)

            last_line_text_iz_perebor_files = last_line_iz_perebor_files(one_file_path)

            data_time_format_iz_perebira = str_date(last_line_text_iz_perebor_files)

            my_int = files_sravnivaem_datatime_iz_perebora(data_time_format_iz_perebira)

            if my_int == 1:

                itogovity_path = one_file_path
                path_live = one_file_path

            else:
                itogovity_path = path_live

        return itogovity_path

    except:
        print(" string_1.py - >  perebor_files(): ОШИБКА !  ")


# Последняя строка
def last_line_iz_perebor_files(one_file_path):
    try:

        with open(one_file_path, 'r', encoding='utf-16') as file:
            global last_line_text_iz_perebor_files
            last_line_text_iz_perebor_files = file.readlines()[-1]

        # print("string_1.py -> def last_line_iz_perebor_files -> last_line_text_iz_perebor_files = " + last_line_text_iz_perebor_files)
        # return last_line_text
    except:
        print(" !!!! вышло хреново в  string_1 ->  def last_line():  !!!! ")

    return last_line_text_iz_perebor_files


def files_sravnivaem_datatime_iz_perebora(data_time_format_iz_perebira):
    global save_format_data_perebora_files

    # print("  ***********           ********** ")
    # print("  ***********    дата перебора "  +  (str(data_time_format_iz_perebira)) +   "        ********** ")

    # print("  ***********    save_data_s   "  + (str)(save_format_data_perebora_files)  + "      ********** ")
    # print("  ***********           ********** ")
    # one_file_path = list_path_files[one_file_path]; print( one_file_path )

    # save_data_str = save_data.strftime('%Y, %m, %d, %H, %M')
    # print( save_data_str )
    # naw_data = datetime.strptime(may_datatime, "%Y, %m, %d, %H, %M") ; print( naw_data )

    if data_time_format_iz_perebira == save_format_data_perebora_files:

        # save_format_data_perebora_files = data_time_format_iz_perebira
        # print(" - ------------ -")
        # print(" - ДАТЫ РАВНЫ")
        # print(" - ------------ -")
        return 0

    elif data_time_format_iz_perebira > save_format_data_perebora_files:

        save_format_data_perebora_files = data_time_format_iz_perebira

        # print(" - ------------ -")
        # print(" - ДАТА БОЛЬШЕ")
        # print(" - ------------ -")
        return 1


    else:
        # print(" - ------------ -")
        # print(" - ДАТА  МЕНЬШЕ")
        # print(" - ------------ -")
        return 0


# посик и определене пути для самого обновлённого файла логов
def max_path_live():
    try:
        files = glob.glob(fr"{mypath_dir}/wc.north*")  # СПИСОК ПУТЕЙ ДО КАЖДОГО ПРЕДПОЛОГАЕМОГО ФАЙЛА где есть "wc.north*
        print(" string_1.py - >  def max_path_live(): " + str(files))
        # print(files)
        # print("                                      ")
        # print("                                      ")
        # print(  len(files) )  # ВСЕГО ФАЙЛОВ
        # list_path_files = files
        # print("                                      ")
        # print("                                      ")
        # print(max(files, key=os.path.getctime))
        # print(max(files, key=os.path.getatime))
        # print("                                     ")
        global path_live
        # path_live = max(files, key=os.path.getctime)
        # print(path_live)
        path_live = perebor_files(files)

        return path_live
    except:
        print(" string_1.py - >  max_path_live(): ОШИБКА !  ")

# Последняя строка
def last_line():
    try:

        with open(path_live, 'r', encoding='utf-16') as file:
            global last_line_text
            last_line_text = file.readlines()[-1]

        print("string_1.py -> def last_line(): -> last_line_text = " + last_line_text)
        # return last_line_text
    except:
        print(" !!!! вышло хреново в  string_1 ->  def last_line():  !!!! ")

    return last_line_text


# НУЖНАЯ строка
# def shouse_line_intel_stroka (nomer_stroki):
#     with open(path_live, 'r', encoding='utf-16') as file:
#         global last_line_text
#         last_line_text = file.readlines()[-1]
#     print("string_1.py -> def last_line(): -> last_line_text = " + last_line_text)
#     return last_line_text


# Количество строк, номер последней строки
def kol_strok():
    global num_posl_stroki_live_reed

    try:
        num_posl_stroki_live_reed = sum(1 for line in open(path_live, 'r', encoding='utf-16'))
        print("string_1.py -> def kol_strok(): -> num_posl_stroki_live_reed = " + (str(num_posl_stroki_live_reed)))
        # return num_posl_stroki_live_reed
    # try:
    #     open("path_live", "r")
    #     print("Файл открыт")
    # except IOError:
    #     print("Файл не открыт")

    except:
        print(" !!!! вышло хреново в  string_1 ->  kol_strok():  !!!! ")

    return num_posl_stroki_live_reed


def str_test(line_text):
    print("str_1: ")
    print(line_text)
    data_str = line_text[3:13]
    time_str = line_text[14:22]

    year_last = line_text[3:7]
    print("year = (" + year_last + ")")
    month_last = line_text[8:10]
    print("month = (" + month_last + ")")
    day_last = line_text[11:13]
    print("day = (" + day_last + ")")

    hour_last = line_text[14:16]
    print("hour_last = (" + hour_last + ")")
    min_last = line_text[17:19]
    print("min_last = (" + min_last + ")")
    sec_last = line_text[20:22]
    print("sec_last = (" + sec_last + ")")

    print("дата = (" + data_str + ")")
    print("время = (" + time_str + ")")
    data_time_str = data_str + " " + time_str
    print("data_time_str= " + data_time_str)
    global date_time_last
    # date_last = datetime.strptime("05-22-2017 12:30:00", "%m.%d.%Y %H:%M:%S")
    date_time_last = datetime.strptime(data_time_str, "%Y.%m.%d %H:%M:%S")

    print(date_time_last)


# дата и время из строки
def str_date(line_text):
    data_str = line_text[3:13]
    time_str = line_text[14:22]
    data_time_str = data_str + " " + time_str
    # print ("string_1.py -> def str_date(line_text): -> data_time_str = " + data_time_str )

    global date_time_last

    try:
        date_time_last = datetime.strptime(data_time_str, "%Y.%m.%d %H:%M:%S")
        # print("  вышло норм ")
    except ValueError:

        print(" !!!! вышло хреново !!!!         string_1.py ->  def str_date(line_text):")
        # date_time_last = datetime.strptime("2000.07.27 0:0:0", "%Y.%m.%d %H:%M:%S")
        # date_time_last = save_format_data_perebora_files

    # print("string_1.py -> def str_date(line_text): -> "  +  (str(date_time_last)  ))
    return date_time_last


# if last_line_text == "":
#     max_path_live()
#     last_line()
#     kol_strok()
#     # print("IF " + last_line_text)
#     str_date(last_line_text)

# else:
#     str_date(last_line_text)

def go():
    if last_line_text == "":
        max_path_live()
        last_line()
        kol_strok()
        # print("IF " + last_line_text)
        str_date(last_line_text)

    else:
        max_path_live()
        str_date(last_line_text)


def string_exit():
    print("string_exit()")
    quit()

    # return path_live, last_line_text, num_posl_stroki_live_reed, date_time_last


# go()


# # НУЖНАЯ строка
def shouse_line_intel_stroka(nomer_stroki):
    with open(path_live, 'r', encoding='utf-16') as file:
        global last_line_text
        last_line_text = file.readlines()[nomer_stroki]
    print("string_1.py ->         shouse_line_intel_stroka (nomer_stroki): -> last_line_text = " + last_line_text)
    return last_line_text


def kontrol_close_file():
    try:
        open("path_live", "r")
        # print("Файл открыт")
    except IOError:
        print("Файл не открыт")

# class Monkey(object):
#     def __init__(self):
#         self._cached_stamp = 0
#         self.filename = path_live

# def ook(self):
#         stamp = os.stat(self.filename).st_mtime
#         if stamp != self._cached_stamp:
#             self._cached_stamp = stamp
#             # File has changed, so do something...


# try:
#     with open("path_live", "r") as file:
# # Распечатать сообщение об успешном завершении
#      print("Файл открыт для чтения.")
# # Вызовите ошибку, если файл был открыт раньше
# except IOError:
#      print("Файл уже открыт")


# go()

# if num_posl_stroki_live_reed > 0  and num_posl_stroki_live_reed < 10:
# print("TEEEEST = " + shouse_line_intel_stroka(num_posl_stroki_live_reed-3))
# shouse_line_intel_stroka(num_posl_stroki_live_reed-10)


# try:
#     open("path_live", "r")
#     print("Файл открыт")
# except IOError:
#     print("Файл не открыт")


# try:
#     with open("path_live", "r") as file:
# # Распечатать сообщение об успешном завершении
#      print("Файл открыт для чтения.")
# # Вызовите ошибку, если файл был открыт раньше
# except IOError:
#      print("Файл уже открыт")
#      # open("path_live", "r").close()

# Функция Drfine проверяет, закрыт ли файл или нет

# def check_closed():
#     if file_xxx.closed == False:
#          # Распечатать сообщение об успешном завершении
#          print("Файл открыт для чтения.")
#     else:
#         # Распечатать сообщение об ошибке
#         print(" Файл закрыт.")
#
#
# file_xxx = open("path_live", "r")
# check_closed()
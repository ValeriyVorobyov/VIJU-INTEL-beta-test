from tkinter import *
from tkinter import ttk
import tkinter as tk
# from main import root

# class Global_setting_window(root.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         print(" Global_setting ")
#
#
# print(" global_setting() ")
# print(" root_x = " + str(root.winfo_x()) + "  root_y = " + str(root.winfo_y()))
#
# global_setting_window = Toplevel()
# global_setting_window.title(" Настройки ")
# w = 600
# h = 400
# x = root.winfo_x()+200
# y = root.winfo_y()+200
# global_setting_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
# global_setting_window.grab_set()
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
#


def glb_sett(root):
    print(" glb_sett(): ")
    # global_setting(root)
    print(" root_x = " + str(root.winfo_x()) + "  root_y = " + str(root.winfo_y()))
    #
    global_setting_window = Toplevel()
    global_setting_window.title(" Настройки ")
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
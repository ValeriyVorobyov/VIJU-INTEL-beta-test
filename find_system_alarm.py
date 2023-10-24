# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 21:29:41 2023

@author: V5
"""
import os
import save_settings
from datetime import datetime, timedelta


# СЛОВАРЬ СИСТЕМ СРАБАТЫВАНИЯ И ИХ ТАЙМЕРОВ  
timers_slovar = {}

# save_sistem_alarm = list()


# def find_alarm_system ( all_name_sistem, posl_stroka, kol_system ):
#     print("find_alarm_system")
    
#     for a1 in kol_system:
#          print(all_name_sistem[a1-1])
#          if all_name_sistem[a1-1] in posl_stroka:
#              print("~~~~~~~~~~~~~~~~~~~~~~~")
         
         
    # if list_system.append(canva_1.itemcget(elements, "tags")) in last_line_text:
    #           print("!!!!!!!!!!       Е С Т Ь              С О В П А Д Е Н И Е         !!!!!!!!!")
    

def add_alarm_timers (datatime, tag_system):
    print("------------------------------------")
    print("add_alarm_timers()")
    
    # проверка на наличие записи ключа(тега) сиситемы
    print("# проверка на наличие записи ключа(Tега) сиситемы = " + tag_system)
    
    if tag_system in timers_slovar:
            print("ЗАПИСЬ ECТЬ = " + tag_system + " : " + (str(timers_slovar[tag_system])))
            
            # Обновляем запись всёравно
            timers_slovar[tag_system] = datatime
          
        
            # если запись есть надо проверить сколько прошло времени с того момента и отреагировать на это
            sravnivaem_datatime (datatime, tag_system)
    
    else:
            print("ЗАПИСЕЙ ДЛЯ ДАННОЙ СИСТЕМЫ НЕ Найдено  - ДОбАВЛЯЕМ НОВЫЙ ТАЙМЕР и Систему как ключ")
            timers_slovar[tag_system] = datatime
            
            sravnivaem_datatime (datatime, tag_system)
            
            
    
    print("ИТОГОВЫЙ СЛОВАРЬ:" + (str(timers_slovar)))
    # print(timers_slovar)
    
    
def searh_alarm_timers (spisok_system_list):
    # print("------------------------------------")
    # print("searh_alarm_timers")
    # print("------------------------------------")
    
   
    
    
    # перебор списка систем и сравнивание со списком систем уже в алярме
    # for person in list_system:
    #     print(person)
    
    # for alarm_system_meyby in spisok_system_list:
       
    #     print(alarm_system_meyby)
    
        # key = "+4444444"
    for spisok_system_list in timers_slovar:
        
            # print (f"Sytem: {spisok_system_list}  Timer {timers_slovar[spisok_system_list]} ")
            return "ok"
            
    # print("ИТОГОВЫЙ СЛОВАРЬ:" + (str(timers_slovar)))
    # return timers_slovar
    # print("ИТОГОВЫЙ СЛОВАРЬ:")
    # print(timers_slovar)        
    
def peredaem_alarm_slovar():
    
    return timers_slovar        
  
            
    
def del_system_alarm(systema_alarm_tag):
    
    if systema_alarm_tag in timers_slovar:
       del timers_slovar[systema_alarm_tag]
       print(f"Элемент с ключом {systema_alarm_tag} удален")
    else:
       print("Элемент не найден при попытки удалить из словаря систему  " + systema_alarm_tag )
        
   
    
   
    
        
        
    
def sravnivaem_datatime (may_datatime, tag_system):
    print("  ******  def sravnivaem_datatime ********** ")
    
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
        
        if i <= 6: return 0
        elif i > 6 and i < 9: return 1
        elif i >= 9 and i < 17: return 2
        elif i >= 17 and i < 25: return 3
        elif i >= 25: 
            del_system_alarm(tag_system)
            return 4
        
        
        
        
        # ДЛя ТЕСТОВ
        # if i <= 1: return 0
       
        # elif i >= 2: 
            
        #     del_system_alarm(tag_system)
                              
            
        #     return 4
    

        
    
    
# def searh_alarm_timers (datatime, tag_system):
#     print("searh_alarms_timer ():")
    
#     # проверка на наличие записи ключа(тега) сиситемы
#     print("# проверка на наличие записи ключа(Tега) сиситемы")
    
#     if tag_system in timers_slovar:
#         print("ЗАПИСЬ ECТЬ = ")
#         print(timers_slovar[tag_system])
        
#         # если запись есть надо проверить сколько прошло времени с того момента и отреагировать на это
        
    
#     else:
#         print("ЗАПИСЕЙ ДЛЯ ДАННОЙ СИСТЕМЫ НЕ Найдено ")
        
def add_green_timers (datatime, tag_system):
    print("------------------------------------")
    print("     add_green_timers()       ")
    print("------------------------------------")
     
    # проверка на наличие записи ключа(тега) сиситемы
    print("# проверка на наличие записи ключа(Tега) сиситемы = " + tag_system)
    
    if tag_system in timers_slovar:
            print("ЗАПИСЬ ECТЬ = " + tag_system + " : " + (str(timers_slovar[tag_system])))
            
            # Обновляем запись всёравно
            timers_slovar[tag_system] = datatime
          
        
            # если запись есть надо проверить сколько прошло времени с того момента и отреагировать на это
            sravnivaem_datatime (datatime, tag_system)
    
    else:
            print("ЗАПИСЕЙ ДЛЯ ДАННОЙ СИСТЕМЫ НЕ Найдено  - ДОбАВЛЯЕМ НОВЫЙ ТАЙМЕР и Систему как ключ")
            timers_slovar[tag_system] = datatime
            
            sravnivaem_datatime (datatime, tag_system)
            
            
    
    print("ИТОГОВЫЙ СЛОВАРЬ:" + (str(timers_slovar)))
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
            # del_system_alarm(tag_system)
            return 4            
    
    
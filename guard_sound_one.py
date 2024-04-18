"""

Для добавления систем по одной, на которых должно быть звуковое оповещение

"""
guard_set_system_sound_one = set()


def get_guard_set_system_sound_one():
    return guard_set_system_sound_one


# обработка клика по системе
def click_guard_system_sound_one(systema):

    if systema in guard_set_system_sound_one:
        # i = guard_list_system_sound_one.index(systema)
        # print("Найдена Система (" + str(guard_list_system_sound_one[i]) + ") с индексом = " + str(i))
        print("Найдена Система (" + systema + ")  - УДАЛЯЕМ !")
        guard_set_system_sound_one.remove(systema)
        return 1
    else:
        guard_set_system_sound_one.add(systema)
        print("Системы " + systema + " нет, ДОБАВЛЯЕМ")
        return 0
#
# def add_guard_set_system_sound_one(systema):
#
#     print("!!!!!! MODULE:  add_guard_sound_one  !!!!!")
#
#     # print("add_sound_system(system, distance): ")
#
#     guard_set_system_sound_one.add(systema)
#     # save_guard_list_system_sound.add(system)
#
#     # print(save_guard_list_system_sound)
#     print("guard_list_system_sound_one = " + str(guard_set_system_sound_one))
#
#     # return save_guard_slovar_sound, save_guard_list_system_sound
#
# def del_guard_set_system_sound_one(systema):
#
#     pass
#
#     # поиск системы на удаление
#     # for reed_systema in guard_list_system_sound_one:
#     #     print(reed_systema)

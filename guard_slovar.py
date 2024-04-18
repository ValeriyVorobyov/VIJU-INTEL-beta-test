



save_guard_slovar_sound = {}  # типа система:дистанция за которыми надо следить
guard_list_system_sound = list()
alarm_sound_system = list()
test_slovar_napravlenya = {}
test_slovar_put = {}

test_set_napravlenya = set()
test_set_put = set()
test_list_put = list()
test_list_put_ok = list()

system_check_ok = set()
gate_check_ok = set()

vetv_list_ok = list()





system_alarm = "QYZM-W"
key_save=0







def poisk_1(list_all_guard, guard_system, distance_1):
    print("____def poisk_1(guard_system, list_all_guard, distance_1): ")

    global put_number, put_guard, gate_list
    put_number = list()
    put_guard = list()
    gate_list = list()

    # global gate_list

    # guard_system = "QYZM-W"
    # system_alarm = "QYZM-W"
    global list_all_guard_set
    list_all_guard_set = list_all_guard
    system_check_ok.clear()
    system_check_ok.add(guard_system)

    gate_check_ok.add(guard_system)



    for system_poisk in list_all_guard:

        if guard_system in system_poisk[0:6]:

            put_guard.clear()
            put_number.clear()



            # put_guard.append(str(guard_system))

            print("system_poisk = " + system_poisk)  # Найдена охраняемая система в общем списке
            gate_string = system_poisk.split()  # количество(-1) гейтов в системе. В листе отсчёт с 0, а там имя самой системы, остальное гейты
            # print("гейтов в ссистеме " + str(system_test[0:6]) + " = " + str(len(test_string)-1))

            gate = 1
            gate_list = list()  # в листе отсчёт с 0, а там имя самой системы, остальное гейты
            while gate < len(gate_string):
                # print(test_string[gate])
                gate_list.append(str(gate_string[gate]))

                gate += 1
                # print(gate_list)
            # print("гейтов в ссистеме " + str(system_poisk[0:6]) + " = " + str(len(gate_string) - 1) + "  " + str(gate_list))
            print("В ссистеме " + str(system_poisk[0:6]) + ", найдено " + str(gate - 1) + " гейта: " + str(gate_list))

            put_number.append(system_poisk[0:6])

            # test_slovar_napravlenya[str(1)] = gate_list

            #
            # проверяем пути через найденные гейты поочерди
            # гейты ведут в всистемы в 1 прыге от охраняемой системы,
            # поэтому проверям сначала наличия там врага
            # !!!!!!!!!!!  тут же разветление на 2 пути (сколько гейтов) !!!!!! ещё не продумал !!
            print(len(gate_list))
            print("проверяем дистанцию на 1 прыге")
            gate_one = 0
            while gate_one < len(gate_list):
                i = poisk_vraga_v_gates(gate_list[gate_one])


                if i == 0:
                    return 0
                gate_one += 1
            # cистемы гейтов проверены
            # put_number.append(put_guard)
            print("put_number =  " + str(put_number))
            # Ecли дистанция больше 1 то проверяем каждый гейт дальше

            distance_2 = 2
            print(str(distance_2) + " < " + str(distance_1))

            # test_slovar_napravlenya[str(distance_2)] = gate_list
            prig = 0

            print("test_slovar_napravlenya = " + str(test_slovar_napravlenya))
            print("test_slovar_put = " + str(test_slovar_put))



            # elif distance_1 > distance_2:
            #     distance_2 = 3
            #     print("проверяем дистанцию на " + str(distance_2) + " прыге")
            #     print("test_slovar_napravlenya = " + str(test_slovar_napravlenya))
            #     print("test_slovar_put = " + str(test_slovar_put))



            while distance_2 < distance_1+1:
                # print("проверяем дистанцию на " + str(distance_2) + " прыге")

                # test_slovar_napravlenya[distance_2] = gate_list
                # print("test_slovar_napravlenya = " + str(test_slovar_napravlenya))


                print("--@@@@@@@@@---  проверяем дистанцию на " + str(distance_2) + " прыге")
                print("--@@@@@@@@@---  gate_list(): " + str(gate_list))

                poisk_vraga_v_bolee_2x_prigax(gate_list, distance_2)

                    # print("test_slovar_napravlenya = " + str(test_slovar_napravlenya))



                # poisk_vraga_v_bolee_2x_prigax(gate_list, distance_2)
                # print("put_number =  " + str(put_number))
                distance_2 += 1



def poisk_vraga_v_gates(gate):

    # print("def poisk_vraga_v_gates(gate):: " + str(gate))
    # print("def poisk_vraga_v_gates(gate)::  system_alarm ==" + str(system_alarm) + "  gate ==" + str(gate))


    if system_alarm == gate:
        # print("def poisk_vraga_v_gates(gate):  ( " + str(system_alarm) + " ) == ( " + str(gate) + " )")
        print("____def poisk_vraga_v_gates(gate): ECТЬ ВРАГ в " + str(gate))

        return 0
    else:
        # print("def poisk_vraga_v_gates(gate):  ( " + str(system_alarm) + " ) == ( " + str(gate) + " )")
        print("____def poisk_vraga_v_gates(gate): НЕТ ВРАГА в " + str(gate))
        system_check_ok.add(gate)
        return 1

def poisk_vraga_v_bolee_2x_prigax(gate_list, distance_2):

    global test_slovar_put_one, test_slovar_put
    global key_save


    print("____def poisk_vraga_v_bolee_2x_prigax(): " + str(len(gate_list)) + " " + str(gate_list))
    print("distance_2: " + str(distance_2))
    # print(" gate_list[" + str(0) + "] = " + str(gate_list[0]))

    print("test_slovar_napravlenya = " + str(test_slovar_napravlenya))
    for key in test_slovar_napravlenya:
        print(f"(test_slovar_napravlenya) Прыги(key): {key}  Гейты: {test_slovar_napravlenya[key]} ")

    print("test_slovar_put = " + str(test_slovar_put))

    # test_list_put_key_local = list()
    # for key in test_slovar_put:
    #     print(f"(test_slovar_put) Прыги(key): {key}  Гейты: {test_slovar_put[key]} ")
    #     test_list_put_key_local.append(key)

    for key, value in test_slovar_put.items():
        print(f"key: {key}  value: {value} ")
        print(type (value))

    if len(test_slovar_put) > 0:
        print(" len(test_slovar_put) = " + str(len(test_slovar_put)) + " > 0: ")

        save_long_put = len(test_slovar_put)


        # print("  len test_slovar_put_key_local = " + str(len(test_list_put_key_local)) + " > 0: ")
        # # gate_list_1 = list()
        # for key in test_list_put_key_local:
        #     print(f"key in test_slovar_put_key_local:: {key}   ")
        # for key in vetv_list_ok:
        #     print(f"  vetv_list_ok:: {key}   ")

        print(" gate_check_ok = " + str(gate_check_ok))


        # number = 1
        # while number < len(test_slovar_put_key_local):
        #     print(f"number = {number}")
        #     gate_list_1 = g_list(test_slovar_put[test_slovar_put_key_local[number]])
        #     check_gate_list(gate_list_1)
        #     number += 1
        # test_slovar_put_key_local.clear()
        print(" key_save = " + str(key_save))
        key_int = 1
        for key, value in list(test_slovar_put.items()):
            print(f"ffffffffffffffff key: {key}  value: {value} ")
            print(" key_int = " + str(key_int))
            print(" key_save = " + str(key_save))

            if key_int > key_save:

                for key_gate in gate_check_ok:
                    print(f"  gate_check_ok :: {key_gate}   ")

                gate_list_1 = g_list(test_slovar_put[key])
                check_gate_list(gate_list_1)


            key_int += 1


    else:
        for key in gate_check_ok:
            print(f"  gate_check_ok :: {key}   ")
        check_gate_list(gate_list)





def check_gate_list(gate_list):
    print("____def check_gate_list(): " + str(gate_list))


    i_gate = 0
    while i_gate < len(gate_list):
        print(" gate_list[" + str(i_gate) + "] = " + str(gate_list[i_gate]))
        put_guard.append(gate_list[i_gate])

        # test_slovar_napravlenya[distance_2] = gate_list
        # print("test_slovar_napravlenya = " + str(test_slovar_napravlenya))

        test_set_napravlenya = gate_list
        print("test_set_napravlenya = " + str(test_set_napravlenya))

        print(" put_number = " + str(put_number))
        print(" put_guard = " + str(put_guard))

        gate_check_ok.add(gate_list[i_gate])

        poisk_geytov_v_system(gate_list[i_gate])

        i_gate += 1



def poisk_geytov_v_system(system_search):

    print("____def poisk_geytov_v_system(system_search):")

    # global list_all_guard_set
    # global gate_list

    # print(list_all_guard_set)
    global test_slovar_napravlenya

    for system_poisk in list_all_guard_set:

        if system_search in system_poisk[0:6]:

                print(system_poisk)  # или просто система, в которой надо найти гейты ; Найдена охраняемая система в общем списке

                gate_string = system_poisk.split()  # количество(-1) гейтов в системе. В листе отсчёт с 0, а там имя самой системы, остальное гейты
                # print("гейтов в ссистеме " + str(system_test[0:6]) + " = " + str(len(test_string)-1))
                gate = 1
                gate_list = list()  # в листе отсчёт с 0, а там имя самой системы, остальное гейты
                while gate < len(gate_string):
                    # print(test_string[gate])
                    gate_list.append(str(gate_string[gate]))
                    gate += 1
                    # print(gate_list)

                print("В ссистеме " + str(system_poisk[0:6]) + ", найдено " + str(gate - 1) + " гейта: " + str(gate_list))
               # проверяем наличия врагов в найденыйх гейтах
                gate_list = del_nenujniy_gate(gate_list)
                print(" gate_list = " + str(gate_list))

                # test_slovar_napravlenya[system_poisk[0:6]] = gate_list
                test_slovar_put[system_poisk[0:6]] = gate_list
                vetv_list_ok.append(system_poisk[0:6])
                print("test_slovar_put = " + str(test_slovar_put))
                print(" len(test_slovar_put) = " + str(len(test_slovar_put)))
                print("test_slovar_napravlenya = " + str(test_slovar_napravlenya))



                gate_one = 0
                while gate_one < len(gate_list):
                    i = poisk_vraga_v_gates(gate_list[gate_one])
                    if i == 0:
                        return 0
                    gate_one += 1
                # cистемы гейтов проверены




def del_nenujniy_gate(gate_list):

    print("____def del_nenujniy_gate():")

    print("____def del_nenujniy_gate(): put_number = " + str(put_number))
    print("____def del_nenujniy_gate(): gate_list = " + str(gate_list))
    print("____def del_nenujniy_gate(): system_check_ok = " + str(system_check_ok))
    print("____def del_nenujniy_gate(): gate_check_ok = " + str(gate_check_ok))

    local_del_set = set()

    for system in gate_list:
        for system_gate in gate_check_ok:
            # print("____system = " + str(system))
            # print("____system_gate = " + str(system_gate))
            if system == system_gate:
                print("____ IF system(" + str(system) + ") = (" + str(system_gate) + ") ")
                print("!!! DEL gate !!! in  gate_list = " + str(gate_list[gate_list.index(system_gate)]))
                local_del_set.add(gate_list[gate_list.index(system_gate)])

    for del_system in local_del_set:
        del gate_list[gate_list.index(del_system)]

    local_del_set.clear()




                # for system in system_check_ok:




    print("____def del_nenujniy_gate(): return gate_list = " + str(gate_list))
    return gate_list


def g_list(list_list):
    print("____def g_list(): list_list= " + str(list_list))
    print("____def g_list(): gate_list= " + str(gate_list))

    gate = 0
    # gate_list.clear()
    new_list = list()

    while gate < len(list_list):
        # print(test_string[gate])
        print("____def g_list(): list[" + str(gate) + "] = " + str(list_list[gate]))
        new_list.append(str(list_list[gate]))

        gate += 1
        # print(gate_list)
    print("____def g_list(list): return gate_list = " + str(new_list))
    return new_list




        # if str(system) in list_all_guard:
        #    print( list_all_guard[ str(system) ] )
        # for system





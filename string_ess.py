# Проверка строки на наличие в ней слов ESS, ess, Ess итд..
# и чтобы они не были в составе ник нейма персонажа
# кстате наверно проще добалять поразитирующие на этом ники в список исключения,
# прям в программе предусмотреть

# Используйте метод str.isspace():
# Возвращает, True если в строке есть только символы пробела и есть хотя бы один символ, False в противном случае.

list_ess = {"ess", "ESS", "Ess", "ESs", "Есс", "Еss"}


def ess_check(string):

    for n in list_ess:

        if string.endswith(n):

            if string[len(string)-4].isspace():
                # print("--ОК")
                return 1
        else:
            if ess_check_0(string, n) == 1:
                # print("--ОК-2")
                return 1


def ess_check_0(string: str, check: str):

    index = string.find(check)

    if index == -1:
        # print(index)
        pass

    else:
        # print(index)
        # print(string[index - 1])
        # print(string[index + 3])
        # print("длинна = " + str(len(string)))
        # l = len(string) - 4
        # print(string[l])

        # if string[l].isspace():
        #     print("ОК")

        if string[index - 1].isspace() and string[index + 3].isspace():
            # print("ОК-1")
            return 1

        else:
            index = string.rfind(check)
            # print("index = " + str(index))

            if string[index - 1].isspace() and string[index + 3].isspace():
                # print("ОК-2")
                return 1


# END


# if ess_check("bu listress ess ") == 1:
#     print("ОООООКККК")


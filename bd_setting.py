import sqlite3


# pach_bd_setting = "bd_setting.db"
# pach_bd_sound_one = "bd_sound_one.db"

def create_bd_all(path_setting, path_sound):
    create_base_setting(path_setting)
    create_base_sound_one(path_sound)

def create_base_setting(path_setting):

    baza = sqlite3.connect(path_setting)
    cursor = baza.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS my_setting
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    text1 TEXT, 
                    text2 TEXT);
                """)
    print("База данных 'my_setting' подключена к SQLite")
    print("Таблица SQLite создана")
    # cursor.close()
    baza.commit()
    cursor.close()
    baza.close()

def create_base_sound_one(path_sound):

    baza = sqlite3.connect(path_sound)
    cursor = baza.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS my_sound_one
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    text1 TEXT, 
                    text2 TEXT);
                """)
    print("База данных 'my_sound_one' подключена к SQLite")
    print("Таблица SQLite создана")
    # cursor.close()
    baza.commit()
    cursor.close()
    baza.close()







# ЕСЛИ НЕ СУЩЕСТВУЕТ  = IF NOT EXISTS








# добавляем строку в таблицу people
# cursor.execute("INSERT INTO people (text1, text2) VALUES ('fon_color', 38)")


# обновляем строки, где name = Tom
# cursor.execute("UPDATE people SET name ='Tomas' WHERE name='Tom'")

# вариант с подстановками
# cursor.execute("UPDATE people SET name =? WHERE name=?", ("Tomas", "Tom"))
# baza.commit()
# cursor = baza.cursor()
# перебор базы
# con = sqlite3.connect(pach_bd)
# cursor = con.cursor()
# for person in cursor:
#     print(" *****************    SQL3           ***********")
#     print(f"{person[1]} - {person[2]}")
#
# records = cursor.fetchall()
# print("Всего строк:  ", len(records))
# cursor.close()


def add_fon_color(set_color: str):

    print("def add_fon_color(set_color):  " + set_color)
    # данные для добавления
    fon = ("fon_color", str(set_color))
    baza = sqlite3.connect("bd_setting.db")
    cursor = baza.cursor()
    records = cursor.fetchall()

    update_query = """Update my_setting set text1 = ?, text2 = ?"""
    column_values = ("fon_color", set_color)
    cursor.execute(update_query, column_values)
    baza.commit()
    cursor.close()
    baza.close()


def save_update_to_base(path_bd_setting, text1: str, text2: str):
    """
    Сохраняем данные в базе.

    """
    conn = sqlite3.connect(path_bd_setting)
    cur = conn.cursor()
    # cur.execute('BEGIN TRANSACTION')
    if check_base_setting(path_bd_setting,text1) == 0:
        cur.execute("INSERT INTO my_setting (text1, text2) VALUES(?, ?)", (text1, text2))
    else:
        cur.execute("UPDATE my_setting SET text2 = ?  WHERE text1 = ?", (text2, text1))
    conn.commit()
    cur.close()
    conn.close()


def open_base(path_bd_setting) -> list:
    """
    Открытие базы данных.
    :param path: Путь к базе данных.
    :return: Список с выборкой названий всех документов в базе.
    """
    conn = sqlite3.connect(path_bd_setting)
    cur = conn.cursor()
    cur.execute("SELECT text1, text2 FROM my_setting")
    data = cur.fetchall()
    sql = "SELECT COUNT (*) FROM my_setting"
    cur.execute(sql)
    results = cur.fetchall()
    print("Всего строк:  " + str(results))
    # print(results)
    cur.close()
    conn.close()
    return data


def check_base_setting(path_bd_setting, text1: str):
    conn = sqlite3.connect(path_bd_setting)
    cur = conn.cursor()
    # cur.execute("SELECT text1, text2 FROM my_setting")

    info = cur.execute('SELECT * FROM my_setting WHERE text1=?', (text1,))

    if info.fetchone() is None:
        print("Записи нет")
        cur.close()
        conn.close()
        return 0

    else:
        print("Запись " + text1 + " есть: " + str(info))
        cur.close()
        conn.close()
        return 1


def reed_base_setting(path_bd_setting, text1: str):
    conn = sqlite3.connect(path_bd_setting)
    cur = conn.cursor()
    # cur.execute("SELECT text1, text2 FROM my_setting")
    reed = cur.execute('SELECT * FROM my_setting WHERE text1=?', (text1, ))
    results1 = reed.fetchall()
    # reed = cur.fetchone()
    print("reed_base_setting = " + str(results1))
    return results1[0][2]


def save_del_to_base_sound_one(path_bd_sound_one, text1: str):
    print(" *******  def save_del_to_base_sound_one: ************")
    """
    Сохраняем данные в базе.

    """
    # text2 = pickle.dumps(event)
    conn = sqlite3.connect(path_bd_sound_one)
    cur = conn.cursor()
    # cur.execute('BEGIN TRANSACTION')
    if check_base_sound_one(path_bd_sound_one, text1) == 0:
        # cur.execute("INSERT INTO my_sound_one (text1, text2) VALUES(?, ?)", (text1, "1"))
        cur.execute("INSERT INTO my_sound_one (text1) VALUES(?)", (text1, ))
    else:
        cur.execute("DELETE FROM my_sound_one WHERE text1 = ?", (text1, ))
    conn.commit()
    cur.close()
    conn.close()


def check_base_sound_one(path_bd_sound_one, text1: str):
    print(" *******  def scheck_base_sound_one ************")
    conn = sqlite3.connect(path_bd_sound_one)
    cur = conn.cursor()
    # cur.execute("SELECT text1, text2 FROM my_setting")

    info = cur.execute('SELECT * FROM my_sound_one WHERE text1=?', (text1,))

    if info.fetchone() is None:
        print("Записи (" + text1 + ") нет")
        cur.close()
        conn.close()
        return 0

    else:
        print("Запись (" + text1 + ") есть")
        cur.close()
        conn.close()
        return 1


def reed_base_sound_one(path_bd_sound_one) -> list:
    conn = sqlite3.connect(path_bd_sound_one)
    cur = conn.cursor()
    # cur.execute("SELECT text1, text2 FROM my_setting")
    reed = cur.execute('SELECT text1 FROM my_sound_one')
    results1 = reed.fetchall()
    data = cur.fetchall()
    sql = "SELECT COUNT (*) FROM my_sound_one"
    cur.execute(sql)
    results = cur.fetchall()
    print("base_sound_one Всего строк:  " + str(results))
    # reed = cur.fetchone()
    # print("reed_base_my_sound_one = " + str(results1))
    # return results1[0][2]
    return results1


def reed_base_sound_one_column(path_bd_sound_one):
    conn = sqlite3.connect(path_bd_sound_one)
    cur = conn.cursor()
    # cur.execute("SELECT text1, text2 FROM my_setting")
    reed = cur.execute('SELECT text1 FROM my_sound_one')
    results1 = reed.fetchall()
    data = cur.fetchall()
    sql = "SELECT COUNT (*) FROM my_sound_one"
    cur.execute(sql)
    results = cur.fetchall()
    print("base_sound_one Всего строк:  " + str(results))
    # reed = cur.fetchone()
    # print("reed_base_my_sound_one = " + str(results1))
    # return results1[0][2]
    return results

# create_base()

# check_base_setting("fon_color")

#
# save_del_to_base_sound_one("qqqq")
# print(str(reed_base_sound_one()))


# save_to_base("fon_color", "#333444444455")

# print(str(open_base()))



    # cursor.execute("INSERT INTO my_setting (text1, text2) VALUES (?, ?)", fon)

    # print("Всего строк:  ", len(records))
    # baza.close()

    # if records == 0:
    #     baza = sqlite3.connect("bd_setting.db")
    #     cursor = baza.cursor()
    #     print("Добавляем фон колор  ")
    #     cursor.execute("INSERT INTO my_setting (text1, text2) VALUES (?, ?)", fon)
    #     baza.commit()
    #     baza.close()



    # cursor.execute("SELECT * FROM my_setting")
    # for person in cursor.fetchall():
    #     print(f"{person[1]} - {person[2]}")

    # cursor.execute("SELECT text1, atext2 FROM my_setting WHERE text1="fon_color"")




    # cursor.execute("UPDATE my_setting SET text1 =? WHERE text1=?", (str(set_color), "fon_color"))
    # cursor.close()



















# try:
#     baza = sqlite3.connect("bd_setting.db")
#     cursor = baza.cursor()
#
#     cursor.execute("""CREATE TABLE IF NOT EXISTS my_setting
#                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     text1 TEXT,
#                     text2 TEXT)
#                 """)
#     print("База данных подключена к SQLite")
#     print("Таблица SQLite создана")
#     # cursor.close()
#     baza.commit()
#
#
#
# except sqlite3.Error as error:
#     print("Ошибка при подключении к sqlite", error)
# finally:
#     if (baza):
#         baza.close()
#         print("Соединение с SQLite закрыто")
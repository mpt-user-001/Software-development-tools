import time as t

import BD
import Main
import animation
import os


def register():
    login = input("Введите номер телефона (79123456789): ")
    password = input("Введите пароль (Aqr90_): ")
    record = BD.Row("Player", login, "S")
    if record:
        print("\nТакой логин есть.")
        t.sleep(2)
        os.system('cls')
        register()
    BD.Row("Player", [login, password], "I")
    animation.progbar3()
    t.sleep(2)
    Main.menu(login)


def authorisation():
    login = input("Введите номер телефона: ")
    password = input("Введите пароль: ")
    record = BD.Row("Player", login, "S")
    animation.progbar2()
    os.system('cls')  
    if not record:
        print("Нет таких данных")        
        t.sleep(2)
        os.system('cls')        
        authorisation()
    else:
        for row in record:
            password_real = record[0]
            if password == password_real[2]:
                Main.menu(login)
            else:
                os.system('cls')
                print("Не правильный пароль")                
                t.sleep(2)
                os.system('cls')
                authorisation()
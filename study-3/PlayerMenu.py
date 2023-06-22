import time as t

import Cheque
import keyboard

import BD
import Main
import os
import pick
import random

selected = 1
global record, rows, logs


def buy_component(_log):
    global record, rows, logs
    logs = _log
    titles = 'Еда: '
    options = ['Выйти']
    for row in BD.Row("Dish", [], "S"):
        options.append(row[1])
    option, index = pick.pick(options, titles, indicator='=>')
    if index == 0:
        Main.menu(logs)
    rows = BD.Row("Component", option, "S")
    record = list(BD.Row("Component", [], "S"))
    i = 0
    for ij in record:
        try:
            record[i] = list(record[i])
            tec = record[i]
            tec[2] = 0
            j = 0
            for jj in rows:
                lec = list(rows[j])
                lec = rows[j]
                if lec[0] == tec[0]:
                    tec[2] = lec[2]
                j += 1
            i += 1
        except:
            titles = 'Еда: '
    component()


def component():
    os.system('cls')
    show_menu()
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.add_hotkey('right', right)
    keyboard.add_hotkey('left', left)
    keyboard.add_hotkey('enter', enter)
    keyboard.wait()


def show_menu():
    global selected, record
    os.system('cls')
    print("Ингридиенты:")
    print("Кошелёк: " + str(balance()))
    print()
    for i in range(len(record)):
        print("{0} {2} {3} {1}".format(">" if selected == i else " ", "<" if selected == i else " ", record[i][1],
                                       record[i][2]))
    print()
    print("Цена: " + str(sam()))


def up():
    global selected
    if selected == 0:
        return
    selected -= 1
    show_menu()


def down():
    global selected, record
    if selected == len(record) - 1:
        return
    selected += 1
    show_menu()


def right():
    global record, selected
    record[selected] = list(record[selected])
    tec = record[selected]
    if tec[2] < tec[4]:
        tec[2] += 1
    show_menu()


def left():
    global record, selected
    record[selected] = list(record[selected])
    tec = record[selected]
    if tec[2] > 0:
        tec[2] -= 1
    show_menu()


def enter():
    global record, logs
    sam_ = sam()
    bal = balance()
    if bal >= sam:
        full = 0
        ran = random.randint(0, 100)
        if ran == 3:
            full = bal / 100 * 30
            print("Попался глаз. Скидка 30%")
            t.sleep(2)
        bal -= (sam_ - full)
        BD.UpdateBalance(logs, sam_)
        BD.UpdateSkald(record)
        t.sleep(6)
        Cheque.cheque(record, sam_)
        Main.menu(logs)
    else:
        print()
        print("Недостаточно денег: " + str(sam() - balance()))
        t.sleep(3)
        show_menu()


def sam():
    global record
    sam_ = 0
    for i in range(len(record)):
        record[i] = list(record[i])
        tec = record[i]
        sam_ += tec[3] * tec[2]
    return sam_


def balance():
    global login
    row_player = BD.Row("Player", login, "S")
    row_player = row_player[0]
    return row_player[4]

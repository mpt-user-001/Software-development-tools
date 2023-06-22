import QR
import os


def add(log):
    os.system('cls')
    _sum = int(input("Введите сумму (100-700)"))
    if _sum > 99:
        if _sum < 701:
            QR.reg(log)
            QR.auto(log,_sum)
        else:
            add(log)
    else:
        add(log)
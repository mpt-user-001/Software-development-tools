sign = input("Знак (+,-,//,/,%,*,^): ")


def math(number1, number2):
    match sign:
        case '+':
            result = number1 + number2
            print(number1, sign, number2, "=", result)
        case '-':
            result = number1 - number2
            print(number1, sign, number2, "=", result)
        case '%':
            result = number1 % number2
            print(number1, sign, number2, "=", result)
        case '/':
            result = number1 / number2
            print(number1, sign, number2, "=", result)
        case '^':
            result = number1 ** number2
            print(number1, sign, number2, "=", result)
        case '//':
            result = number1 // number2
            print(number1, sign, number2, "=", result)
        case '*':
            result = number1 * number2
            print(number1, sign, number2, "=", result)
    return result


amount = int(input("Количество: "))
numberOne = float(input("Число: "))
numberTwo = float(input("Число: "))
i = 1
if amount > 0:
    if amount == 1:
        while i < amount + 1:
            i += 1
            if (sign == '//' or sign == '/' or sign == '%') and numberTwo != 0:
                numberOne = math(numberOne, numberTwo)
            elif sign == '+' or sign == '-' or sign == '*' or sign == '^':
                numberOne = math(numberOne, numberTwo)
            else:
                i -= 1
                numberOne = float(input("Число: "))
                numberTwo = float(input("Число: "))
                sign = input("Знак (+,-,//,/,%,*,^): ")
    elif amount > 1:
        if (sign == '//' or sign == '/' or sign == '%') and numberTwo != 0:
            numberOne = math(numberOne, numberTwo)
        elif sign == '+' or sign == '-' or sign == '*' or sign == '^':
            numberOne = math(numberOne, numberTwo)
        else:
            i -= 1
        while i < amount:
            i += 1
            numberTwo = float(input("Число: "))
            sign = input("Знак: ")
            if (sign == "//" or sign == '/' or sign == '%') and numberTwo != 0:
                numberOne = math(numberOne, numberTwo)
            elif sign == '+' or sign == '-' or sign == '*' or sign == '^':
                numberOne = math(numberOne, numberTwo)
            else:
                i -= 1
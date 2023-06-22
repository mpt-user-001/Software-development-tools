def math(x):
    result = 0
    for i in range(1, x + 1):
        result += i % 10 + i // 10
    return result


days = 0
year = -1

while year < 0:
    year = int(input("Год: "))

days += math(31) * 7

if year % 4 == 0 and year // 100 % 4 == 0:
    days += math(29)
else:
    days += math(28)

days += math(30) * 4

print("Итого: " + str(days))
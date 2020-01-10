"""
Определить, какой тип будет иметь результат операции (переменная c)
"""
a = 3
b = 4
c = a / b

print(type(c))

"""
Посчитать сумму чисел от 1 до 100
"""
n = 100
summa = 0
for i in range(n+1):
    summa += i
print(summa)


"""
Проверить, что число является четным
"""
number = 4
if number % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")
"""
Будет ли работать данный код?
name = "Svetozar"
age = 24
name_and_age = name + age
"""
# нет

"""
Проверить, если ли заданное число в списке
"""
number = 3
data = [1, 4, 2]
for i in data:
    if number == i:
        print(True)
    else:
        print(False)

"""
Написать функцию, которая проверяет, делится ли одно число на другое без остатка
"""
a = 5
b = 5
res = a % b
def proverka(res):
    if res == 0:
        return True
    else:
        return False
print(proverka(res))


def isDividable(a, b):
    return a % b == 0

print(isDividable(6, 2))




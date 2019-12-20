import value as value

a = 10
b = 20
values = [x ** 2 for x in range(a, b + 1)]
print(values)

# values = []
# for x in range(a, b + 1):
#     values.append(x ** 2)

print(x for x in range(a, b + 1))


values = [x for x in values if x % 2 == 0]
print(values)

values = [100 if x < 200 else 400 for x in values]
print(values)


# сгенерировать список степеней двойки от 0 до n
n = 20
values = [2 ** i for i in range(n)]
print(values)

# оставить в списке только строки полностью в верхнем регистре
values = ['Привет', 'как', 'ДЕЛА']
# upper_case = value.upper()
values = [x for x in values if x == x.upper()]
values = [x for x in values if x.isupper()]
print(values)


# список списков

n = 4
m = 5
data = [[0 for y in range(m)] for x in range(n)]
print(data)

for row in data:
    for element in row:
        print(element, end=' ')
    print()
print()

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=' ')
    print()
print()



first = [1, 2, 3]
second = [4, 5, 6]
result = [x + y for x in first for y in second]
print(result)
print()

a = 12
b = 23
maximum = b if b > a else a # тернарные операции

# сгенерировать список вида [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,...]






# дано число n, сгенерировать таблицу умножения nxn и сохранить в список

n = 10
data = [[0 for y in range(n)] for x in range(n)]

for row in range(len(data)):
    for column in range(len(data[row])):
        data[row][column] = (row + 1) * (column + 1)
        print(data[row][column], end=' ')
    print()
print()



# сгенерировать поле для игры в "Сапер"
# [[0, -1, 0],
#  [0, 0, 0],
#  [-1, 0, 0]]






# Напечатать табличку змейкой
# лано N
# 1 2 3
# 6 5 4
# 7 8 9



# напечатать табличку "спиралью"
# 1 2 3
# 8 9 4
# 7 6 5
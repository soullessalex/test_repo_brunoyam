#import value as value
from typing import List

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

n = 10
values = [x for x in range(n) for i in range(x)]
print(values)
values = []
n = 10
for x in range(n):
    for i in range(x):
        values.append(x)
print(values)

values = []
for k in range(1, n + 1):
    # for i in range(k):
    #     values.append(k)
    values += [k] * k
print(values)



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

n = 5
m = 5
bomb = 9
data = [[0 for i in range(n)] for j in range(m)]
data[0][1] = bomb
data[2][3] = bomb
data[2][1] = bomb
x = 1
y = 1
data.insert(0, [0] * (n+2)) # строчка в начале
data.append([0] * (n + 2)) # строчка в конце
for i in range(1, m + 1): # строки между
    data[i].append(0)
    data[i].insert(0, 0)
# print(data)
# for row in data:
#     for element in row:
#         print(element, end=' ')
#     print()
# print()
# смещаем точку в новом поле
x += 1
y += 1
bomb_count = 0
for i in range(-1,2):
    for j in range(-1,2):
        if data[x + i][y + j] == bomb:
            bomb_count += 1
print(bomb_count)

for row in range(m):
    for column in range(n):
        x = row + 1
        y = column + 1
        if data[x][y] != bomb:
            bomb_count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if data[x + i][y + j] == bomb:
                        bomb_count += 1
            data[x][y] = bomb_count
for row in data:
    print(row)
print()



# if [[-1 for y in range(y-1, y+1)] for x in range(x-1, x+1)]:
#     count += 1
#     data[x][y] = count






# Напечатать табличку змейкой
# дано N
# 1 2 3
# 6 5 4
# 7 8 9

n = 10
data = [x for x in range(1, n)]
print(data)

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data[1].reverse()
print(data)
for row in data:
    for element in row:
        print(element, end=' ')
    print()
print()

# n = 3
# data = [[0 for y in range(n)] for x in range(n)]
# count = 0
# for row in range(len(data)):
#     for column in range(len(data[row])):
#         count += 1
#         data[row][column] = count
#         print(data[row][column], end='')
#     print()
# # data[1].reverse()
# # print(data)
# print()

result = []
n = 4
for i in range(n):
    current_list = [x for x in range(n * i +1, n * (i + 1) + 1)]
    if i % 2 == 1:
        current_list.reverse()
    print(current_list)

# напечатать табличку "спиралью"
# 1 2 3
# 8 9 4
# 7 6 5

x = 0
y = 0
direction = 0
n = 3
result = [[0 for i in range(n)] for j in range(n)]
current = 1
while current < n * n + 1:
    if result[x][y] == 0:
        result[x][y] = current
        current += 1
    if direction == 0:  # движение вправо
        if y + 1 < n:
            y += 1
        else:
            direction += 1  # поворот вниз
    elif direction == 1: # движение вниз
        if x + 1 < n:
            x += 1
        else:
            direction += 1 # поворот влево
    elif direction == 2:
        if y - 1 >= 0:
            y -= 1
        else:
            direction += 1
    elif direction == 3:
        if x - 1 >= 0:
            x -= 1
        else:
            direction = 0
for row in result:
    print(row)
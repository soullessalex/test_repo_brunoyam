# print('hello')
# a = 132
# b = 45
# b = b - 7
# c = a + b
# b = 25
# c = 35
# a = b + c
# a = 12.2
# a = int(a)
# print(a)
# year = 1991
# value = 'I was born in ' + str(year)
# print(value)
# print('I was born in', year)


# a = 5
# b = 10
# c = 7
# res_float = (a+b+c)/3
# res_int = (a+b+c)//3
# print(res_float)
# print(res_int)
# if a > b:
#     print(a)
# else:
#     print(b)

value = 5
# if value < -10:
#     print('left')
# else:
#     if value > 10:
#         print('right')
#     else:
#         print('center')
if value < -10:
    print('left')
elif value > 10:
    print('right')
else:
    print('center')

if -10 < value < 10:
    print('center')

#1
d = 6
if d % 2 == 0:
    print('четное')
else:
    print('нечетное')

#2
a = 3
b = 7
c = 11
# a b c
if a > b:
    tmp = b
    b = a
    a = tmp
if b > c:
    tmp = c
    c = b
    b = tmp
if a > b:
    tmp = b
    b = a
    a = tmp
print(a, b, c)
#3
a = 14
b = 8
if a % b == 0:
    print('делится')
else:
    print('не делится')

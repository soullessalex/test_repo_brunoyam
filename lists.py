<<<<<<< HEAD
# data = [2, 3, 5, 4, 65]
# summa = 0
# for number in data:
#     print(number)
#     summa += number
# print(summa)
#
# sum(data)
# print(sum(data))
#
# zeros = [0] * 30
# print(zeros)
# print(zeros+data)
#
# 1

data = [1, -3, 2, -3]
count = 0
for number in data:
    if number > 0:
        count += 1
print('количество = ', count)

# 2

data = [1, -3, 2, -3]
count = 0
for number in data:
    if number > 0:
        print(number)


# 3

data = [1, -3, 2, -3]
count = 0
for number in data:
    count += 1
    if count % 2 == 0:
        print(number)

for i in range(len(data)):
    if i % 2 == 0:
        print(data[i])
print(data[::2])

# 4

# data = [1, -3, 2, -3]
data = [1, 4, 10]
count = 0
for number in data:
    count += 1
    res = sum(data)
    tr = res / count
print(tr)

print(sum(data) / len(data))

# 5

data = ['hello', 'very long string', 'world']
a = 'hello'
b = 'very long string'
c = 'world'
if len(a) > 5:
    print(a)
if len(b) > 5:
    print(b)
if len(c) > 5:
    print(c)

for i in data:
    if len(i) > 5:
        print(i)

# 6

value = 'Hello my friend...'+'$'
result = ''
for i in range(len(value) - 1):
    if value[i] != value[i + 1]:
        result += (value[i])
print(result)
# ?

# 7

value = 'Hi, my name is Alexander'
print(value.swapcase())

# print(ord('a'))
# print(chr(97))
# symbol = 'b'
# upper_symbol = chr(ord(symbol) - 32)
# print(upper_symbol)
# lower_symbol = chr(ord(upper_symbol) + 32)
# print(lower_symbol)

value = 'Hi, my name is Alexander'
result = ''
for symbol in value:
    if 'A' <= symbol <= 'Z':
        result += chr(ord(symbol) + 32)
    elif 'a' <= symbol <= 'z':
        result += chr(ord(symbol) - 32)
    else:
        result += symbol
print(result)

# for i in range(54):
#     print(chr(i), end=' ')

# 8

data = [1, 2, -1, 4, 3]
for i in range(1, len(data)-1):
    if value[i+1] > value[i] < value[i - 1] or value[i + 1] < value[i] > value[i - 1]:
        result = True
    else:
        result = False
print(result)

# 9

value = [0, 2, 1]
result = True
for i in range(len(value)-1):
    if value[i] >= value[i + 1]:
        result = True
    else:
        result = False
        break
print(result)

res = all(value[i] >= value[i + 1] for i in range(len(value) - 1))
print(res)

# 10

value = [1, 2, 3, 4, 5]
res = 0
print(sum([0 if x % 2 == 0 else x for x in value]) - sum([0 if x % 2 != 0 else x for x in value]))
print(sum([-x if x % 2 == 0 else x for x in value]))
for i in value:
    if i % 2 != 0:
        res += i
    else:
        res -= i
print(res)

=======
# data = [2, 3, 5, 4, 65]
# summa = 0
# for number in data:
#     print(number)
#     summa += number
# print(summa)
#
# sum(data)
# print(sum(data))
#
# zeros = [0] * 30
# print(zeros)
# print(zeros+data)
#
# 1

data = [1, -3, 2, -3]
count = 0
for number in data:
    if number > 0:
        count += 1
print('количество = ', count)

# 2

data = [1, -3, 2, -3]
count = 0
for number in data:
    if number > 0:
        print(number)


# 3

data = [1, -3, 2, -3]
count = 0
for number in data:
    count += 1
    if count % 2 == 0:
        print(number)

for i in range(len(data)):
    if i % 2 == 0:
        print(data[i])
print(data[::2])

# 4

# data = [1, -3, 2, -3]
data = [1, 4, 10]
count = 0
for number in data:
    count += 1
    res = sum(data)
    tr = res / count
print(tr)

print(sum(data) / len(data))

# 5

data = ['hello', 'very long string', 'world']
a = 'hello'
b = 'very long string'
c = 'world'
if len(a) > 5:
    print(a)
if len(b) > 5:
    print(b)
if len(c) > 5:
    print(c)

for i in data:
    if len(i) > 5:
        print(i)

# 6

value = 'Hello my friend...' + '$'
result = ''
for i in range(len(value) - 1):
    if value[i] != value[i + 1]:
        result += (value[i])
print(result)
# ?

# 7

value = 'Hi, my name is Alexander'
print(value.swapcase())

# print(ord('a'))
# print(chr(97))
# symbol = 'b'
# upper_symbol = chr(ord(symbol) - 32)
# print(upper_symbol)
# lower_symbol = chr(ord(upper_symbol) + 32)
# print(lower_symbol)

value = 'Hi, my name is Alexander'
result = ''
for symbol in value:
    if 'A' <= symbol <= 'Z':
        result += chr(ord(symbol) + 32)
    elif 'a' <= symbol <= 'z':
        result += chr(ord(symbol) - 32)
    else:
        result += symbol
print(result)

# for i in range(54):
#     print(chr(i), end=' ')

# 8

data = [1, 2, -1, 4, 3]
for i in range(1, len(data)-1):
    if value[i+1] > value[i] < value[i - 1] or value[i + 1] < value[i] > value[i - 1]:
        result = True
    else:
        result = False
print(result)

# 9

value = [3, 2, 1]
result = True
for i in range(len(value)-1):
    if value[i] >= value[i + 1]:
        result = True
    else:
        result = False
        break
print(result)

res = all(value[i] >= value[i + 1] for i in range(len(value) - 1))
print(res)

# 10

value = [1, 2, 3, 4, 5]
res = 0
print(sum([0 if x % 2 == 0 else x for x in value]) - sum([0 if x % 2 != 0 else x for x in value]))
print(sum([-x if x % 2 == 0 else x for x in value]))
for i in value:
    if i % 2 != 0:
        res += i
    else:
        res -= i
print(res)

>>>>>>> origin/master

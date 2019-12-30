# 1

# data = 'Ivanov Ivan Ivanovich'
# data2 = data.split()
# for i in data2[1:]:
#     i = list(i)
#     print(i)
#     data3 = []
#     for j in range(len(i)):
#         j = 0
#         res = data[j] + '.'
#         data3 += res
#
# print(data2)
# print(data3)   # не работает

data = 'Ivanov Ivan Ivanovich'
def short_name(first_name, last_name, family_name):
    # result = last_name + " " + first_name[0] + "." + family_name[0] + "."
    # return result
    return last_name + " " + first_name[0] + "." + family_name[0] + "."


print(short_name("Ivan", "Ivanov", 'Ivanovich'))

# 2

# value = [1, 2, 3]
# result = True
# def check(value):
#     result = True
#     res = all(value[i] > value[i + 1] for i in range(len(value) - 1))
# print(check([3, 2, 1]))


# def check(value):
#     result = True
#     for i in range(len(value)-1):
#         if value[i] > value[i + 1] or value[i] < value[i + 1]:
#             result = True
#         else:
#             result = False
#         result += 1
#     return result
# print(check([3, 2, 1]))
#
# def check(value):
#     result = True
#     res = all(value[i] > value[i + 1] for i in range(len(value) - 1))
#     res = all(value[i] < value[i + 1] for i in range(len(value) - 1))
#     return result
# print(check([5, 2, 3, 6]))    # не работает


value = [3, 2, 3]


def check(value):
    res = True
    kol = 0
    for i in range(1, len(value)):
        if value[i] > value[i - 1]:
            kol = kol + 1
        elif value[i] < value[i - 1]:
            kol = kol + 1
    if kol == len(value) - 1:
        res = True
    else:
        res = False
    print(kol)
    return res
print(check(value))     # не корректно


def is_sorted(data):
    ordered = sorted(data)
    if ordered == data:
        return True
    ordered.reverse()
    # ordered = reversed(ordered)
    if ordered == data:
        return True
    return False

data = [1, 2, 3]
print(is_sorted(data))
data.reverse()
print(is_sorted(data))
data[0] = 0
print(is_sorted(data))


# 3

value = [1, 2, 2, 3, 4, 5]
def spisok(value):
    for i in value:
        if value.count(i) > 1:
            del value[i]
    return value
print(spisok(value))


def distinct(data):
    # elements = set()
    # for value in data:
    #     elements.add(value)
    # return list(elements)

    return list(set(data))

print(distinct([1, 2, 2, 3, 3, 3, 3]))

#4 дана дата "12.04.2019", требуется перевести в запись "12 апреля 2019"

months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}


value = '12.04.2019'
keys = months.keys()
data = value.split('.')
data2 = list(data[1])
for i in range(len(data2)):
    if data2[0] == '0':
        x = data2[1]
    else:
        x = data[1]
x = int(x)
y = months.get(x)
data[1] = y
value = " "
value = value.join(data)
print(value)



#5

def form_map(names, phones):
    name_to_phone = dict()
    for i in range(len(names)):
        name_to_phone[name_to_phone[i]] = phones[i]
    return name_to_phone


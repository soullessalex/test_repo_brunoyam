# 5 дана дата "12.04.2019", требуется перевести в запись "12 апреля 2019"

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
str_value = months.get(14)
if str_value is None:
    print("Wrong Number")
else:
    print(str_value)

for value in months:
    print(months[value])

keys = [value for value in months]
keys = months.keys()

months[13] = 'Ещё один месяц'
print(months[13])
del months[13]
print(months.get(13))
print(type(keys))


# dictionary = dict()
# dictionary = {}
phones = set()
phones.add('123456')
phones.add('123457')
print(phones)
phones.add('123456')
print(phones)
phones.add('123459')
print(phones)

for element in phones:
    print(element)

another_phones = set()
another_phones.add('123455')
another_phones.add('123453')

united_set = phones.union(another_phones)
print(united_set)

intersect_set = phones.intersection(another_phones)
print(intersect_set)


element = '123456'
if element in united_set:
    print("yes")

#hash()

# 12.04.2019
def format_date(date):
    parts = date.split(".")
    changed_month = months.get(int(parts[1]))
    if changed_month is None:
        return "Error during parsing"
    else:
        return parts[0] + " " + changed_month + " " + parts[1]

print(format_date("12.14.2019"))
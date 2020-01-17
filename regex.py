import re

pattern = re.compile('^world')
value = 'world, hello something'
print(re.search(pattern, value))

pattern = re.compile('^\w\w\w$')
print(re.search(pattern, "abF"))
print(re.search(pattern, "asfdfs"))

pattern = re.compile('\d\d\d')
print(re.search(pattern, "ASF 123665"))

pattern = re.compile("^Hello, \w\w\w\w!")
print(re.search(pattern, 'Hello, Alex!'))

pattern = re.compile('^\d{4}$')
print(re.search(pattern, '1234'))
print(re.search(pattern, '12345'))

re.compile('^d{4,10}$')
print(re.search(pattern, '123'))

pattern = re.compile('^\d{4,}$')
print(re.search(pattern, '123453125553'))

pattern = re.compile('^d{,}$')
print(re.search(pattern, '1{}'))

pattern = re.compile('^[abc] + $')
pattern = re.compile('^[0-5] + $')
pattern = re.compile('^[b-z] + $')

pattern = re.compile('^hello|world|something$')

# 1  DD.MM.YYYY

pattern = re.compile('(0[1-9]|[12]\d|3[01])\.(1[012]|0[1-9])\.(\d{4})')
# print(re.search(pattern, '31.12.1999'))
result = re.search(pattern, '12.12.2010')
print(result.groups())
# 2 +7xxx-xxx-xx-xx
pattern = re.compile('\+7-?\d{3}-?\d{3}-?\d{2}-?\d{2}')

# Четное число
pattern = re.compile('[02468]$')

# Шестнадцатиричкая запись цвета

pattern = re.compile('(\d|[A-F]){6}')

print(re.search(pattern, 'FF42A5'))

""""""""
""""""""


pattern = re.compile('hello')

print(re.match(pattern, 'hello'))
print(re.findall(pattern, 'hello'))
print(re.sub('\s+', ' ', 'Hello    world    it\'s    me'))
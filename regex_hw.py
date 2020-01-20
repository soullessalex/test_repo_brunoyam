import re


# ДЗ

#1

pattern = '<b> Определенный набор символов </b>'
# print(re.sub(pattern, '<b>', '*'))
res1 = re.sub('<b>', '*', pattern)
res2 = re.sub('</b>', '*', res1)
print(res2)

pattern = re.compile('<b>(.*?)<\/b')
value = "<b> hello world </b><b> safatuj </b>"
print(re.sub(pattern, '*\\1*', value))
#2

pattern = re.compile('(\w+)(\s+\\1)+')
value = "abc abc abc def def"
print(re.sub(pattern, '\\1', value))

#3
pattern = re.compile('^[A-Za-z]\w*(\d\w*[?!]|[?!]\w*\d)\w*')
value = 'asdfsdf12!'
print(re.match(pattern, value) is not None)


pattern = 'Delivery took 2 hours?'
if re.match('[A-Za-z]', pattern) and re.search('\d', pattern) and (re.search('\!', pattern) or re.search('\?', pattern)):
    print(True)
else:
    print(False)

#4

pattern = re.compile('^(0?(1+0)?)*$')





#5

pattern = re.compile('\w+@\w+\.(ru|com|de)')
value = "a@b.com"
print(re.match(pattern, value) is not None)




pattern = 'soullessalex@gmail.com'
if re.search('\w+@\w+\.[A-Za-z]+', pattern):
    print(True)
else:
    print(False)
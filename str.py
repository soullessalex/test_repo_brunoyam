name = 'Example'
# print(name[0])
# print(type(name[3]))
#
# subname = name[1:3:1]
# print(subname)
#
# subname = name[1:]
# print(subname)
#
# subname = name[:4]
# print(subname)
#
# subname = name[::2]
# print(subname)
#
# print(name[-1])
#
# print(name[0:8])
#
# print(name[::-1])

value = 'aabbccdd'
symbol = 'b'

# count = 0
# for char in value:
#     if char==symbol:
#         # print('found')
#         count +=1 # count = count +1
#
# print('num of elements', count, count/len(value)*100)

count = 0
for i in range(len(value)):
    print(i, value[i])
    if value[i] == symbol:
        count += 1
print('num of elements', count, count/len(value)*100)

count = 0
for i in range(len(value)):
    char = value[i]
    print(i, char)
    if char == symbol:
        count += 1

#1
value = 'abccba'
print(value[-1]+value[1:-1]+value[0])


#2
# value = 'abcba'
# result = True
# for i in range(len(value)):
#     if value[i] != value[-i-1]:
#         result = False
#         break
# print(result)
# print(value == value[::-1]) # однострочное решение



#3
value = 'abcbbaac'
result = True
for char in value:
    if char not in 'abc': # if char != 'a' or char != 'b' or char != 'c':
        result = False
        break
print(value, 'consist of abc', result)

result = True
for i in range(len(value)):
    if value[i] == 'a' or value[i] == 'b' or value[i] == 'c':
        result = True
    else:
        result = False
print(result)
#4

value = 'aaabbbbcc'+'$'
last_change = 0
result = ''
for i in range(len(value)-1):
    if value[i] != value[i+1]:
        current_value = value[last_change: i+1]
        result += value[i] + str(len(current_value))
        last_change = i+1
print(result)

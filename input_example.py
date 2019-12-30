# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число'))
# print('result = ', a + b)

# n = 10
# for i in range(n):
# while True:
    # value = input('Enter expression').split()
    # if 'exit' in value:
        # break
    # a = int(value[0])
    # a = input('1-ое число')
    # if a == 'exit':
        # break
    # a= int(a)
    # x = value[1]
    # x = input('операция с числами')
    # if x == 'exit':
    #     break
    # b = int(value[2])
    # b = input('2-ое число')
    # if b == 'exit':
    #     break
    # b= int(b)
    # result = 0
    # if x == '+':
    #     result = a + b
    # elif x == '-':
    #     result = a - b
    # elif x == '*':
    #     result = a * b
    # elif x == '/':
    #     result = a / b
    # print('result = ', result)



# дз

Empty = ''
data = [Empty] * 5
while True:
    user_input = input('Enter command: ').split()
    command = user_input[0]
    if command == 'show':
        print(data)
    elif command == 'free':
        print(data.count(Empty))
    elif command == 'park':
        # free_pos = 0
        # for place in data:
        #     if place == Empty:
        #         break
        #     free_pos += 1
        free_pos = data.index(Empty)
        data[free_pos] = user_input[1]
        print(data)
    elif command == 'leave':
        # pos = 0
        # for i in range(len(data)):
        #     if data[i] == user_input[1]:
        #         data[i] = Empty
        #         break
        data[data.index(user_input[1])] = Empty
        print(data)
    else:
        break







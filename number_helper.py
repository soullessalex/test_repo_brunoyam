def sum_of_digits(number):
    return sum([int(x) for x in str(number)])


print(sum_of_digits(12345))





# посчитать сумму цифр числа
number = 123
print(sum_of_digits(number)))

summa = 0
while number !=0:
    summa += number % 10
    number //= 10
print(summa)

# посчитать количество делителей

number = 123
count = 0
for i in range(2, number):
    if number % i == 0:
        count += 1
        print(i)
print(count)

print(sum([1 if number % x == 0 else 0 for x in range(2, number)]))
print()



# 3

data = [123, 232, 2323]
print('---')
for i in data:
    # summa = 0
    # while i != 0:
    #     summa += i % 10
    #     i //= 10
    # print(summa)
    print(sum_of_digits(number))
print(data)

print('---')
max_sum = -1
for i in data:
    summa = sum_of_digits(number)
    # while i != 0:
    #     summa += i % 10
    #     i //= 10
    max_sum = max(max_sum, summa)
print(max_sum)

from typing import List



def sum_of_two_element(a, b):
    """
    Функция для вычисление двух чисел

    :param a: Первое число для суммы
    :type a: int
    :param b: Второе число для суммы
    :type b: int
    :return: сумма двух чисел
    :rtype c: int
    """

    return a + b

print(sum_of_two_element(1, 2))


def find_positive_elements(data):
    """
    :type data: List[int]
    :return:
    """
    result = []
    for element in data:
        if element > 0:
            result.append(element)
    return result

print(find_positive_elements([1, -2, 3, -5]))


def my_join(*args, delimiter=' '):
    return delimiter.join(args)

print(my_join('Hello', 'world'))
print(my_join('a', 'b', 'c', 'd', delimiter=', '))

print('Hello', 'world', '!', sep=', ', end='!!!\n')


def most_common_function(*args, **kwargs):
    print(args)
    print(kwargs)

most_common_function('Hello', 'world', '!', sep=', ', end='!!!')


#1 напечатать максимум из трех


def max_res(data):
    return max(data)

print(max_res([1, 23, 15]))

#2 дан год (число), определить, является ли он весокосным (делится на 4 и не делится на 100)

def year(data):
    if data % 4 == 0 and data % 100 != 0:
        return 'Yes'
    else:
        return 'No'

print(year(409))


#3 даны длины двух катетов прямоугольного треугольника, посчитать гипотенузу ( c = sqrt(a^2 + b^2))

def gip(a, b):
    c = (a**2 + b**2)**(1/2)
    return c

print(gip(3, 4))

#4 проверить, что является простым (делится без остатка на 1 и на себя)

def simple(number):
    for i in range(2, number):
        if number % i == 0:
            return 'No'
    return 'Yes'


print(simple(6))


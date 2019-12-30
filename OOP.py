

# class BackClient():
#     name = "Dima"
#     age = 21
#     inc = 500
#     status = "investor"
#     def get_month_inc(self): # ссылка на объект класса BackClient
#         return self.inc / 12
#
#
# max = BackClient()
#
# print(max.age)
#
# print(max.get_month_inc())


class BackClient():
    min_life = 15 * 12
    def __init__(self, name, age, inc, status):
        self.name = name
        self.age = age
        self.inc = inc
        self.status = status

    def get_month_inc(self):  # ссылка на объект класса BackClient
        return self.inc / 12

    def accept_credit(self, value):
        pay_time = 70 - self.age
        if (self.inc - value / pay_time - self.min_life > 0) & (pay_time > 0):
            return True
        else:
            return False



max = BackClient("Max", 99, 1000, 'Investor')

print(max.age)

print(max.get_month_inc())

print(max.accept_credit(1000))


class Cat():
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def meow(self):
        return self.name + " says meowwwww "
    def is_healthy(self):
        if 3 < self.weight < 10:
            return "Ок"
        else:
            return "Не ок"


Barsik = Cat("Barsik", "black", 9)

print(Barsik.meow())
print(Barsik.is_healthy())

# class Animal():
#     def eat(user_input):
#         return "Приятного аппетита"
#     def getName(user_input):
#         return "Мурзик"
#
#         while True:
#             try:
#                 user_input = input().split()
#                 command = user_input[0]
#
#                 if command == 'getname':
#                     getName(user_input)
#
#                 elif command == 'average':
#                     process_average(user_input)
#                 elif command == 'min':
#                     if len(user_input) > 2:
#                         pass
#                     elif user_input[1] == 'year':
#                         pass
#                     else:
#                         pass
#             except:
#                 print("Wrong command. Retry")
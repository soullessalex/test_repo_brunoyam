class Fraction:
    def __init__(self, delimiter, denominator):
        self.a = delimiter
        self.b = denominator

    def __add__(self, other): # a + b
        return self.plus(other)

    def __sub__(self, other): # a - b
        return self.minus(other)

    def __mul__(self, other): # a * b
        return self.mul(other)

    def __truediv__(self, other): # a / b
        return self.div(other)

    def __floordiv__(self, other): # a // b
        return self.div(other)

    def __eq__(self, other): # a == b
        return self.a == other.c and self.b == other.d

    def __le__(self, other): # a <= b
        return 0

    def __gt__(self, other): # a > b
        return 0

    def plus(self, other):
        a = self.a
        b = self.b
        c = other.c
        d = other.d
        return Fraction(a*d + b*c, b*d)

    def minus(self, other):
        return Fraction(self.a * other.d - self.b * other.c, self.b * other.d)

    def mul(self, other):
        return Fraction(self.a * other.c, self.b * other.d)

    def div(self, other):
        return Fraction(self.a * other.d, self.b * other.c)

    def to_float(self):
        return self.a / self.b

    # def simplify(self):
        # a = self.a
        # b = self.b
        # while a != 0 and b != 0:
        #     if a > b:
        #         a -= b
        #     else:
        #         b -= a
        #     a = max(a, b)
        #     b = max(a, b)

    # def __str__(self):
    #     return str(self.a) + "/" + str(self.b)




one_half = Fraction(1, 2)
one_quater = Fraction(1, 4)
three_quater = one_half.plus(one_quater)
three_quater = one_half + one_quater
print(three_quater)
# three_quater.simplify()
print(three_quater)
print(three_quater.to_float())
from expression.Expression import Expression, Pow


class Const(Expression):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def calc(self):
        return self.value


p = Pow(Const(2), Const(5))
print(p.calc())


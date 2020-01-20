import abc


class Expression(abc.ABC):
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

    @abc.abstractmethod
    def calc(self):
        return 0


class Pow(Expression):
    def __init__(self, left, right):
        super().__init__(left, right)

    def calc(self):
        return self.left.calc() ** self.right.calc()


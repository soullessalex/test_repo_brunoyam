from miner.cell import Cell
from miner.field import Field


class View:
    def __init__(self, field):
        self.field = field   # type:  # miner.field.Field

    def display_field(self):
        for row in self.field.data:
            for cell in row:
                if cell.is_open:
                    if cell.mines_count == Cell.Mine:
                        print('* ', end='')
                    else:
                        print(str(cell.mines_count), end=' ')
                else:
                    print("_ ", end='')
            print()

    def get_user_turn(self):
        try:
            x = int(input("x: "))
            y = int(input("y: "))

            if x < 0 or x >= self.field.size:
                return None
            if y < 0 or y >= self.field.size:
                return None
        except:
            return None

        return x, y
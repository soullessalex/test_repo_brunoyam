class Car:
    def __init__(self, number, model):
        self.number = number
        self.model = model

    def __str__(self):
        return str(self.number) + "," + str(self.model)

    def __eq__(self, other):
        pass


class Parking:
    def __init__(self, places_count = 10):
        Empty = ''
        self.places = [Empty] * places_count

    def park(self, car):
        Empty = ''
        data = self.places
        free_pos = data.index(Empty)
        data[free_pos] = car
        return data
    def leave(self, car):
        Empty = ''
        data = self.places
        data[data.index(car)] = Empty
        return data
    def free(self):
        Empty = ''
        data = self.places
        return data.count(Empty)


bmw = Car("a123aa", "BMW")
audi = Car("c523ta", "Audi")
garage = Parking()
garage.park(bmw)
garage.park(audi)
print(garage.free())
print(garage)
garage.leave(bmw)
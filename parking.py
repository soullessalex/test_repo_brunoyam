<<<<<<< HEAD
class Car:
    def __init__(self, number='', model=''):
        self.number = number
        self.model = model

    def __str__(self):
        return "|" + self.number + " " + self.model

    def __eq__(self, other):
        return self.number == other.number


class Parking:
    def __init__(self, places_count = 10):
        self.Empty_car = Car()
        self.places = [self.Empty_car] * places_count

    def park(self, car):
        pos = -1
        for i in range(len(self.places)):
            if self.places[i] == self.Empty_car:
                pos = i
                break
            if pos != -1:
                self.places[pos] = car
            else:
                print('Parking is full')
    def leave(self, car):
        try:
            pos = self.places.index(car)
            self.places[pos] = self.Empty_car
        except ValueError:
            print('Car is not found')
    def __str__(self):
        # result = ""
        # for car in self.places:
        #     result += str(car) + ","
        return ','.join([str(car) for car in self.places])
    def free(self):
        return self.places.count(self.Empty_car)



bmw = Car("a123aa", "BMW")
print(bmw)
audi = Car("c523ta", "Audi")
print(audi)
garage = Parking()
print(garage)
garage.park(bmw)
garage.park(audi)
print(garage)
print(garage.free())
=======
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
>>>>>>> origin/master
garage.leave(bmw)
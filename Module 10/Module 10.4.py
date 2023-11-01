import random


class Car:
    def __init__(self, RegistrationNumber, MaxSpeed):
        self.RegisNum = RegistrationNumber
        self.MaximSpe = MaxSpeed
        self.CurreSpe = 0
        self.TraveDis = 0

    def accelerate(self, change):
        self.CurreSpe += change
        if self.CurreSpe > self.MaximSpe:
            self.CurreSpe = self.MaximSpe
        elif self.CurreSpe < 0:
            self.CurreSpe = 0

    def drive(self, time):
        self.TraveDis += time * self.CurreSpe


class Race:
    def __init__(self, Name, CarDistance, Num_vehicle):
        self.name = Name
        self.distance = CarDistance
        self.cars = list(range(Num_vehicle))

        for i in range(Num_vehicle):
            self.cars[i] = Car(f"ABC-{i + 1}", random.randint(100, 200))

    def hour_passes(self):
        for i in range(len(self.cars)):
            self.cars[i].accelerate(random.randint(-10, 15))
            self.cars[i].drive(1)

    def print_status(self):
        for i in range(len(self.cars)):
            print(vars(self.cars[i]))

    def race_finished(self):
        for i in range(len(self.cars)):
            if self.cars[i].TraveDis >= self.distance:
                print(self.cars[i].RegisNum, "won the race!\n")
                return True


def main():
    new_race = Race("Grand Demolition Derby", 8000, 10)
    hours = 0

    while not new_race.race_finished():
        new_race.hour_passes()
        hours += 1
        if not hours % 10:
            new_race.print_status()
    new_race.print_status()


main()
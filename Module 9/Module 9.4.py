import random

class Car:
    def __init__(self, RegistrationNumber, MaxSpeed):
        self.RegisNum = RegistrationNumber
        self.MaximSpeed = MaxSpeed
        self.CurreSpeed = 0
        self.TraveDist = 0

    def drive(self, count):
        self.TraveDist += count * self.CurreSpeed

    def accelerate(self, SpeedChange):
        self.CurreSpeed += SpeedChange
        if self.CurreSpeed > self.MaximSpeed:
            self.CurreSpeed = self.MaximSpeed
        elif self.CurreSpeed < 0:
            self.CurreSpeed = 0

def main():
    cars = []
    for i in range(10):
        car = Car(f"ABC-{i}", random.randint(100, 200))
        cars.append(car)

    while True:
        for i in range(len(cars)):
            cars[i].accelerate(random.randint(-10, 15))
            cars[i].drive(1)

            if cars[i].TraveDist >= 10000:
                print(cars[i].RegisNum, "Won!")
                break
        else:
            continue
        break

    for i in range(len(cars)):
        print("Car", cars[i].RegisNum)
        print("Current Speed:", cars[i].CurreSpeed)
        print("Travelled Distance:", cars[i].TraveDist)
        print("---")


main()
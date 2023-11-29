from random import randint


class Car:
    def __init__(self, RegistrationNumber, MaxSpeed, CurreSpe=0, TraveDis=0):
        self.RegisNum = RegistrationNumber
        self.MaximSpe = MaxSpeed
        self.CurreSpe = CurreSpe
        self.TraveDis = TraveDis

    def accelerate(self, change):
        self.CurreSpe += change
        if self.CurreSpe > self.MaximSpe:
            self.CurreSpe = self.MaximSpe
        elif self.CurreSpe < 0:
            self.CurreSpe = 0

    def drive(self, time):
        self.TraveDis += time * self.CurreSpe


class ElectricCar(Car):
    def __init__(self, Registration_number, MaxSpeed, battery_capacity, CurreSpe=0, TraveDis=0):
        super().__init__(Registration_number, MaxSpeed, CurreSpe, TraveDis)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, Registration_number, MaxSpeed, tank_volume, CurreSpe=0, TraveDis=0):
        super().__init__(Registration_number, MaxSpeed, CurreSpe, TraveDis)
        self.tank_volume = tank_volume


# main program
electric_car = ElectricCar("ABC-15", 180, 52.5, 0)
gasoline_car = GasolineCar("ACD-123", 165, 32.3, 0, 0)

speed_electric_car = randint(30, 60)
speed_gasoline_car = randint(30, 60)

electric_car.accelerate(speed_electric_car)
gasoline_car.accelerate(speed_gasoline_car)

hours_of_drive = 3

electric_car.drive(hours_of_drive)
gasoline_car.drive(hours_of_drive)

print(f"Electric Car: {electric_car.RegisNum}\nDistance Travelled: {electric_car.TraveDis} km\n")
print(f"Gasoline Car: {gasoline_car.RegisNum}\nDistance Travelled: {gasoline_car.TraveDis} km\n")


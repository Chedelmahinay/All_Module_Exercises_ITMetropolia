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
    NewCar = Car("ABC-123", 165)
    for i in range(4):
        match i:
            case 0:
                NewCar.accelerate(30)
                NewCar.drive(0.5)
            case 1:
                NewCar.accelerate(70)
                NewCar.drive(2)
            case 2:
                NewCar.accelerate(50)
                NewCar.drive(3.5)
            case 3:
                NewCar.accelerate(-200)
                NewCar.drive(1)
        print(vars(NewCar))

main()
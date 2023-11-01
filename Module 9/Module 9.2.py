class Car:
    def __init__(self, RegistrationNumber, MaxSpeed):
        self.RegisNum = RegistrationNumber
        self.MaximSpeed = MaxSpeed
        self.CurreSpeed = 0
        self.TraveDist = 0

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
            case 1:
                NewCar.accelerate(70)
            case 2:
                NewCar.accelerate(50)
            case 3:
                NewCar.accelerate(-200)
        print(vars(NewCar))

main()

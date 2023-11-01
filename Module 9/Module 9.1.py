
class Car:
    def __init__(self, RegistrationNumber, MaxSpeed):
        self.RegisNum = RegistrationNumber
        self.MaximSpeed = MaxSpeed
        self.CurreSpeed = 0
        self.TraveDist = 0

def main():
    NewCar = Car("ABC-123", 142)
    print("Registration Number:", NewCar.RegisNum)
    print("Maximum Speed:", NewCar.MaximSpeed, "km/h")
    print("Current Speed:", NewCar.CurreSpeed, "km/h")
    print("Travelled Distance:", NewCar.TraveDist, "km")


main()








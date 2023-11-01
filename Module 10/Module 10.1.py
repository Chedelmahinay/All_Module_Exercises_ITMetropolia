class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current = bottom_floor

    def go_to_floor(self, floor):
        if floor > self.top:
            print(f"Error: Cannot go to floor {floor}. Maximum floor allowed is {self.top}.")
            return
        while floor != self.current:
            if floor > self.current:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        self.current += 1
        print(f"Elevator moving up to floor {self.current}")

    def floor_down(self):
        self.current -= 1
        print(f"Elevator moving down to floor {self.current}")


def main():
    new_elevator = Elevator(0, 10)
    new_elevator.go_to_floor(6)
    new_elevator.go_to_floor(4)
    new_elevator.go_to_floor(100)

main()
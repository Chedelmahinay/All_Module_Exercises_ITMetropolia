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


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom = bottom_floor
        self.top = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, floor):
        if elevator_num >= 0 and elevator_num < len(self.elevators):
            print(f"\nRunning Elevator {elevator_num + 1}:")
            self.elevators[elevator_num].go_to_floor(floor)
        else:
            print(f"Error: Elevator number {elevator_num} is out of range.")

    def fire_alarm(self):
        print(f"\nFire Alarm Triggered - All elevators moving to the bottom floor!")
        for i in range(len(self.elevators)):
            self.run_elevator(i, self.bottom)

def main():
    building_complex = Building(0, 10, 8)
    building_complex.run_elevator(4, 8)
    building_complex.run_elevator(6, 8)
    building_complex.run_elevator(2, 2)

    building_complex.fire_alarm()

main()

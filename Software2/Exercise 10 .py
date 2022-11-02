import random

# exercise 1
print("\n************************Exercise 1*****************************\n")

class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self, current_floor):
        current_floor += 1

    def floor_down(self,current_floor):
        current_floor -= 1
    def go_to_floor(self, floor):
        while floor != self.current_floor:
            if floor > self.top_floor:
                print("This floor doesn't exist.")
                break
            if floor < self.bottom_floor:
                print("This floor doesn't exist.")
                break
            else:
                if floor == self.current_floor:
                    print("You are already in ", self.current_floor, "floor.")
                if floor > self.current_floor:
                    self.floor_up(floor)
                    self.current_floor = floor
                    print("Floor is currently", self.current_floor)
                if floor < self.current_floor:
                    self.floor_down(floor)
                    self.current_floor = floor
                    print("Floor is currently", self.current_floor)


elevator = Elevator(1, 9)

elevator.floor_up(1)
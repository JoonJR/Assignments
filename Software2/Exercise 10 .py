import random

# exercise 1
print("\n************************Exercise 1*****************************\n")


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            print(f"This elevator is moving up from {self.current_floor} to {self.current_floor+1}")
            self.current_floor += 1
            return True
        else:
            return False

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            print(f"The elevator is moving down from {self.current_floor} to {self.current_floor-1}")
            self.current_floor -= 1
            return True
        else:
            return False
    def go_to_floor(self, floor):
        if floor > self.current_floor:
            for i in range(floor - self.current_floor):
                if not self.floor_up():
                    break

        elif floor < self.current_floor:
            for i in range(self.current_floor - floor):
                if not self.floor_down():
                    break
        else:
            print("You are already at this floor.")
elevator = Elevator(1, 5)
target_floor = int(input("Which floor you would like to go: "))
elevator.go_to_floor(target_floor)

# exercise 2
print("\n************************Exercise 2*****************************\n")


class Building:
    def __init__(self, bottom_floor, top_floor, elevator_list):
        self.elevator_list = []
        for i in range(elevator_list):
            self.elevator_list.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, floor):
        print(f"The elevator number {elevator_number} is running")
        self.elevator_list[elevator_number - 1].go_to_floor(floor)


print("Elevators in the building: ")
building = Building(1, 7, 3)
building.run_elevator(1, 4)
building.run_elevator(2, 4)
building.run_elevator(3, 1)

print("\n************************Exercise 3*****************************\n")


class Building:
    def __init__(self, bottom_floor, top_floor, elevator_list):
        self.elevator_list = []
        for i in range(elevator_list):
            self.elevator_list.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, floor):
        print(f"The elevator number {elevator_number} is running")
        self.elevator_list[elevator_number - 1].go_to_floor(floor)

    def fire_alarm(self):
        print("************************")
        print("ITS HOT :D")
        for i in self.elevator_list:
            i.go_to_floor(i.bottom_floor)

print("Elevators in the building: ")
building = Building(1, 7, 3)
building.run_elevator(1, 4)
building.run_elevator(2, 4)
building.run_elevator(3, 1)
building.fire_alarm()


print("\n************************Exercise 4*****************************\n")


class Car:
    def __init__(self, reg, max_speed, curr_speed=0, distance_travelled=0):
        self.reg = reg
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.distance_travelled = distance_travelled

    def accelerate(self, change_of_speed):
        if self.max_speed >= self.curr_speed + change_of_speed >= 0:
            self.curr_speed = self.curr_speed + change_of_speed
        elif self.max_speed < self.curr_speed + change_of_speed:
            self.curr_speed = self.max_speed
        elif self.curr_speed + change_of_speed < 0:
            self.curr_speed = 0
        return self.curr_speed

    def drive(self, number_of_hours):
        self.distance_travelled += number_of_hours * self.curr_speed

class Race:
    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.cars_list = cars_list

    def hour_pass(self):
        for car in self.cars_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1.)

    def print_status(self):
        print(self.name + ":")
        print("Registration   Speed     Travelled ")
        for car in self.cars_list:
            print(f"{car.reg:6s}:       {car.curr_speed:3d}km/h    {car.distance_travelled}km")

    def race_finished(self):
        for car in self.cars_list:
            if car.distance_travelled >= self.distance:
                return True
        return False

car_list = []

for i in range(1, 11):
    new_car = Car("ABC-" + str(i), random.randint(100, 200))
    car_list.append(new_car)

race = Race("Grand Demolition Derby", 8000, car_list)
n = 0
while not race.race_finished():
    race.hour_pass()
    n += 1
    if n%10 == 0:
        print(f"After {n} hours")
        race.print_status()

print(f"The final result after {n} hours is:")
race.print_status()
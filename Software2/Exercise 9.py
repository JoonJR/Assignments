import random
from prettytable import PrettyTable

# exercise 1
print("\n************************Exercise 1*****************************\n")


class Car:
    def __init__(self, reg, max_speed, curr_speed=0, distance_travelled=0):
        self.reg = reg
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.distance_travelled = distance_travelled


car1 = Car("ABC-123", 142)

print('First cars registration plate is', car1.reg, 'and the maximum speed on the car is', car1.max_speed, 'km/h.'
      'The current speed is', car1.curr_speed, 'km/h and distance travelled is', car1.distance_travelled,'km.')


# exercise 2
print("\n************************Exercise 2*****************************\n")


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


car1 = Car("ABC-123", 142)

print('Now the car accelerates to 30 km/h, new current speed of the car is', car1.accelerate(30), 'km/h')
print('Car enters highway and accelerates to correct speed', car1.accelerate(70), 'km/h')
print('New sports car, ofcourse you need to try how the power feels, drivers press gas pedal to the floor and speeds '
      'to', car1.accelerate(50), 'km/h')
print('It only goes 142km/h?? Driver spots a cop car and has to brake hard, looks like the brakes are too good'
      ', car is now going at', car1.accelerate(-200), 'km/h')


# exercise 3
print("\n************************Exercise 3*****************************\n")


class Car:
    def __init__(self, reg, max_speed, curr_speed=0, distance_travelled=2000):
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


car = Car("ABC-123", 142)
car.accelerate(60)
car.traveled_distance = 2000
print(f"The initial distance is {car.distance_travelled} km")
car.drive(1.5)
print(f"The distance traveled in 1.5h at the constant speed of 60 km/h is {car.distance_travelled} km")


# Exercise 4
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


car_list = []
for i in range(1, 11):
    new_car = Car("ABC-" + str(i), random.randint(100, 200))
    car_list.append(new_car)

race_on = True

while race_on:
    for car in range(len(car_list)):
        if car_list[car].distance_travelled <= 10000:
            car_list[car].drive(1)
            car_list[car].accelerate(random.randint(-10, 15))
        else:
            print(f"The car {car_list[car].reg} won the race!!")
            race_on = False


my_table = PrettyTable(["Registration number", "Distance traveled", "Max speed:"])
for car in range(len(car_list)):
    my_table.add_row([car_list[car].reg, car_list[car].distance_travelled, car_list[car].max_speed])
print(my_table)

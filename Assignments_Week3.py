#phase 1

n = 1
while n <= 1000:
    modulo = n % 3
    if modulo == 0:
        print(str(n))
    n = n + 1

#phase 2

inches_input = float(input("Give a lenght in inches to convert it to centimeters: "))
while inches_input >=0:
    cm = inches_input * 2.54
    print(f"This lenght in cm is: {cm:.2f}")
    inches_input = float(input("Enter lenght in inches: "))

#phase 3

input_number = int(input("Enter first number: "))
smallest_number = input_number
largest_number = input_number
while input_number !="":
    if input_number <= smallest_number:
        smallest_number = input_number
    if input_number >= largest_number:
        largest_number = input_number
    input_number = input("Enter new number or leave empty to finish: ")
    if input_number == "":
        break
    input_number = int(input_number)
print(f"The smallest number is: {smallest_number} and the largest number is: {largest_number}")

#phase 4

import random

random_int = random.randint(1,10)
user_int = int(input("Guess a integer from 1 to 10: "))
while user_int != random_int:
    if user_int < random_int:
        print("Too low, guess again: ")
    if user_int > random_int:
        print("Too high, guess again: ")
    user_int = int(input("Guess a integer from 1 to 10: "))
print("Correct!")

#phase 5

user_name = "python"
password = "rules"
tries = 0
input_username = ""
input_password = ""
while not(input_username == user_name and input_password == password):
    tries = tries + 1
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    if tries == 5:
        print("Access denied.")
        break
    elif input_username == user_name and input_password == password:
        print("Welcome")
    else:
        print("Try again")


#phase 6

N = int(input("Enter a amount random points: "))
n = 0
N_count = 0

while N_count != N:
    N_count = N_count + 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    nn = x**2+y**2


    if nn < 1:
        n = n +1

pi = 4*n/N
print(pi)






















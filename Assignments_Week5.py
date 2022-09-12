import random

#phase 1
def rollDice():
    return random.randint(1,6)


dice = rollDice()
while dice != 6:
    print(dice)
    dice = rollDice()
print(dice)

#phase 2

def rollDice(sides):
    return random.randint(1,sides)


dice_sides = int(input("How many sides does the dice have?: "))

dice = rollDice(dice_sides)
while dice != dice_sides:
    print(dice)
    dice = rollDice(dice_sides)
print(dice_sides)

#phase 3

def gallon_litres(gallons):
    return gallons * 3.785


print("Enter negative number to stop.")
gallons_input = float(input("Enter the amount in gallons to convert it to litres: "))
while gallons_input >= 0:
    print(f"Entered amount of  gallons is "+ str(gallon_litres(gallons_input)) + " litres")
    gallons_input = float(input("Enter the amount in gallons to convert it to litres: "))

# phase 4
def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total



result = sum(1,2,3,4,5,6,7,8,9,10)
print(result)

#phase 5

import math
def num(numlist):
    even_list = []
    for i in numlist:
        if i % 2 == 0:
            even_list.append(i)
    print("Orginal list was: " + str(numlist))
    print("New list without uneven numbers: " + str(even_list))


orginal_list = [1,2,3,4,5,6,7,8,9,10]
num(orginal_list)

#phase 6

import math

p1_dia = int(input("Enter the diameter of the first pizza: "))
p1_price = int(input("Enter the price of the first pizza: "))
p2_dia = int(input("Enter the diameter of the second pizza: "))
p2_price = int(input("Enter the price of the second pizza: "))


def calc_p_price(diameter, price, name):
    areap = math.pi * (diameter / 2)**2
    return price / (areap * 0.0001)


def calc_area_m(diameter, price, name):
    areap = math.pi * (diameter / 2) ** 2
    print("The price per square meter of pizza", name, f": {price / (areap * 0.0001):.3f}")
    return price / (areap * 0.0001)


if calc_p_price(p1_dia, p1_price, 1) < calc_p_price(p2_dia, p2_price, 2):
    print(calc_area_m(p1_dia, p1_price,1))
    print("Pizza 1 is cheaper.")
elif calc_p_price(p1_dia, p1_price, 1) > calc_p_price(p2_dia, p2_price, 2):
    print(calc_area_m(p1_dia, p1_price, 2))
    print("Pizza 2 is cheaper.")
else:
    print("Same price.")
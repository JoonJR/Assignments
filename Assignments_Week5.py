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

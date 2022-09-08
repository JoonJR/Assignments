#phase 1

import random

dice_list = []
input_rolls = int(input("How many dices you want to roll: "))
rolls = 0
sum = 0
while rolls != input_rolls:
    rolls += 1
    dice_list.append(random.randint(1, 6))
print(dice_list)
for i in dice_list:
    sum += i
print("The sum of dices rolled is: " + str(sum))

#phase 2

numbers_list = []
print("Enter at least 5 numbers.")
numbers_input = input("Enter first number: ")
while numbers_input != "":
    numbers_list.append(numbers_input)
    numbers_input = input("Enter more numbers or leave empty to exit: ")
    if numbers_input == "":
        break

numbers_list2 = [eval(i) for i in numbers_list]
numbers_list2.sort(reverse=True)
print("Five greatest numbers in descending order are: ")
for i in numbers_list2[:5]:
    print(i)

#phase 3

num = int(input("Enter a integer to check if it is a prime number: "))

if num > 1:

    for i in range(2, int(num/2)+1):
         if (num % i) == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

#phase 4

#s_code1 = "NATO"
#s_code2 = "EU"


#answer = input("What is the secret code? ")
#if answer == s_code1:
#    print("Correct")
#elif answer == s_code2:
#    print("Also correct")
#    s_number = int(input("What is the secret number? "))
#    if s_number % 4 == 0:
#        print("You are lucky!")
#    else:
#        print("You are not lucky.")
#elif answer == "TOPSECRET":
#    print("You got it!!")
#else:
#    print("Incorrect")

#phase 1

#number = 1
#while number <= 1000:
#    modulo = number % 3
#    if modulo == 0:
#        print(str(number))
#    number = number + 1

#phase 2

#inches_input = float(input("Give a lenght in inches to convert it to centimeters: "))
#while inches_input >=0:
#    cm = inches_input * 2.54
#    print(f"This lenght in cm is: {cm:.2f}")
#    inches_input = float(input("Enter lenght in inches: "))

#phase 3

#input_number = int(input("Enter first number: "))
#smallest_number = input_number
#largest_number = input_number
#while input_number !="":
   # if input_number <= smallest_number:
  #      smallest_number = input_number
 #   if input_number >= largest_number:
#        largest_number = input_number
   # input_number = input("Enter new number or leave empty to finish")
  #  if input_number == "":
 #       break
#    input_number = int(input_number)
#print(f"The smallest number is: {smallest_number} and the largest number is: {largest_number}")

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


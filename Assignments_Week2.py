#exercise 1

fish_length = int(input("Enter length of the fish you caught in centimeters: "))
limit = 42
length_missing = limit - fish_length
if fish_length < limit:
    print("Release the fish back to the lake, it needs to grow " + str(length_missing) + " centimeters." )
else:
    print("The fish is over 42cm and it meets the size limit.")

#exercise 2

cabin_class = input("Enter the cabin class (LUX, A, B or C): ")
class_lux = "LUX"
class_a = "A"
class_b = "B"
class_c = "C"

if cabin_class == class_lux:
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == class_a:
    print("A: above the car deck, equipped with a window.")
elif cabin_class == class_b:
    print("B: windowless cabin above the car deck.")
elif cabin_class == class_c:
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#exercise 3

user_male = "M"
user_female = "F"
normal_hv = "Your hemoglobin value is normal."
low_hv = "Your hemoglobin value is lower than normal."
high_hv = "Your hemoglobin value is higher than normal."

user_gender = input("What is your biological gender? (M or F): ")
user_hv = int(input("What is your hemoglobin value? (g/l): "))
if user_gender == user_male:
    if user_hv >= 137 and user_hv <= 167:
        print(normal_hv)
    elif user_hv < 137:
        print(low_hv)
    elif user_hv > 167:
        print(high_hv)
elif user_gender == user_female:
    if user_hv >= 117 and user_hv <= 155:
        print(normal_hv)
    elif user_hv < 117:
        print(low_hv)
    elif user_hv > 155:
        print(high_hv)
else:
    print("Input error.")

#exercise 4

year = int(input("Enter a year to see if it's a leap year: "))
division_modulo_4 = year % 4
division_modulo_100 = year % 100
division_modulo_400 = year % 400
if division_modulo_4 == 0:
    if division_modulo_100 == 0 and division_modulo_400 !=0:
        print("This year is not a leap year.")
    else:
        print("This year is a leap year.")
else:
    print("This year is not a leap year.")

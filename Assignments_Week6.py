#phase 1

months_of_the_year = ("Winter", "Spring", "Summer", "Autumn")
month_number = int(input("Enter the number of a month (1-12): "))
year = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Season for that month is: ", months_of_the_year[year.index(month_number)//3])

#phase 2

names = set()
while True:
    name = str(input("Enter a name: "))
    if name in names:
        print("Name is already in the list")
    elif name != names:
        names.add(name)
    if name == "":
        break

for i in names:
    print(i)
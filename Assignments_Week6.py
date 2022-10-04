#phase 1

months_of_the_year = ("Winter", "Spring", "Summer", "Autumn")
month_number = int(input("Enter the number of a month (1-12): "))
year = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Season for that month is: ", months_of_the_year[year.index(month_number)//3])

#phase 2

names = set()
while True:
    name = input("Enter name to put in on the list: ")
    if name in names:
        print("Name is already on the list.")
    elif name != names:
        names.add(name)
    if name == "":
        break

for i in names:
    print(i)

#phase 3

airports = {"EFHK":"Helsinki-Vantaa Airport"}
while True:
    select = int(input("Select a option (1-3) \n1. Enter a new airport.\n2.Fetch airport information\n3. Quit.\n Enter your option : "))
    if select == 1:
        ICAO = input("Enter ICAO code of the airport: ")
        airport = input("Enter name of the airport: ")
        airports[ICAO] = airport
        print(airports)
    elif select == 2:
        ICAO = input("Enter ICAO code of the airport: ")
        if ICAO in airports:
            print(f"{ICAO} airport name is {airports[ICAO]}")
    elif select == 3:
        break
    else:
        print("Error. Wrong input, enter option (1-3)")

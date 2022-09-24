#exercise 1

import mysql.connector

connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database= 'flight_game',
        user= 'root',
        password= 'root',
        autocommit=True
        )

def geticao(airport_name):
    sql = "SELECT ident, airport.name, municipality FROM airport"
    sql += " WHERE ident='" + airport_name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in results:
            print(f"ICAO code: {row[0]} airports name is: {row[1]} and it is located in {row[2]}")
    return

airport_name = input("Enter ICAO code: ")
geticao(airport_name)

#exercise 2

def area_airports(area):
    sql = "SELECT airport.iso_country, country.name, airport.type, count(*) FROM airport, country"
    sql += " WHERE airport.iso_country = country.iso_country AND airport.iso_country='" + area + "' GROUP BY airport.type"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    if cursor.rowcount > 0:
        for row in results:
            print(f"{row[1]} has")
            print(f" {row[3]} {row[2]}")
    return


area = input("Enter the area code to see how many airports it has: ")
area_airports((area))
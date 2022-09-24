import mysql.connector
import geopy
from geopy import distance
#exercise 1


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
    if cursor.rowcount > 0:
        for row in results:
            print(f"{row[1]} has")
            print(f" {row[3]} {row[2]}")
    return


area = input("Enter the area code to see how many airports it has: ")
area_airports((area))

#excercise 3

def coordinates(icao1):
    sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao1 + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def coordinates(icao2):
    sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao2 + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


icao1 = input("Enter first ICAO code to calculate distance: ")
icao2 = input("Enter second ICAO code to calculate distance: ")
a = coordinates(icao1)
b = coordinates(icao2)

print(f"Distance between airports is: {distance.distance(a, b).kilometers:.1f} kilometers")
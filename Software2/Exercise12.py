# Exercise 1

import requests
request = 'https://api.chucknorris.io/jokes/random'
response = requests.get(request).json()
print(response["value"])

# Exercise 2
cityname = input("Enter a city name to check weather there: ")
request = (f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=0f2241f6e15ca941b24d11d94718fd2e&units=metric")
response = requests.get(request).json()
description = response["weather"][0]["description"]
temp = response["main"]["temp"]

print(f"City: {cityname}\nWeather description: {description}\nTemperature: {temp}°C")

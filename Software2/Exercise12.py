# Exercise 1
import requests
print("\n******************Exercise1******************\n")

request = 'https://api.chucknorris.io/jokes/random'
response = requests.get(request).json()
print(response["value"])

# Exercise 2
print("\n******************Exercise2******************\n")

cityname = input("Enter a city name to check weather there: ")
request = (f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=0f2241f6e15ca941b24d11d94718fd2e&units=metric")
try:
    response = requests.get(request)
    if response.status_code==200:
        response = response.json()
        description = response["weather"][0]["description"]
        temp = response["main"]["temp"]
        print(f"City: {cityname}\nWeather description: {description}\nTemperature: {temp}°C")
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")
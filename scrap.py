import requests


request = (f"https://api.openweathermap.org/data/2.5/weather?q=Helsinki&appid=0f2241f6e15ca941b24d11d94718fd2e&units=metric")
response = requests.get(request).json()
print(response["main"])

description = response["main"]["temp"]
print(description)
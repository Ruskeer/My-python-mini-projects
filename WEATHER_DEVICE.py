import requests
import json

api_key = "d0d78eceecbdec9a121d8eeba14aa3b3"  
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

# Personal variable (Uses built-in python f-string to insert values into the document given parameters: appid=, q=, units=)
complete_url = f"{base_url}appid={api_key}&q={city_name}&units=metric"

response = requests.get(complete_url)

x = response.json()

print(x)

if x.get("cod") == 200:
    y = x['main']

    current_temp = y['temp']
    current_humidity = y['humidity']
    current_pressure = y['pressure']

    z = x['weather'][0]
    description = z['description']

    print(f"Current Temperature: {current_temp} Celsius")
    print(f"Current Humidity: {current_humidity}")
    print(f"Current Pressure: {current_pressure}")
    print(f"STATUS: {description}")

else:
    print(f"\nServer Response: {x}")



import requests


from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")


url = "https://api.openweathermap.org/data/2.5/weather"




def weather_info(params):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data

    else:
        return None

while True:
    city = input("Enter a city name :")

    if city == "exit":
        break

    params = {
        "q" : city,
        "appid" : api_key,
        "units" : "metric"
    }

    data = weather_info(params)

    if data == None:
        print("Enter valid city")

    else:

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        wind_speed = data["wind"]["speed"]

        condition = data["weather"][0]["description"]


        print("="*25)
        print("Wheather Dashboard")
        print("="*25)
        print("\nTemperature:", temperature, "°C")
        print("Feels Like:", feels_like, "°C")
        print("Humidity:", humidity, "%")
        print("Pressure:", pressure, "hPa")
        print("Wind Speed:", wind_speed, "m/s")
        print("Condition:", condition)
        print("="*25)

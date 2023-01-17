# imports
import requests
import json

# ask the user which city they want 
ville = input("Which city do you want to get the weather information ? ")

# use the openweathermap API to retrieve city weather information
url = "http://api.openweathermap.org/data/2.5/weather?q=" + ville + "&appid=API_HERE"

# send a GET request to the openweathermap API
response = requests.get(url)

# verify that the request was successful
if response.status_code == 200:
    # transformer les données json en un dictionnaire python
    weather_data = json.loads(response.text)

    # display weather information
    print("Le temps actuel à " + ville + " est :")
    print("Description: " + weather_data["weather"][0]["description"])
    print("Température: " + str(weather_data["main"]["temp"]) + "°C")
    print("Humidité: " + str(weather_data["main"]["humidity"]) + "%")
    print("Pression: " + str(weather_data["main"]["pressure"]) + "hPa")
    print("Vent: " + str(weather_data["wind"]["speed"]) + "m/s")

else:
    print("An error occurred while retrieving weather information.")

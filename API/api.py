import requests
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

url = "http://api.openweathermap.org/data/2.5/weather?lat=46.5333&lon=6.6667&appid=8a8466dd96f8a2ffc48a71793b8449a5&lang=fr&units=metric"

r = requests.get(url)

#print(r.text)

data = r.json()

temp = data["main"]['temp']
feels = data["main"]['feels_like']
sky = data["weather"][0]['description']

print('\n\t************************************')
print('\t*           METEO LAUSANNE         *')
print('\t************************************')

print("\nDate : {}\n".format(dt_string))

print("La température d'aujourd'hui est de : {} °C \nMais la température resentie est de : {} °C\nSi nous levons la tête nous verrons : {}".format(temp, feels, sky))
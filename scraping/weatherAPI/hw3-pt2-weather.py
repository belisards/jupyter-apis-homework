# -*- coding: utf-8 -*-

import requests


docs = 'https://www.weatherapi.com/docs/'


print(f'The documentations URL is: {docs}')


weathernow = f'http://api.weatherapi.com/v1/current.json?key={my_key}&q={query}'


rio = requests.get(weathernow.replace('{query}','Rio+de+Janeiro')).json()


temp_c = rio['current']['temp_c']


print(f'In {rio["location"]["name"]} - a city based in {rio["location"]["country"]} - it is {temp_c} C degrees')


feelslike_c = rio['current']['feelslike_c']


if feelslike_c > temp_c:

  diff = feelslike_c - temp_c
    print(f"It feels {diff} degrees warmer")


if temp_c > feelslike_c:

  diff = temp_c - feelslike_c
    print(f"It feels {diff} degrees cooler")


heathrow = requests.get(weathernow.replace('{query}','iata:LHR')).json()


print(f'In Heathrow International Airport - it is {heathrow["current"]["temp_c"]} C degrees')


forecasts = f'http://api.weatherapi.com/v1/forecast.json?key={my_key}&q=iata:LHR&days=3'


print(f'The API endpoint for 3 days forecasts of Heathrow Airpoirt with my token is: {forecasts}')


response = requests.get(forecasts).json()['forecast']


print("Here are the dates:")

top_day = {}

total = len(response['forecastday'])


for i in range(total):
  date = response["forecastday"][i]["date"]
  max_temp_c = response["forecastday"][i]["day"]["maxtemp_c"]
  top_day[date] = max_temp_c
  print(f'{date} with {max_temp_c} degrees C as max. temp.')


print("This is the day with the highest maximum temperature in this forecast:")

print(sorted(top_day.items(), key=lambda day: day[1], reverse=True)[:1])


# -*- coding: utf-8 -*-
"""Sakshi Weather.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BW_K7VCUe6WkQ64YT1H26nUWQDLqjb6A
"""

import requests
from datetime import datetime

#Got API from openweathermap.org with mail valec91207@d4wan.com
api_key = '88637107e8cfdf1d6abd2b9216e91aee'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#Write the output to Report Weather file
with open("Report Weather.txt","w") as f:
    f.write("-------------------------------------------------------------\n")
    f.write(f"Weather Stats for - {location.upper()}  || { date_time}\n")
    f.write("-------------------------------------------------------------\n")
    #Writing the data
    f.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
    f.write(f"\nCurrent weather desc  :{weather_desc}")
    f.write(f"\nCurrent Humidity      :{hmdt}%")
    f.write(f"\nCurrent wind speed    :{wind_spd}kmph\n")
    f.write("\n-------------------------------------------------------------\n")

#Close the file
f.close()
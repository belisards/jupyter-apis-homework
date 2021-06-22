#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


get_ipython().system('pip3 install python-dotenv')


# # Be sure to restart your kernel after installing a package.

# In[2]:


import os
import requests
import datetime


# In[3]:


# Load the API key in the .env file

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

my_key = os.environ['my_key']


# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: This sure seems familiar.*

# In[4]:


city = 'Rio+de+Janeiro'
weathernow = f"http://api.weatherapi.com/v1/current.json?key={my_key}&q={city}"


# In[5]:


rio = requests.get(weathernow).json()


# In[6]:


temp_c = rio['current']['temp_c']
temp_c


# In[7]:


print(f'In {rio["location"]["name"]} - a city based in {rio["location"]["country"]} - it is {temp_c} C degrees')


# ## 2) What's the current wind speed, and how much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference. Same as we did last time!*

# In[8]:


print(f"The wind speed is {rio['current']['temp_c']} km per hour")


# In[9]:


feelslike_c = rio['current']['feelslike_c']


# In[10]:


if feelslike_c > temp_c:

  diff = round(feelslike_c - temp_c)

  print(f"It feels {diff} degrees warmer")


if temp_c > feelslike_c:

  diff = round(tempc - feelslike_c)

  print(f"It feels {diff} degrees cooler")


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible on next Thursday?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[11]:


# Adapted from the SO answer below
# https://stackoverflow.com/questions/6558535/find-the-date-for-the-first-monday-after-a-given-date
from datetime import date
today = date.today()

def next_weekday(d, weekday):
    days_ahead = weekday - today.weekday()
    # print(days_ahead)
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

next_thursday = next_weekday(today, 3) 
# 0 = Monday, 1=Tuesday, 2=Wednesday...


# In[12]:


forecasts = f'http://api.weatherapi.com/v1/forecast.json?key={my_key}&q={city}&dt={today}'


# In[13]:


print(f"The API endpoint about moons is: {forecasts.replace(my_key,'your_key')}")


# In[14]:


rio_forecast = requests.get(
    forecasts.replace('{date}',str(next_thursday))
    ).json()


# In[15]:


moon_visibility = rio_forecast['forecast']['forecastday'][0]['astro']['moon_illumination']


# In[16]:


print(f'Next Thursday the moon will be {moon_visibility}% visible')


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[17]:


rio_forecast_today = requests.get(
    forecasts.replace('{date}',str(today))
    ).json()


# In[18]:


min_c = rio_forecast_today['forecast']['forecastday'][0]['day']['mintemp_c']


# In[19]:


max_c = rio_forecast_today['forecast']['forecastday'][0]['day']['maxtemp_c']


# In[20]:


print(f'The difference is {round(max_c - min_c)} celsius degrees')


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[21]:


# Creating the variable names properly


# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next week's worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[22]:


hot_temp = 0

for day in range(0,7):
    date = next_weekday(today, day)
    forecasts = f'http://api.weatherapi.com/v1/forecast.json?key={my_key}&q={city}&dt={str(date)}'
    rio_forecast = requests.get(forecasts).json()
    high = rio_forecast['forecast']['forecastday'][0]['day']['maxtemp_c']
    if high > hot_temp:
        hot_temp = high
        hot_date = rio_forecast['forecast']['forecastday'][0]['date']
    if high >= 37:
        print(f"Hot day: {high} degrees Celsius on {date}")
    elif 29.5 < high < 37:
        print(f"Warm day: {high} degrees Celsius on {date}")
    else:
        print(f"Cold day: {high} degrees Celsius on {date}")
        
print(f'The hottest day week will be {hot_date} with {hot_temp} degrees Celsius.')


# # 6) What will be the hottest day in the next week? What is the high temperature on that day?

# In[23]:


# Described above.


# In[ ]:





# In[ ]:





# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[24]:


url = f"http://api.weatherapi.com/v1/forecast.json?key={my_key}&q=Miami&days=1"
response = requests.get(url, allow_redirects=True)
date = response.json()['forecast']['forecastday']

for item in date:
    hour = item['hour']
    for time in hour:
        temperature = time['temp_c']
        if time['cloud'] > 50:
            print(f"{time['time']}: {temperature} Celsius degrees and cloudy")
        else:
             print(f"{time['time']}: {temperature} Celsius degrees")


# In[ ]:





# In[ ]:





# # 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[25]:


counter = 0

#converting to celsius
temp_limit = round((85-32)*5/9,1)
temp_limit


# In[26]:


for item in date[0]['hour']:
    temperature = item['temp_c']
    #print(temperature)
    if temperature > temp_limit:
        counter = counter + 1

percent = round(counter/len(date[0]['hour'])*100)

print(f"{percent}% of the time the temperature will be above 85 degrees in fahrenheit or {temp_limit} in Celsius")


# ## 9) What was the temperature in Central Park on Christmas Day, 2020? How about 2012? 2007? How far back does the API allow you to go?
# 
# - *Tip: You'll need to use latitude/longitude. You can ask Google where Central Park is, it knows*
# - *Tip: Remember when latitude/longitude might use negative numbers*

# In[27]:


link = f"http://api.weatherapi.com/v1/history.json?key={my_key}&q=Central+Park&dt=2020-12-25"


# In[28]:


# Not available
requests.get(link).json()


# In[ ]:





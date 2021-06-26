# Adriano Belisário Feitosa da Costa
# Jun 12 2021
# Homework 1

from datetime import date as dt

############

# Variables
year = dt.today().year

# User's variables
birth = int(input("What is your birth year?"))

# 1- How old the user is
age = year - birth

# Creator's variables
my_birth_year = 1978
my_age = year - my_birth_year
years_diff = abs(my_age - age)

# Fixed variables :D
minutes_in_year = 60 * 24 * 365
one_million = 1000000

############

## Hearth beats rates
## Source: https://www.sjsu.edu/faculty/watkins/longevity.htm
## 2- How many times the user's heart has beaten
## 3 - How many times a blue whale's heart has beaten
## 4- How many times a rabbit's heart has beaten

hearth_beats_min = {
    'human':60,
    'whale':3,
    'rabbit':205,
}

human_beat = age * hearth_beats_min['human'] * minutes_in_year

rat_beat = age * hearth_beats_min['whale'] * minutes_in_year

rabbit_beat = age * hearth_beats_min['rabbit'] * minutes_in_year


# 5 - If the answer to rabbit heartbeats is more than a million, say "XXX million" instead of the very long raw number
if rabbit_beat > one_million:
    rabbit_beat = str(round(rabbit_beat/one_million)) + ' million'

############

## Planet years compared to Earth
## https://www.physicsclassroom.com/getattachment/reasoning/circularmotion/src18.pdf

planet_years = {
    'venus':0.615,
    'neptune': 165,
}

## 6- How old they are in Venus years
venus_years = round(age * planet_years['venus'])

## 7- How old they are in Neptune years
neptune_years = round(age * planet_years['neptune'])

############

## Functions
# 8- Whether they are the same age as you, older or younger
# 9-  If older or younger, how many years difference
def age_comparison(age):
    if age == my_age:
        print('We have the same age!')
    elif age < my_age:
        print(f'Btw, you are {years_diff} years younger than I!')
    elif age > my_age:
        print(f'And you are {years_diff} years older than I!')


# 10  If they were born in an even or odd year
if birth % 2 == 1:
    status_year = "odd"
else:
    status_year = "even"

# 11 How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)
# https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States
presidents_list = [
    {'name':'Eisenhower','party':'REP','start':1953,'end':1960},
    {'name':'John Kennedy','party':'DEM','start':1961,'end':1963},
    {'name':'Lyndon B. Johnson','party':'REP','start':1963,'end':1969},
    {'name':'Richard Nixon','party':'REP','start':1969,'end':1973},
    {'name':'Gerald Ford','party':'REP','start':1974,'end':1976},
    {'name':'Jimmy Carter','party':'DEM','start':1977,'end':1980},
    {'name':'Ronald Reagan','party':'REP','start':1981,'end':1988},
    {'name':'George  H. W. Bush','party':'REP','start':1989,'end':1992},
    {'name':'Bill Clinton','party':'DEM','start':1993,'end':2000},
    {'name':'George W. Bush','party':'REP','start':2001,'end':2008},
    {'name':'Barack Obama','party':'DEM','start':2009,'end':2016},
    {'name':'Donald Trump','party':'REP','start':2017,'end':2020},
    {'name':'Joe Biden','party':'DEM','start':2021,'end':''},
    ]

def presidents(birth):
  count = 0
  for single_president in range(0,len(presidents_list)):
    if presidents_list[single_president]['party'] == 'DEM' and presidents_list[single_president]['start'] >= birth:
        count = count + 1
  print(f'Since your year of birth we had {count} presidents from the Democratic Party')

 # Which US President was in office when they were born (1960 onward)
  for single_president in range(0,len(presidents_list)):
    if birth >= 1960 and (presidents_list[single_president]['start'] <= birth) and (birth <= presidents_list[single_president]['end']):
        name_president = presidents_list[single_president]['name']
        print(f'When you came to this world, {name_president} was the president of USA')
        

###########################
# If someone says they were born in the future, try asking them again (assume they'll do it right the second time).

if birth > year:
    print("Sorry, time traveler, this game is not for you :(")
else:
    print('Hi there!',
    f'It seems that you are {age} years old 🕐.',
    f'I estimate {human_beat} heart`s beat for you.',
    f'However, if you were a blue whale 🐋, your heart would have beaten {rat_beat} times',
    f'And if you were a rabbit 🐇 this number would be {rabbit_beat}',
    f'♀️ In Venus you would have {venus_years} years',
    f'🌊 In Neptune it would be {neptune_years}',
    sep='\n')

    age_comparison(age)

    presidents(birth)


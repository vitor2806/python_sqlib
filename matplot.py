from crud import *
import matplotlib.pyplot as plt

def countCity(cities, city):
    data_dict[city] = cities.count(city) # this will return an object with city: city occurences, if its already registered, will only sum
    return data_dict

data = select('cidade', 'alunos') # Get all cities from students table
data_dict = {}
cities = []

for item in data:
    cities.append(item['cidade']) # For each city append it to cities

for city in cities:
    countCity(cities, city) # For each city execute counter

num_cities = list(data_dict.values()) # since data_dict is city: occurences ordered, get all occurences value from it
name_cities = list(data_dict.keys()) # then get all city names

# Graphic config
title = 'student per city'
x = 'cities'
y = 'students'

plt.xlabel(x)
plt.ylabel(y)
plt.title(title)

# Graphic view
plt.bar(name_cities, num_cities)
plt.show()
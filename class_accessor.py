from classes import pets
from classes import country

#TO IMPORT SPECIFC CLASSES, USE from (filename) import (classname)
#IMPORTS USUALLY GO TOGETHER SO PUT THEM ALL AT THE TOP

fish = pets('fish', 'glub', 3)

print(fish.to_string())



mexico = country('mexico city', 133, 75)
australia = country('canberra', 28, 7)
us = country('washington d.c.', 343, 17)

print(mexico.capital_retriever())
print(australia.capital_retriever())
print(us.capital_retriever())

mexico.capital_changer('cacnoon')
print(mexico.capital_retriever())
import random


guitar = {
    'players': ['Stevie Ray Vaughn', 'Jimi Hendrix', 'Tim Henson', 'Slash'],
    'string count': 6,
    'type': 'string instrument',
    'tuning': 'standard'
}


for keys in guitar:
    print(f'Key: {keys}')
    print(f'Value(s): {guitar[keys]}')


print('Random Experimentation')

print(random.random())
#prints a random float from 0 to 1 excluding 1

print(random.random()*100 + 1)
#prints a random float from 1 to 101 excluding 101

print(random.randint(5, 10))
#prints a random integer from 5 to 10 including both

print(random.randrange(3, 98))
#prints a random integer from 3 to 98 excluding 98


print(range(len(guitar['players'])))

print(guitar['players'][1])

print(guitar['players'][random.randrange(0, len(guitar['players']))])
'''
The statement seen above is explained here:

1. You need len(guitar['players']) to find the length of the list you want to be randomized, and make their values integers
2. You put the outcome (which represents the total length of the list) of said function into random.randrange(0, x) to make the outcome random
2.5 It is good to note that the length of the function is only counting the amount of values and needs to be seen as a range for the random function
3. The random funtion's outcome is an integer so you must use guitar['players'][x] to access the list at that index
'''
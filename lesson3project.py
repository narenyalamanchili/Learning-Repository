house = {
    
    'bedroom': {
        'money': 3000,
        'TSR': 10,
        'SR': 3600
    },
    'bathroom': {
        'money': 3000,
        'TSR': 10,
        'SR': 3600
    },
    'kitchen': {
        'money': 3000,
        'TSR': 10,
        'SR': 3600
    },
    'family_room': {
        'money': 3001,
        'TSR': 10,
        'SR': 3600
    }

}

print(house)

for room in house:
    print(room)

# for sr in house:
#     print
print("\n")

print(house['bedroom']['SR'])

print('\n')



print(house.get('bedroom').get('SR'))

print('\n')

for room in house:
    print(house[room]['SR'])

print('\n')

high = 0

for room in house:
    if (house[room]['money'] > high):
        high = house[room]['money']

print(high)
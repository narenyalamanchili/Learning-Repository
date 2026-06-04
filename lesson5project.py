bad_guys = ['goons', 'thieves', 'criminals', 'bandits', 'murderers', 'robbers']

for x in range(len(bad_guys)):
    print(bad_guys[x])

y = 0

for x in bad_guys:
    print(x)

while y < len(bad_guys):
    if y % 2 == 1:
        print(bad_guys[y])
    y = y + 1


vehicles = {
    'cars': {
        'Lamborghini': {
            'cost': 197000,
            'size': 1200,
            'wheel': 4,
            'miles': 30000
        },
        'Ford': {
            'cost': 30000,
            'size': 1600,
            'wheel': 4,
            'miles': 27000
        },
        'Ferrari': {
            'cost': 200010,
            'size': 1150,
            'wheel': 4,
            'miles': 32000
        },
        'Toyota': {
            'cost': 12000,
            'size': 1400,
            'wheel': 4,
            'miles': 26000
        },
        'Chevrolet': {
            'cost': 50000,
            'size': 1400,
            'wheel': 4,
            'miles': 27500
        }
    },
    'trucks': {
        'DAF': {
            'cost': 75000,
            'size': 9000,
            'wheel': 14,
            'miles': 32000,
            'cc': 20
        },
        'Jeep': {
            'cost': 50000,
            'size': 1400,
            'wheel': 4,
            'miles': 22000,
            'cc': 4
        }
    }
}



for automobile in vehicles:
    for brands in vehicles[automobile]:
        if 'cc' in vehicles[automobile][brands]:
            print(f'{brands}: {vehicles[automobile][brands]['cc']}')

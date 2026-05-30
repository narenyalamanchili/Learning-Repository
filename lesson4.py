#global variables are declared outside functions, loops, and other things
#local variables are declared inside functions, loops, and other things
#local variables can only be accessed inside said function, loop, and other thing
#global variables can be accessed anywhere

solar_system = {
    'Earth': {
        'Moon': {
            'Water': 'Minimal',
            'PD': 384400
        },
        'SD': 93
    },
    'Saturn': {
        'Titan': {
            'PD': 1200000
        },
        
        'Mimas': {
            'Water': 'Mostly',
            'PD': 185520
        },
        'Dione': {
            'Water': 'Half',
            'PD': 377400
        },
        'SD': 886
    },
    'Jupiter': {
        
        'Europa': {
            'Water': 'Vast',
            'PD': 417000
        },
        'Ganymede': {
            'Water': 'Half',
            'PD': 1070400
        },
        'Io': {
            'PD': 262000
        },
        'SD': 484
    }

}


print(solar_system['Jupiter']['Europa']['Water'])

for planet in solar_system:
    for moon in solar_system[planet]:
        if type(solar_system[planet][moon]) == type({}):
            if ('Water' in solar_system[planet][moon]):
                if(solar_system[planet][moon]['Water'] == 'Half'):
                    print(moon)

# for planet in solar_system:
#     for moon in solar_system[planet]:
#         print(moon)

# if ('Water' in solar_system["Jupiter"]["Io"]):
#     print("YEAH")
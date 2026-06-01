family = {
    'pets': {
        'cat': {
            'age': 2,
            'cost': 250
        },
        'dog': {
            'age': 3,
            'cost': 250
        }
    },
    'people': {
        'father': {
            'salary': 5000,
            'age': 40
        },
        'mother': {
            'salary': 7000,
            'age': 38
        },
        'brother': {
            'allowance': 600,
            'age': 14
        },
        'sister': {
            'allowance': 600,
            'age': 17
        }
    }
}

for living in family:
    if (living == 'people'):
        for humans in family[living]:
            print(humans)
            print(family[living][humans]['age'])
            print(f'{humans}: {family[living][humans]['age']}')
            #PUTTING 2 STEPS TOGETHER
            #f STRING EASILY PUTS TWO CONCEPTS TOGETHER BY PUTTING {} AROUND ANYTHING THAT CONTAINS A VALUE
            #SAID VALUES THAT f STRINGS CAN CONTAIN CAN BE LISTS, DICTIONARIES, BOOLEANS AS WELL



money = 0

for living in family:
    if (living == 'pets'):
        for animals in family[living]:
            money = money - family[living][animals]['cost']
    if (living == 'people'):
        for humans in family[living]:
            if ('allowance' in family[living][humans]):
                money = money - family[living][humans]['allowance']
            if ('salary' in family[living][humans]):
                money = money + family[living][humans]['salary']


print(money)



# def dictionaryfunc(dictionary):
#     for x in dictionary:
        # print(me)
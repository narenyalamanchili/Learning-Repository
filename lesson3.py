#def FUNCTIONS
def me(gah):
    print('blah2', gah)
    return f'blah {gah}'
#def FUNCTION DOESN'T DO ANYTHING BUT DEFINE A PARAMETER AND WHENEVER THAT ORIGINAL FUNCTION APPEARS THE DEF FUNCTION ACTIVATES
#gah IS THE PARAMETER AND 4, 39, AND john ARE THE ARGUMENTS IN THIS CASE
me(4)
me(39)
x = me('john')
print(x)

# def password_identifier(password):
    # if (type(int(password)) == type (0)):
    #     if (password < 298):
    #         print('not')
    #     if (password > 298):
    #         print('good job')
    #     if (password == 298):
    #         print('who is this tho')

    # if (type(password) == type('lol')):
    #     if (password == f'298, benedict'):
    #         print('kill jerry')
    #     elif (password == 'password'):
    #         print('no\n\n\nbad')
    #     elif (password == '298, jerry'):
    #         print('your word passed')
    #     else:
    #         print('yeaaaaa...\n...nah')

# password_identifier(input('tell your password: '))


y = 55
if (y > 50 & y < 75):
    print(50, 75)
    

#DICTIONARIES ARE TYPES OF LISTS THAT STORE KEYS AND VALUES IN PAIRS
#brand IS THE KEY AND Ford WOULD BE THE VALUE
#ONE KEY AND VALUE PAIR WOULD BE CALLED AN ITEM
dictionary = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(dictionary['brand'])
print(dictionary.keys())
print(dictionary.values())
#KEYS AND VALUES ARE PRINTED USING THESE FUNCTIONS
dictionary['model'] = 'F150'
print(dictionary)
dictionary.update({'model': 'F150'})
print(dictionary)
#USING THE UPDATE FUNCTION OR SIMPLY MAKING THE KEY EQUAL SOMETHING ELSE CHANGES THE VALUE OF THE KEY TO SAID SOMETHING ELSE
dictionary.update({'tires': 'rubber'})
print(dictionary)
#THE UPDATE FUNCTION CAN ALSO ADD ITEMS TO THE DICTIONARY
dictionary.pop('tires')
print(dictionary)
#THE POP FUNCTION REMOVES ITEMS FROM THE DICTIONARY

for z in dictionary:
    print(dictionary[z])
for z in dictionary:
    print(z)
#YOU CAN MAKE DICTIONARIES LOOPS BY USING THE (for X in DICTIONARY:) FUNCTION



trees = {
    'Acacia': {
        'Leaf Color': 'Orange',
        'Trunk Color': 'Gray-ish Brown',
        'Avg. Height': 7.5
    },
    'Oak': {
        'Leaf Color': 'Bright Green',
        'Trunk Color': 'Brown',
        'Avg. Height': 22.5
    },
    'Pine': {
        'Leaf Color': 'Forest Green',
        'Trunk Color': 'Brown',
        'Avg. Height': 30
    }
}

print(trees)

print(trees['Oak']['Leaf Color'])
print(trees.get('Acacia').get('Trunk Color'))
#THESE ARE WAYS TO PRINT SPECIFIC VALUES FROM A DICTIONARY WITHIN A DICTIONARY

for tree in trees:
    print(trees[tree]['Leaf Color'])
#SINCE TREE REPRESENTS EACH SUB-DICTIONARY, THE LEAF COLOR OF EACH SUB-DICTIONARY WILL BE PRINTED THROUGH EACH LOOP

for tree in trees:
    if (trees[tree]['Trunk Color'] == 'Brown'):
        print(tree)
#IN THE DICTIONARY, IF BROWN IS THE TRUNK COLOR OF THE TREE BEING SHOWN, PRINT THAT TREE^^
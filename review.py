def stick_maker(sticks):
    if (sticks == 'broom'):
        print('sweep')


stick_maker(input('Stick Type: '))



big_cats = ['lion', 'tiger', 'jaguar', 'leopard', 'panther']

for x in big_cats:
    if len(x) <= 5:
        print(x)


for y in range(len(big_cats)):
    if y % 2 == 1:
        print(big_cats[y])
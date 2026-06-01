numbered = [2, 45, 25, 95, 4.6, 2.1, 909]

y = 0

for x in numbered:
    if (x > 50):
        print(x)

while (True):
    if (y > 3):
        break
    print(y)
    y = y + 1


def list_taker(list):
    z = 0
    while (z < len(numbered)):
        print(numbered[z])
        z = z + 1
    for integers in list:
        print(integers)

list_taker(numbered)

#while STATMENTS ARE if STATEMENTS THAT REPEAT AGAIN EVEN AFTER ALREADY BEING ACCOMPLISHED UNTIL THEY ARE NO LONGER TRUE
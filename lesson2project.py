numbers = [32, 42, 88, 48, 72, 25, 61, 97]
print(numbers)
sun = 0
for y in numbers:
    if y > 50:
        sun += y
print(sun)
print('The sum is', sun)
print(f'The sum is {sun}')

print('\\')

for y in range(len(numbers)):
    if (y % 2 != 0):
        print(numbers[y])

print('\\')

print(21, 'times')
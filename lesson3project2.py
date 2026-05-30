def size_name(name):
    if (len(name) < 6):
        return (f'Your name, {name}, is quite small')
    elif (len(name) > 6):
        return (f'Your name, {name}, is pretty big')
    elif (len(name) == 6):
        return (f'Your name, {name}, is average size')

print(size_name('Jerry'))
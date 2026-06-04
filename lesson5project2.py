def man(man):
    try:
        int(man)
    except:
        if (man == 'haha'):
            print('sorry')
        if (man == 'truth'):
            print('someday')
    else:
        print('Value: 0')

man(input(': '))
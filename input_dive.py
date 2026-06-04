def output_generator(output):
    
    try:
        int(output)
    except:
        if (output) == 'enel':
            print('god himself.')
        elif (output) == 'rapper':
            print('slim shady')
        elif (output) == 'white man':
            print('mayhaps')
        else:
            print('uhhhh yea sure')
    else:
        print("soon")
    finally:
        if (output) != '1.38':
            print('/killall')
    


output_generator(input('eminem?: '))
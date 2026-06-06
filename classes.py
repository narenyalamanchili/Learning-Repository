class game_console:
    def __init__(self, controller, games = None):
        self.controller = controller
        self.games = games

playstation = game_console('controller', ['spiderman', 'astrobot', 'forza'])
wii = game_console('remote', ['mariokart', 'wiisports', 'smashbros'])
print(wii.controller)
print(wii.games)
playstation.controller = 'null'
print(playstation.controller)
del(wii)



class pets:
    def __init__(self, name, sound, lifespan = 14):
        self.name = name
        self.sound = sound
        self.__lifespan = lifespan
    def to_string(self):
        print(f'{self.name}, {self.sound}, {self.__lifespan}')
    def set_lifespan(self, lifespan):
        self.__lifespan = lifespan
    def lifespan_grab(self):
        return self.__lifespan

dog = pets(['dog', 'puppy'],['bark', 'ruff', 'woof'])
cat = pets(['cat', 'kitty'],'meow')
hamster = pets('hamster','squeek', 3)
bird = pets('bird', ['chirp', 'caw'], 30)

print(dog.to_string())


#TO ENCAPSULATE A VARIABLE, PUT 2 _S BETWEEN self. AND SAID VARIABLE
#ENCAPSULATE BASICALLY MEANS TO PRIVATIZE
#IN THIS EXAMPLE THE ENCAPSULATED VARIABLE CAN NOT BE CALLED OUTSIDE OF THE CLASS AND NEEDS TO BE CALLED THROUGH A FUNCTION

dog.set_lifespan(12) #THIS FUNCTION WILL WORK

'print(self.__lifespan)' #THIS FUNCTION WILL NOT WORK




class country:
    def __init__(self, capital, population, hdi):
        self.__capital = capital
        self.population = population
        self.hdi = hdi
    def capital_retriever(self):
        return self.__capital
    def capital_changer(self, capital):
        self.__capital = capital
    
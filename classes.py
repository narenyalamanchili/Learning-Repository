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
        self.lifespan = lifespan
    # def to_string(self):
    #     print(f'{self.name}, {self.sound}, {self.lifespan}')

dog = pets(['dog', 'puppy'],['bark', 'ruff', 'woof'])
cat = pets(['cat', 'kitty'],'meow')
hamster = pets('hamster','squeek', 3)
bird = pets(['bird','chirp', 'caw'], 30)

print(dog.to_string())
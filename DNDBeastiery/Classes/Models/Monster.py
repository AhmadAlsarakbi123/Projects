class Dice:
    def __init__(self, name, hp, ac, actions, resistances, immunities):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.actions = actions
        self.resistances = resistances
        self.immunities = immunities
        self.speed = speed


    def roll(self):
        return random.randrange(1,self.sides)
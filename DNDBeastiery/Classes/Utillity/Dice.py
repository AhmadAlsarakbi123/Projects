import random
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randrange(1,self.sides)
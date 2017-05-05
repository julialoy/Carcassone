# Carcassone player class

class Player:

    def __init__(self, name, points=0):
        self.name = name
        self.points = points

    def update(self, value):
        self.points = self.points + value
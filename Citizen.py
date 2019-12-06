# Christopher Jones
# December 6, 2019
# HUM 414
# Utopia Project
# Citizen Class

import random


class Citizen:

    xlim = (0, 100)
    ylim = (0, 100)

    def __init__(self, name, money, health, stuff):
        self.name = name
        self.money = money
        self.health = health
        self.stuff = stuff
        self.coords = [random.randint(self.xlim[0], self.xlim[1]), random.randint(self.ylim[0], self.ylim[1])]
        self.money_history = []
        self.money_history.append(self.money)
        self.health_history = []
        self.health_history.append(self.health)

    def __str__(self):
        info = 'Name:{} Money:{} Health:{} Coordinates:{}'.format(self.name, self.money, self.health, self.coords)
        return info

    def update(self):
        buffer = 10
        # Orientations: up = 1, right = 2, down = 3, left = 4
        orientation = random.randint(1, 4)
        if orientation == 1 and self.coords[1] < (self.ylim[1] - buffer):
            self.coords[1] += buffer
        if orientation == 2 and self.coords[0] < (self.xlim[1] - buffer):
            self.coords[0] += buffer
        if orientation == 3 and self.coords[1] < (self.ylim[0] + buffer):
            self.coords[1] -= buffer
        if orientation == 4 and self.coords[0] < (self.xlim[0] + buffer):
            self.coords[0] -= buffer
        self.money_history.append(self.money)

        #Health update.
        if self.money < 50:
            self.health -= .1
            if self.money < 0:
                self.health -= .2
        else:
            if self.health > 0:
                self.health += 5
                if self.health > 100:
                    self.health = 100
        if self.health < 0:
            self.health = 0
        self.health_history.append(self.health)

    def get_coords(self):
        return self.coords


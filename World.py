# Christopher Jones
# December 6, 2019
# HUM 414
# Utopia Project
# World Class

import Citizen
import random
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np


class World:

    money = 100
    health = 100
    stuff = 5
    citizens = []
    days = 100
    area = 1000

    def __init__(self, population):
        self.population = population
        self.create_citizen()
        self.cycle()

    def create_citizen(self):
        for i in range(self.population):
            self.citizens.append(Citizen.Citizen(i, self.money, self.health, self.stuff))

    def update(self):
        for citizen in self.citizens:
            citizen.update()

    def cycle(self):
        buffer = 10
        for i in range(self.days):
            self.update()
            for j in range(self.population):
                for citizen in self.citizens:
                    if ((self.citizens[j].coords[0] - citizen.coords[0]) < buffer) and (self.citizens[j].name != citizen.name):
                        if (self.citizens[j].coords[1] - citizen.coords[1]) < buffer:
                            if random.randint(0, 1) == 1:
                                if self.citizens[j].health > 0 and citizen.health > 0:
                                    self.citizens[j].money -= 5
                                    citizen.money += 5
                                    self.citizens[j].stuff += 1
                                    citizen.stuff -= 1
        for citizen in self.citizens:
            self.plot(citizen)
        plt.savefig('HealthOver100.png')
        plt.show()


    def plot(self, citizen):
        #fig, axs = plt.subplots(2)
        #fig.suptitle('Money vs. Health: Citizen {}'.format(citizen.name))
        #axs[0].plot(citizen.money_history)
        #axs[1].plot(citizen.health_history)
        #if citizen.name == 3 or citizen.name == 24 or citizen.name == 45:
            #plt.savefig('citizen{}.png'.format(citizen.name), bbox_inches='tight')
        plt.suptitle('Health over 100 days')
        plt.plot(citizen.health_history)

import Citizen
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np


class TestAnim:

    money = 10
    health = 100
    citizens = []

    def __init__(self, population):
        self.population = population
        self.create_citizen()
        self.create_plot()

    def create_citizen(self):
        for i in range(self.population):
            self.citizens.append(Citizen.Citizen(i, self.money, self.health))
            print(self.citizens[i])

    def create_plot(self):
        plt.ion()
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set(xlim=(-100, 100), ylim=(-100, 100))
        for j in range(10):
            for i in range(self.population):
                sc = plt.scatter(self.citizens[i].coords[0], self.citizens[i].coords[1])
            plt.show()
            plt.close(fig)
            fig.gcf()

            self.update()

    def update(self):
        for citizen in self.citizens:
            citizen.update()

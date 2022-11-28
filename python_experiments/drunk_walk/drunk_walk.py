# create a program to calculate path of drunken walk
import random as r
from math import sqrt


class Drunk:
    def __init__(self, l=(0, 0)):
        self.l = l
        self.pm = ((1, 0), (0, 1), (-1, 0), (0, -1))
        self.s = 0

    def __str__(self):
        return f"This drunk is at location: {self.get_l()} and traveled {self.get_s()} steps being {self.get_d()} " \
               f"steps away from the origin"

    def get_l(self):
        return self.l

    def get_s(self):
        return self.s

    def get_d(self):
        return round(sqrt(self.l[0] ** 2 + self.l[1] ** 2), 1)

    def reset_l(self):
        self.l = (0, 0)

    def reset_s(self):
        self.s = 0

    def reset_all(self):
        self.reset_l()
        self.reset_s()

    def move1(self):
        self.l = tuple(map(lambda i, j: i + j, self.l, r.choice(self.pm)))
        self.s += 1

    def move(self, steps):
        for _ in range(steps):
            self.move1()

    def walk(self, steps):
        walk = []
        for _ in range(steps):
            self.move1()
            state = (self.get_l(), self.get_d())
            walk.append(state)
        return walk

    def walk_simulation(self, steps, trials, desc=False):
        walks = []
        for _ in range(trials):
            self.move(steps)
            walk = (self.get_l(), self.get_d())
            walks.append(walk)
            self.reset_all()
        distances = [walk[1] for walk in walks]
        locations = [walk[0] for walk in walks]
        min_d, max_d, = min(distances), max(distances)
        av_d = (max_d + min_d) // 2
        min_p, max_p = min(walks, key=lambda x: (sqrt(x[0][0] ** 2 + x[0][1] ** 2))), max(walks,key=lambda x: (sqrt(x[0][0] ** 2 +x[0][1] ** 2)))
        stats = (av_d, min_p, max_p)
        if desc == True:
            return print(f"After {trials} walks, the minimum distance is {min_d}, the maximum is {max_d} and the average is {av_d}")
        else:
            return locations, stats


# drunk = Drunk()
# walks, stats = drunk.walk_simulation(10, 10)
# drunk.walk_simulation(10, 10, desc=True)
# drunk.walk_simulation(10, 10, desc=True)
# drunk.walk_simulation(100, 100, desc=True)
# drunk.walk_simulation(100, 100, desc=True)
# drunk.walk_simulation(1000, 1000, desc=True)

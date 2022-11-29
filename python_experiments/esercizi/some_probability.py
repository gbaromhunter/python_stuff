import random as r
import math as m
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import statistics as s


class Coin(object):

    def __init__(self):
        self.p = ('Head', 'Tails')
        self.outcomes = []
        self.count = 0

    def __str__(self):
        return f"This is a coin with two faces: {self.p[0]} and {self.p[1]}. It had been tossed {self.get_count()} times. " \
               f"{self.get_heads()} times Heads and {self.get_tails()} times Tails. The Heads/Tails ratio is {self.get_ratio()}"

    def get_outcomes(self):
        return self.outcomes

    def get_p(self):
        return self.p

    def get_heads(self):
        return len([elem for elem in self.outcomes if elem == 'Heads'])

    def get_tails(self):
        return self.get_count() - self.get_heads()

    def reset(self):
        self.outcomes = []
        self.count = 0

    def numeric_outcome(self):
        mapped = map(lambda x: 1 if x==self.get_p()[0] else 0, self.get_outcomes())
        return list(mapped)

    def get_ratio(self):
        try:
            return self.get_heads() / self.get_count()
        except:
            return None

    def get_count(self):
        return self.count


    def toss(self, times=1):
        for _ in range(times):
            outcome = r.choice(self.p)
            self.count += 1
            self.outcomes.append(outcome)
        return outcome

def plot_bets(start, n):
    def bet(start):
        money = start
        tosses = 0
        c = Coin()
        while money > 0:
            t = c.toss()
            if t == "Head":
                tosses += 1
                money = 2 * money
            else:
                last = money
                money = 0
        return tosses, last
    def bets_res(start, n):
        return [bet(start) for i in range(n)]
    fig, ax = plt.subplots()
    ax.set_title(f"Maximum amount of money reached, {n} trials with {start} as starting bet.")
    sim = bets_res(start, n)
    xs = [x[0] for x in sim]
    ys = [x[1] for x in sim]
    ax.hist(ys, bins=20)
    return plt.show()

plot_bets(10, 10000)

# idea: if gambling with a coin, each time it's head you win double your money, each time it's tails you lose all.
# run a simulation to see after several bets your financial situation



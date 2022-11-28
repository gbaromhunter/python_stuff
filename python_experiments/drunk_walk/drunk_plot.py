from drunk_walk import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

drunk = Drunk()
steps = 25
trials = 25
locations, stats = drunk.walk_simulation(steps, trials)
dp = np.asarray(locations)
xs = np.asarray([x[0] for x in dp])
ys = np.asarray([x[1] for x in dp])
walk = drunk.walk(steps)
# xsteps = np.arange(steps)
yavdist = np.asarray([x[1] for x in walk])

fig, ax = plt.subplots(2)
ax[0].set_title("Destination points of the drunk after 25 steps. 25 trials.")
ax[0].scatter(xs, ys)
ax[1].set_title("Number of steps and distance")
ax[1].set_ylabel("Number of steps")
ax[1].set_xlabel("Distance from origin")
ax[1].plot(range(1,steps+1), yavdist)
fig.set_constrained_layout(True)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

sharenow = pd.read_excel("sharenow.xlsx", header=5)
uber = pd.read_excel("uber.xlsx", header=5)


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


x = range(1,31)
y1 = sharenow['Tasso di engagement']
y2 = uber['Tasso di engagement']

ax = plt.subplot(111)
plt.title("Tasso di engagement")
ax.plot(x, y1, color='b', label='Sharenow')
ax.plot(x, y2, color='g', label='Uber')
plt.xlabel("Giorni")

plt.legend()
plt.show()
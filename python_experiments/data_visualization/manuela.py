import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sharenow = pd.read_excel("sharenow.xlsx", header=5)
uber = pd.read_excel("uber.xlsx", header=5)

# Need to plot 3 graphics:
# 1) comparison between engagement of uber and sharenow as a linear graph
# 2) two pie charts showing count of post objectives
# 3) two linear graphs representing number of comments and likes for each company
#    best and worst commenst needs to be highlited, showing date, type and title


x = range(1,31)
y_sh = sharenow['Tasso di engagement']
y_ub = uber['Tasso di engagement']
fig, axs = plt.subplots(3, 2)



# First graph plot

axs[0].plot(x, y_sh, color='b', label='Sharenow')
axs[0].plot(x, y_ub, color='g', label='Uber')
axs[0].set_title("Tasso di engagement")
axs[0].set_xlabel("Giorni")
axs[0].legend()
plt.show()
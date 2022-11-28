import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.gridspec import GridSpec
import pandas as pd

# import data from excel files and load it into dataframe object
sharenow = pd.read_excel("sharenow.xlsx", header=5)
uber = pd.read_excel("uber.xlsx", header=5)

# def format_axes(fig):
#     for i,ax in enumerate(fig.axes):
#         # ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
#         ax.tick_params(size=1, width=1)

fig = plt.figure(figsize=(9, 11), tight_layout=True)

gs = GridSpec(3, 2, figure=fig)
ax1 = fig.add_subplot(gs[0, :2])
ax2 = fig.add_subplot(gs[1, 1])
ax3 = fig.add_subplot(gs[1, -2])
ax4 = fig.add_subplot(gs[-1, 1])
ax5 = fig.add_subplot(gs[-1, -2])
plt.style.use('ggplot')
fig.subplots_adjust(wspace=1, hspace=1)
# format_axes(fig)

# First graph

x = range(1, 31)
y_sh = sharenow["Tasso di engagement"]
y_ub = uber["Tasso di engagement"]

ax1.set_title("Tasso di engagement", fontdict={"fontsize": 10})
ax1.set_xlabel("Giorni", fontdict={"fontsize": 8})
ax1.set_ylabel("Engagement", fontdict={"fontsize": 8})
ax1.tick_params(axis="both", labelsize=8)
ax1.plot(x, y_sh, color='b', label='Sharenow', linewidth=1)
ax1.plot(x, y_ub, color='g', label='Uber', linewidth=1)
ax1.legend()

# Second and Third graph

sharenow_purpose = sharenow.groupby("Obiettivo Post (ricorrenza, real time, vendita prodotto, ecc)").size()
labels_sh = list(*sharenow_purpose.axes)
labels_sh[3] = "sconto sul servizio"
sizes_sh = list(sharenow_purpose)
uber_purpose = uber.groupby("Obiettivo Post (ricorrenza, real time, vendita prodotto, ecc)").size()
labels_ub = list(*uber_purpose.axes)
sizes_ub = list(uber_purpose)

ax2.set_title("Obiettivi post Sharenow", fontdict={"fontsize": 10})
ax2.pie(sizes_sh, labels=labels_sh, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
        textprops={"fontsize": 8})
ax2.axis('equal')

ax3.set_title("Obiettivi post Uber", fontdict={"fontsize": 10})
ax3.pie(sizes_ub, labels=labels_ub, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
        textprops={"fontsize": 8})
ax3.axis('equal')

# Fourth and Fifth graphs

y1_sh = sharenow['Numero di "Mi Piace"']
y1_ub = uber['Numero di "Mi Piace"']
ax4.set_title("Numero di Likes", fontdict={"fontsize": 10})
ax4.set_xlabel("Giorni", fontdict={"fontsize": 8})
ax4.set_ylabel("Likes", fontdict={"fontsize": 8})
ax4.tick_params(axis="both", labelsize=8)
ax4.plot(x, y1_sh, color='b', label='Sharenow', linewidth=1)
ax4.plot(x, y1_ub, color='g', label='Uber', linewidth=1)
# ax4.annotate('Miglior post', xy=(max(y1_ub)), xycoords='data',
#              xytext=(0.8, 0.95), textcoords='axes fraction',
#              arrowprops=dict(facecolor='black', shrink=0.05),
#              horizontalalignment='right', verticalalignment='top',
#              )

y2_sh = sharenow['Numero di commenti']
y2_ub = uber['Numero di commenti']
ax5.set_title("Numero di commenti", fontdict={"fontsize": 10})
ax5.set_xlabel("Giorni", fontdict={"fontsize": 8})
ax5.set_ylabel("Commenti", fontdict={"fontsize": 8})
ax5.tick_params(axis="both", labelsize=8)
ax5.plot(x, y2_sh, color='b', label='Sharenow', linewidth=1)
ax5.plot(x, y2_ub, color='g', label='Uber', linewidth=1)

plt.show()

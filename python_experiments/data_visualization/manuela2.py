# various graphics
import pandas as pd
import matplotlib.pyplot as plt


# import data from excel files and load it into dataframe object
sharenow = pd.read_excel("sharenow.xlsx", header=5)
uber = pd.read_excel("uber.xlsx", header=5)



x = range(1,31)
y1 = sharenow["Tasso di engagement"]
y2 = uber["Tasso di engagement"]

axl = plt.subplot(111)
plt.title("Tasso di engagement")
axl.plot(x, y1, color='b', label='Sharenow')
axl.plot(x, y2, color='g', label='Uber')

plt.legend()
plt.show()

# # How many comments types Sharenow
#
# sharenow_purpose = sharenow.groupby("Obiettivo Post (ricorrenza, real time, vendita prodotto, ecc)").size()
# labels = list(*(sharenow_purpose.axes))
# labels[3] = "sconto sul servizio"
# sizes = list(sharenow_purpose)
# # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
# fig1, ax1 = plt.subplots(figsize=(6, 6))
# plt.title("Obiettivi dei post di Sharenow", fontsize=18)
# ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.tight_layout()
# plt.show()
#
# # Uber
#
# uber_purpose = uber.groupby("Obiettivo Post (ricorrenza, real time, vendita prodotto, ecc)").size()
# labels = list(*(uber_purpose.axes))
# sizes = list(uber_purpose)
# # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
# fig1, ax1 = plt.subplots(figsize=(6, 6))
# plt.title("Obiettivi dei post di Uber", fontsize=18)
# ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.tight_layout()
# plt.show()
# sharenow_purpose = sharenow.groupby("Obiettivo Post (ricorrenza, real time, vendita prodotto, ecc)").size()
# labels_s = list(*(sharenow_purpose.axes))
# labels_s[3] = "sconto sul servizio"
# sizes_s = list(sharenow_purpose)
# fig, ax = plt.subplots(2, figsize=(6, 6))
# fig.suptitle("Obiettivi dei post")
# ax[0].title.set_text("Sharenow")
# ax[0].pie(sizes_s, labels=labels_s, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
# ax[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# # Uber
#
# uber_purpose = uber.groupby("Obiettivo Post (ricorrenza, real time, vendita prodotto, ecc)").size()
# labels_u = list(*(uber_purpose.axes))
# sizes_u = list(uber_purpose)
# ax[1].title.set_text("Uber")
# ax[1].pie(sizes_u, labels=labels_u, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
# ax[1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.tight_layout()
# plt.show()

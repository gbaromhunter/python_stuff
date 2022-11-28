# import matplotlib.pyplot as plt
# from matplotlib.gridspec import GridSpec
#
#
# def format_axes(fig):
#     for i, ax in enumerate(fig.axes):
#         ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
#         ax.tick_params(labelbottom=False, labelleft=False)
#
# fig = plt.figure(constrained_layout=True)
#
# gs = GridSpec(3, 3, figure=fig)
# ax1 = fig.add_subplot(gs[0, :2])
# ax2 = fig.add_subplot(gs[1, 0])
# ax3 = fig.add_subplot(gs[1, -2])
# ax4 = fig.add_subplot(gs[-1, 0])
# ax5 = fig.add_subplot(gs[-1, -2])
#
# fig.suptitle("GridSpec")
# format_axes(fig)
#
# plt.show()
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        # ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure(constrained_layout=True)

gs = GridSpec(3, 2, figure=fig)
ax1 = fig.add_subplot(gs[0, :2])
ax2 = fig.add_subplot(gs[1, 1])
ax3 = fig.add_subplot(gs[1, -2])
ax4 = fig.add_subplot(gs[-1, 1])
ax5 = fig.add_subplot(gs[-1, -2])

fig.suptitle("Sharenow VS Uber")
format_axes(fig)

plt.show()
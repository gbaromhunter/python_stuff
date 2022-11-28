"""Hello World application for Tkinter"""

from tkinter import *
from tkinter.ttk import *

root = Tk()
label = Label(root, text="Hello World")
label.pack()
label_2 = Label(root, text="Hello Universe")
label_2.pack()
button = Button(root, text="Click Me")
button.pack()
root.mainloop()
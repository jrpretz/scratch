
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from matplotlib.figure import Figure

from Tkinter import *

root = Tk()
f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = np.random.random(size=100)
s = np.random.random(size=100)

a.plot(t, s,'.')
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


def go():
    a.clear()
    t = np.random.random(size=100)
    s = np.random.random(size=100)

    a.plot(t,s,'.')
    canvas.show()

button = Button(root, text='Go', width=25, command=go)
button.pack()



mainloop()

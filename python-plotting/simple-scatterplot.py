import matplotlib.pyplot as plt
import matplotlib.ticker as tk
import numpy as np
import pylab

fig = plt.figure(figsize=(8,6))
inset = fig.add_subplot(111)

x1 = np.linspace(-10*np.pi,10*np.pi,1000)
y1 = np.sin(x1 * x1/100.)+1.2

x2 = np.linspace(-10*np.pi,10*np.pi,25)
y2 = np.sin(x2 * x2/100.) + np.random.normal(0,0.1,size=len(x2))+1.2
y2err = np.array([0.1] * len(x2))

#inset.set_xlim(0.1,1e8)
#inset.set_ylim(1e-10,1e-4)

inset.set_yscale("log", nonposx='clip')
#inset.set_xscale("log", nonposx='clip')

inset.plot(x1,y1,color='red')
inset.errorbar(x2,y2,yerr=y2err,fmt='o',color='black')

inset.set_xlabel("X axis")
inset.set_ylabel("Y axis")

plt.savefig('simple-scatterplot.png',bbox_inches='tight')

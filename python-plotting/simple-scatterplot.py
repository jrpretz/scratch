import matplotlib.pyplot as plt
import matplotlib.ticker as tk
import numpy as np
import pylab

fig = plt.figure(figsize=(8,6))
inset = fig.add_subplot(111)


inset.set_xlim(0.1,1e8)
inset.set_ylim(1e-10,1e-4)

inset.set_yscale("log", nonposx='clip')
inset.set_xscale("log", nonposx='clip')

inset.set_xlabel("Energy [GeV]")
inset.set_ylabel("E$^{2}$ dN/dE  [GeV/(cm$^{2}$ s sr)]")

plt.savefig('simple-scatterplot.png',bbox_inches='tight')

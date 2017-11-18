import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
#%matplotlib inline
fig = plt.figure(figsize=(11.7,8.3))

ax = fig.add_subplot(1,1,1)

# good ole N. America
y1 = 20.
y2 = 60.
x1 = -150.
x2 = -50.

m = Basemap(resolution='i',projection='merc', llcrnrlat=y1,urcrnrlat=y2,llcrnrlon=x1,urcrnrlon=x2)
m.drawcountries(linewidth=0.5)
m.drawcoastlines(linewidth=0.5)
m.drawstates(linewidth=0.5)
plt.savefig('map.png',dpi=300)

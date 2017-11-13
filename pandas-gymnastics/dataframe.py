import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

x = np.random.normal(size=1000)
y = np.random.normal(size=1000)
z = np.random.normal(size=1000)

data = pd.DataFrame({"x":x,"y":y,"z":z})

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(data["x"],data["y"],'.')

plt.savefig("x_vs_y.png")

if os.path.exists('data.h5'):
    os.remove('data.h5')
data.to_hdf('data.h5','data')


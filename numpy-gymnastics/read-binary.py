import numpy as np
import matplotlib.pyplot as plt

arr = np.fromfile("data.dat")

print len(arr)

data =  arr.reshape(100,4)

plt.plot(data[:,0],data[:,1])
plt.plot(data[:,0],data[:,2])

plt.savefig("read-binary.png")

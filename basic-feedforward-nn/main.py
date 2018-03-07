import numpy as np
import matplotlib.pyplot as plt
from nnutil import init_network
from nnutil import forward_propagate
from nnutil import backward_propagate
from nnutil import softmax

np.random.seed(42)

X = np.random.randn(2,75)*0.2
y = np.zeros(shape=(3,75))
y_enc = np.zeros(75)

sel = (y % 3 == 0)
for i in range(0,75):
    if i % 3 == 0:
        X[:,i] = X[:,i] + np.array([-0.7,0.5])
        y[:,i] = np.array([1.0,0.0,0.0])
        y_enc[i] = 0

    if i % 3 == 1:
        X[:,i] = X[:,i] + np.array([0.7,0.5])
        y[:,i] = np.array([0.0,1.0,0.0])
        y_enc[i] = 1
        
    if i % 3 == 2:
        X[:,i] = X[:,i] + np.array([0.0,-1.0])
        y[:,i] = np.array([0.0,0.0,1.0])
        y_enc[i] = 3



network = init_network()
network["a0"] = X


for epoch in range(1,100):
    forward_propagate(1,network)

    probs = softmax(network["a2"])

    cost = np.sum(y * np.log(probs))
    print(epoch,cost)

    network["da2"] = probs - y
    backward_propagate(2,network)

    for param in ["W1","W2","b1","b2"]:
        network[param] = network[param] - 0.5 * network["d" + param]

X_region = np.random.random(size=(2,10000)) * 4. - 2.

network["a0"] = X_region
forward_propagate(1,network)
pred = np.argmax(network["a2"],axis=0)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(X_region[0,:],X_region[1,:],c=pred,alpha=0.2)
plt.savefig("classification.png")
        

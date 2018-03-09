import numpy as np
import matplotlib.pyplot as plt
from nnutil import init_network
from nnutil import forward_propagate
from nnutil import backward_propagate
from nnutil import softmax

np.random.seed(42)

# generating a fake (easily trained) multi-class classification
# dataset
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


# create the network and set the input
network = init_network()
network["a0"] = X

# Train for 100 epochs. This is a very 'hands on' training,
# pedagogically showing the computation.
epochs = []
costs = []
for epoch in range(1,100):
    epochs.append(epoch)
    
    # propagate to the end
    forward_propagate(1,network)

    # compute the softmax activation
    probs = softmax(network["a" + str(network["depth"])])

    # the cost
    cost = -np.sum(y * np.log(probs))
    print(epoch,cost)
    costs.append(cost)

    # derivative of the cost wrt softmax activations
    network["da" + str(network["depth"])] = probs - y

    # and the backpropagation
    backward_propagate(network["depth"],network)

    # gradient descent on the parameters
    for i in range(1,network["depth"]+1):
        for param_prefix in ["W","b"]:
            param = param_prefix + str(i)
            network[param] = network[param] - 0.5 * network["d" + param]

# just a bunch of points to see the shape of the trained network            
X_region = np.random.random(size=(2,10000)) * 4. - 2.

network["a0"] = X_region
forward_propagate(1,network)
pred = np.argmax(network["a" + str(network["depth"] )],axis=0)

# just a summary plot
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.scatter(X_region[0,:],X_region[1,:],c=pred,alpha=0.2)
ax2.plot(epochs,costs)
ax1.set_xlabel("x0")
ax1.set_ylabel("x1")


ax2.set_yscale("log", nonposy='clip')
ax2.set_xlabel("epoch")
ax2.set_ylabel("cost")
plt.savefig("classification.png")
        

import numpy as np

def softmax(z):
    exps = np.exp(z)
    return exps/(np.sum(exps,axis=0))

class sigmoid_activation:
    def eval(self,z):
        print(z)
        return 1./(1+np.exp(-z))

    def evald(self,z):
        ret = self.eval(z)
        return ret * (1-ret)

class linear_activation:
    def eval(self,z):
        return z

    def evald(self,z):
        return np.ones(shape=z.shape)

class tanh_activation:
    def eval(self,z):
        return np.tanh(z)

    def evald(self,z):
        t = np.tanh(z)
        return 1.-t**2
        
def init_network():
    network = {}
    network["W1"] = np.random.randn(10,2)
    network["b1"] = np.random.randn(10,1)
    network["W2"] = np.random.randn(3,10)
    network["b2"] = np.random.randn(3,1)
    network["activation1"] = tanh_activation()
    network["activation2"] = linear_activation()
    network["depth"] = 2
    return network

# start forward propagation at layer 1 (not 0)
def forward_propagate(l,network):
    depth = network["depth"]
    if (l > depth):
        return 

    a_prev = network["a"+str(l-1)]
    W = network["W"+str(l)]
    b = network["b" + str(l)]

    activation = network["activation" + str(l)]
    network["z" + str(l)] = np.matmul(W,a_prev) + b
    network["a" + str(l)] = activation.eval(np.matmul(W,a_prev) + b)

    forward_propagate(l+1,network)

def backward_propagate(l,network):
    if l == 0:
        return
    
    da = network["da" + str(l)]
    z = network["z"+str(l)]

    m = da.shape[1]
    
    activation = network["activation" + str(l)]
    network["dz" + str(l)] = dz = da * activation.evald(z)

    network["dW" + str(l)] = (1./m) * np.matmul(dz,network["a" + str(l-1)].T)
    network["db" + str(l)] = (1./m) * np.sum(dz, axis = 1, keepdims = True)

    network["da" + str(l-1)] = np.matmul(network["W" + str(l)].T,dz)
    backward_propagate(l-1,network)
    
    

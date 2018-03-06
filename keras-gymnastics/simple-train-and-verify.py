# simple keras network
# 
# just verifying that the guts work as advertised. Train a simple
# network, get the trained parameters, and apply them 'by hand' and
# compare the answers to what you get asking the network to do it itself


import numpy as np
import tensorflow as tf
import keras
import matplotlib.pyplot as plt

# activation functions
def relu(x):
    return x * (x>0)

def sigmoid(x):
    return 1./(1+np.exp(-x))

# reproducibility
np.random.seed(50)

# assemble a simple training set
X_train = np.zeros(shape=(100,2))
y_train = np.zeros(shape=(100,1))

r = np.random.random(size=100)
phi = np.random.random(size=100) * 2 * 3.14158

X_train[:,0] = r * np.sin(phi)
X_train[:,1] = r * np.cos(phi)
sel = (X_train[:,0]>0)
y_train[sel] = 1

# the network: 
# 2 inputs 
# 10-activation hidden layer (relu activation)
# one output with sigmoid activation

X_input = keras.layers.Input((2,))

layer1 = keras.layers.Dense(10, activation='relu') 
X = layer1(X_input)

layer2 = keras.layers.Dense(1, activation='sigmoid')
X = layer2(X)

model = keras.models.Model(inputs = X_input, outputs = X, name='model')
model.compile('adam', 'binary_crossentropy', metrics=['accuracy'])

# fit the model
model.fit(x=X_train,y=y_train,epochs=100)

# fitted wieghts
W1 = layer1.get_weights()[0]
b1 = layer1.get_weights()[1]

W2 = layer2.get_weights()[0]
b2 = layer2.get_weights()[1]

print("W1.shape",W1.shape)
print("b1.shape",b1.shape)
print("W2.shape",W2.shape)
print("b2.shape",b2.shape)

# making a prediction 'by hand' using the learned weights
z1 = np.matmul(X_train,W1) + b1
a1 = relu(z1)

z2 = np.matmul(a1,W2) + b2
a2 = sigmoid(z2)

# a prediction from the model itself
pred = model.predict(x=X_train)

for i in range(0,len(pred)):
    print(i,pred[i][0],"=?=",a2[i][0])
    

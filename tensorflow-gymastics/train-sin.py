import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

np.random.seed(42)

def forwardprop(X, w_1,b_1, w_2,b_2):
    h    = tf.nn.sigmoid(tf.matmul(X, w_1)+b_1)  # The \sigma function
    #yhat = tf.nn.sigmoid(tf.matmul(h, w_2)+b_2)  # The \varphi function
    yhat = tf.matmul(h, w_2)+b_2
    return yhat

def untrained_weights():
    w_1 = tf.Variable(tf.random_normal((1,24), stddev=0.1))
    b_1 = tf.Variable(tf.random_normal((1,24), stddev=0.1))
    w_2 = tf.Variable(tf.random_normal((24,1), stddev=0.1))
    b_2 = tf.Variable(tf.random_normal((1,1), stddev=0.1))
    return (w_1,b_1,w_2,b_2)

N = 1600

X_train = np.zeros(shape=(N,1))
y_train = np.zeros(shape=(N,1))

X_train[:,0] = np.random.random(N) * 6.28 * 2 - 6.28
y_train[:,0] = np.sin(X_train[:,0]) + np.random.random(N)*0.2 - 0.4


X = tf.placeholder(tf.float32 , shape=(None, 1),name="X")
y = tf.placeholder(tf.float32 , shape=(None, 1),name="y")

w_1,b_1,w_2,b_2 = untrained_weights()

h = forwardprop(X,w_1,b_1,w_2,b_2)
sess=tf.Session()

#cost    = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=h))
cost = tf.reduce_mean((h-y)*(h-y))
updates = tf.train.MomentumOptimizer(learning_rate=0.1,momentum=0.1).minimize(cost)
#updates = tf.train.GradientDescentOptimizer(0.5).minimize(cost)

sess.run(tf.global_variables_initializer())

plottedEpochs = [0,1,5,10,20,30,40,50,200,500]

if True:
    for epoch in range(501):
        perm = np.random.permutation(y_train.shape[0])

        X_tmp = X_train[perm,:]
        y_tmp = y_train[perm,:]
    
    
        for i in range(int(y_train.shape[0]/5)):
            low = i*5
            high = (i+1)*5
            sess.run(updates,feed_dict={X: X_tmp[low:high,:], y: y_tmp[low:high]})
        print("%d %f"%(epoch,sess.run(cost,feed_dict={X: X_train, y: y_train})))
        
        if epoch in plottedEpochs:
            
            p = sess.run(h,feed_dict={X:X_train})

            plt.plot(X_train[:,0],p,'.',label="%d"%(epoch))

p = sess.run(h,feed_dict={X:X_train})
plt.plot(X_train[:,0],y_train[:,0],'.',label="training")
plt.legend(loc='upper right')
plt.savefig("tf-sin.png")

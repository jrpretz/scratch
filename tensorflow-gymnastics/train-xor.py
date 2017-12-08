import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
root_logdir = "tf_logs"
logdir="{}/run-{}/".format(root_logdir,now)

#%matplotlib inline

def forwardprop(X, w_1,b_1, w_2,b_2):
    h    = tf.nn.sigmoid(tf.matmul(X, w_1)+b_1)  # The \sigma function
    #yhat = tf.nn.sigmoid(tf.matmul(h, w_2)+b_2)  # The \varphi function
    yhat = tf.matmul(h, w_2)+b_2
    return yhat

def untrained_weights():
    w_1 = tf.Variable(tf.random_normal((2,12), stddev=0.1))
    b_1 = tf.Variable(tf.random_normal((1,12), stddev=0.1))
    w_2 = tf.Variable(tf.random_normal((12,1), stddev=0.1))
    b_2 = tf.Variable(tf.random_normal((1,1), stddev=0.1))
    return (w_1,b_1,w_2,b_2)

N = 1600

X_train = np.zeros(shape=(N,2))
y_train = np.zeros(shape=(N,1))

x1 = np.random.normal(loc=1,scale=0.15,size=400)
x2 = np.random.normal(loc=1,scale=0.15,size=400)
X_train[0:400,0] = x1
X_train[0:400,1] = x2
y_train[0:400,0] = np.zeros(shape=400)

x1 = np.random.normal(loc=1,scale=0.15,size=400)
x2 = np.random.normal(loc=0,scale=0.15,size=400)
X_train[400:800,0] = x1
X_train[400:800,1] = x2
y_train[400:800,0] = np.ones(shape=400)

x1 = np.random.normal(loc=0,scale=0.15,size=400)
x2 = np.random.normal(loc=1,scale=0.15,size=400)
X_train[800:1200,0] = x1
X_train[800:1200,1] = x2
y_train[800:1200,0] = np.ones(shape=400)

x1 = np.random.normal(loc=0,scale=0.15,size=400)
x2 = np.random.normal(loc=0,scale=0.15,size=400)
X_train[1200:1600,0] = x1
X_train[1200:1600,1] = x2
y_train[1200:1600,0] = np.zeros(shape=400)


#sel = np.where(y[:,0] > 0.5)
#x1_plt = X[:,0]
#x2_plt = X[:,1]
#plt.plot(x1_plt[sel],x2_plt[sel],'.')
#sel = np.where(y[:,0] < 0.5)
#plt.plot(x1_plt[sel],x2_plt[sel],'.')

X = tf.placeholder(tf.float32 , shape=(None, 2),name="X")
y = tf.placeholder(tf.float32 , shape=(None, 1),name="y")

w_1,b_1,w_2,b_2 = untrained_weights()

h = forwardprop(X,w_1,b_1,w_2,b_2)
sess=tf.Session()

cost    = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=h))
updates = tf.train.MomentumOptimizer(learning_rate=0.1,momentum=0.1).minimize(cost)
#updates = tf.train.GradientDescentOptimizer(0.5).minimize(cost)
cost_summary = tf.summary.scalar('Cost',cost)
file_writer = tf.summary.FileWriter(logdir,tf.get_default_graph())

sess.run(tf.global_variables_initializer())

for epoch in range(100):
    perm = np.random.permutation(y_train.shape[0])

    X_tmp = X_train[perm,:]
    y_tmp = y_train[perm,:]
    
    
    #for i in range(int(y_train.shape[0]/5)):
    #    low = i*5
    #    high = (i+1)*5
    #    sess.run(updates,feed_dict={X: X_tmp[low:high,:], y: y_tmp[low:high]})
    #print("%d %f"%(epoch,sess.run(cost,feed_dict={X: X_train, y: y_train})))

    
    for i in range(0,N):
        sess.run(updates,feed_dict={X: X_train[i:i+1,:],y:y_train[i:i+1,:]})
    sess.run(updates,feed_dict={X: X_train,y:y_train})
    print("%d %f"%(epoch,sess.run(cost,feed_dict={X: X_train, y: y_train})))
    summary_str = sess.run(cost_summary,feed_dict={X: X_train, y: y_train})
    file_writer.add_summary(summary_str,epoch)

file_writer.close()


X_phase = np.zeros(shape=(10000,2))
spc = np.linspace(-0.5,1.5,100)
for i in range(0,100):
    for j in range(0,100):
        X_phase[i * 100 + j][0] = spc[i]
        X_phase[i * 100 + j][1] = spc[j]

pred = tf.nn.sigmoid(h)

pred_val = sess.run(pred,feed_dict={X: X_phase})

predictions = np.where(pred_val > 0.5)

#plt.plot(y_train,pred_val,'o',alpha=0.3)
c = plt.scatter(X_phase[:,0],X_phase[:,1],c=pred_val.reshape(10000))

x1_plt = X_train[:,0]
x2_plt = X_train[:,1]
sel = np.where(y_train[:,0] > 0.5)

plt.plot(x1_plt[sel],x2_plt[sel],'.',color='white')
sel = np.where(y_train[:,0] < 0.5)
plt.plot(x1_plt[sel],x2_plt[sel],'.',color='red')

plt.colorbar(c)
plt.savefig("train-xor.png")

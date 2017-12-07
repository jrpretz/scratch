import numpy as np
import tensorflow as tf
import sys
from sklearn import datasets
from sklearn import metrics

# for reproducibility
tf.set_random_seed(42)

# init random weights
w_1 = tf.Variable(tf.random_normal((4,16), stddev=0.1))
b_1 = tf.Variable(tf.random_normal((1,16), stddev=0.1))
w_2 = tf.Variable(tf.random_normal((16,3), stddev=0.1))
b_2 = tf.Variable(tf.random_normal((1,3), stddev=0.1))

# the neural network.
# note that the 'softmax_cross_entropy_with_logits' cost function
# includes the 'softmax' part
def forward(X,w_1,b_1,w_2,b_2):
    h = tf.nn.sigmoid(tf.matmul(X,w_1)+b_1)
    yhat = tf.matmul(h,w_2)+b_2
    return yhat

# not interested in splitting into train/test cause i'm only
# interested in the mechanism of creating/training a NN with tensorflow
iris = datasets.load_iris()

# arranging the data for multi-class classification
X_train = iris.data
nFeatures = X_train.shape[1]
y_train_labels = iris.target
labels = np.unique(y_train_labels)
nLabels = len(labels)
y_train = np.zeros(shape=(y_train_labels.shape[0],nLabels))

for i in range(len(labels)):
    y_train[:,i][np.where(y_train_labels == labels[i])] = 1.0

# the tensorflow tensors for the NN output, the predictions,
# the cost function and a minimization algorithm
sess = tf.Session()

X = tf.placeholder(tf.float32 , shape=(None,nFeatures ),name="X")
y = tf.placeholder(tf.float32 , shape=(None,nLabels),name="y")

h = forward(X,w_1,b_1,w_2,b_2)
y_pred = tf.nn.softmax(h)
cost = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=h))
updates = tf.train.AdamOptimizer(0.1).minimize(cost)

# needed to run with variables
sess.run(tf.global_variables_initializer())

# 1000 epochs of training
for epoch in range(1000):
    sess.run(updates,feed_dict={X: X_train, y: y_train})
    print("%d %f"%(epoch,sess.run(cost,feed_dict={X: X_train, y: y_train})))

# classification report
# N.B. it's not best practices to use the training dataset for this, but idc right now
prediction = np.argmax(sess.run(y_pred,feed_dict={X: X_train, y: y_train}),
                       axis=1)

print(metrics.classification_report(y_train_labels,prediction))

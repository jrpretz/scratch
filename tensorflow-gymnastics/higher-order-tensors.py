import tensorflow as tf
import numpy as np

a = np.zeros(shape=(2,2))

a[0][0] = 1
a[1][1] = 1

A = tf.Variable(a,dtype=np.float64)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

print(sess.run(A))


X = tf.placeholder(shape=(None,2,2),dtype=tf.float64)

x_tmp = np.random.uniform(-1,1,size=(100,2,2))
x_tmp = x_tmp.astype(dtype=np.float64)

#X.reshape(
#tot = tf.batch_matmul(X,A)

def mult(x):
    return tf.matmul(x,a)

#tot = tf.scan(lambda a, x: tf.matmul(x, U), embed)

tot = tf.map_fn(mult,X)

print(sess.run(tot,feed_dict={X:x_tmp}))
print("-----------")
print(sess.run(tot,feed_dict={X:tot}))


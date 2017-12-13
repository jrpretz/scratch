import tensorflow as tf
import numpy as np


input2 = [ 2*x for x in range(100) ]
input2 = np.array(input2,dtype=np.float64).reshape(1,100)
input2_tf = tf.Variable(input2,dtype=tf.float64)

input = [ x for x in range(100) ]
input = np.array(input,dtype=np.float64).reshape(1,100)
input_tf = tf.Variable(input,dtype=tf.float64)


input_union = tf.concat([input_tf,input2_tf],axis=1)


input_tf_10_10 = tf.reshape(input_tf,(10,10))

input_slice = tf.slice(input_tf,[0,10],[1,10])

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    print(sess.run(input_tf))

    print(sess.run(input_tf_10_10))

    print(sess.run(input_union))

    print(sess.run(input_slice))

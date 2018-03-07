import tensorflow as tf
import numpy as np

x = tf.placeholder(dtype=tf.float32)

stack = tf.stack([x,x*x,x*x*x,x*x*x*x])

stackstack = tf.stack([stack,stack])

unstack_0,unstack_1,unstack_2,unstack_3 = stack[0],stack[1],stack[2],stack[3]

with tf.Session() as sess:
    print(sess.run(stack,feed_dict={x:4}))
    print(sess.run([unstack_0,unstack_1,unstack_2,unstack_3],feed_dict={x:4}))


column = stackstack[:,0]
with tf.Session() as sess:
    print(sess.run(stackstack,feed_dict={x:4}))
    print(sess.run(column,feed_dict={x:4}))

import tensorflow as tf

sess = tf.Session()

x = tf.Variable(5.0)
y = tf.Variable(-5.0)

f = x * x + y * y

init = tf.global_variables_initializer()
sess.run(init)

sess.run(f)

updates = tf.train.GradientDescentOptimizer(0.3).minimize(f,var_list=[x,y])

for i in range(0,50):
    sess.run(updates)
    print(sess.run(f),sess.run(x),sess.run(y))

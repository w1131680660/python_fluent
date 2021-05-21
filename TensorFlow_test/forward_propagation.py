import tensorflow as tf
tf.compat.v1.disable_eager_execution() # 禁用急切执行
print(tf.__version__)
w1 = tf.Variable(tf.random.normal((2,3),stddev=1,seed=1))
w2 = tf.Variable(tf.random.normal((3,1),stddev=1,seed=1))

x = tf.constant([[0.7,0.9]])

a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

sess = tf.compat.v1.Session()
sess.run(w1.initializer)
sess.run(w2.initializer)
print(sess.run(y))
init_op = tf.compat.v1.global_variables_initializer()
sess.run(init_op)

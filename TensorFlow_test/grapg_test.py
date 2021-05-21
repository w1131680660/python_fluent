import tensorflow as tf

# g1 = tf.Graph()
# with g1.as_default():
#     v = tf.compat.v1.get_variable('v',shape =[1],)
#     print(v)
#
# g2 = tf.Graph()
# with g2.as_default():
#     v = tf.compat.v1.get_variable('v',shape =[1],)
#
# with tf.compat.v1.Session(graph = g1) as sess:
#     # print(sess.run(tf.compat.v1.get_variable))
#     sess.run(tf.compat.v1.get_variable)
#     with tf.variable_creator_scope('',reuser=True):
#         print(sess.run(tf.compat.v1.get_variable('v')))


g = tf.Graph()
with g.as_default():
    a = tf.constant([[10,10],[11.,1.]])
    x = tf.constant([[1.,0.],[0.,1.]])
    b = tf.Variable(12.)
    y = tf.matmul(a, x) + b
    init_op = tf.compat.v1.disable_eager_execution()
with tf.compat.v1.Session() as sess:
    sess.run(y)
    # print(sess.run(y))
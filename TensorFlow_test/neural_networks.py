import tensorflow as tf
from numpy.random import RandomState

tf.compat.v1.disable_eager_execution()
batch_size = 8
w1 = tf.Variable(tf.compat.v1.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.compat.v1.random_normal([3,1], stddev=1, seed=1 ))

x = tf.compat.v1.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.compat.v1.placeholder(tf.float32, shape=(None, 1), name='y-input')

# 定义前向传播
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数以及后向传播算法
y = tf.sigmoid(y)
cross_entropy = -tf.reduce_mean(
                 y_ * tf.compat.v1.log(tf.clip_by_value(y, 1e-10, 1.0))
                 + (1 - y_) * tf.compat.v1.log(tf.clip_by_value(1-y,1e-10, 1.0)))

# train_step = tf.compat.v1.train.AdamOptimizer(0.001).minimize(cross_entropy)
# cross_entropy = -tf.reduce_mean(
#                  y_ * tf.compat.v1.log(tf.clip_by_value(y, 1e-10, 1.0))
#                                 + (1 - y_) * tf.compat.v1.log(tf.clip_by_value(1 - y, 1e-10, 1.0)))
train_step = tf.compat.v1.train.AdamOptimizer(0.001).minimize(cross_entropy)

# 通过随机数来生成一个模拟的数据集
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
Y = [[int(x1+x2 < 1)] for (x1, x2) in X]

with tf.compat.v1.Session() as sess:
    init_op = tf.compat.v1.global_variables_initializer()
    # 初始化变量
    sess.run(init_op)
    # 这是在训练前的网络参数的值
    print(sess.run(w1))
    print(sess.run(w2))
    print('开始训练前')
    STEPS = 5000
    for i in range(STEPS):
        start = (i * batch_size) %dataset_size
        end = min(start + batch_size, dataset_size)
        # 通过选取样本训练神经网络并且更新参数
        sess.run(train_step,
                 feed_dict={ x: X[start:end], y_: Y[start:end]})
        if i % 1000 == 0:
            total_cross_entropy = sess.run(
                cross_entropy, feed_dict= {x:X,y_:Y})
            print(" After %s training step(s), cross entropy on all data is %s"%(i,total_cross_entropy))
    print('这是训练后')
    print(sess.run(w1))
    print(sess.run(w2))





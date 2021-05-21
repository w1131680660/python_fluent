import tensorflow as tf

a = tf.constant([1.0,2.0],name='a') # 给定一个常量数组

# 声明一个2×3的矩阵
tf.compat.v1.disable_eager_execution()
weigths = tf.Variable(tf.compat.v1.random_normal((2,3), stddev=1,seed=1))
print(weigths)
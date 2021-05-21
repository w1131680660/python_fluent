import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets
import os


tf.compat.v1.disable_eager_execution()


w1 = tf.Variable(tf.compat.v1.random_normal( (2,3),stddev=1,seed=1 ))
w2 = tf.Variable(tf.compat.v1.random_normal( (3,1), stddev=1, seed=1))

# 暂时将输入的特征向量定义为一个常量. 注意x是一个1×2的矩阵


x = tf.constant( [ [0.7 ,0.9]])

# 进行前向传播算法的神经网络输出 层数为1层

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

sess = tf.compat.v1.Session()
# 初始化 W1和W2变量
# sess.run(w1.initializer)
# sess.run(w2.initializer)
init_op = tf.compat.v1.global_variables_initializer() # 初始化所有变量
sess.run(init_op)

print(sess.run(y))
sess.close()
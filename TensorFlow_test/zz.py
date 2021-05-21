import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets
import os


os.environ['TF_CPP_MIN_LOG_LEVEL']='2'   #屏蔽无关的信息，2是只打印error
#自动查看有没有缓存一个mnist数据集，没有的话自动从google下载。
# x: [60k, 28, 28],
# y: [60k]
(x,y),_ =datasets.mnist.load_data()

# 把数据类型转换为张量
#x: [0~255] => [0~ 1.]
x=tf.convert_to_tensor(x,dtype=tf.float32) / 255.
y=tf.convert_to_tensor(y,dtype=tf.int32)

print(x.shape, y.shape, x.dtype, y.dtype)
print(tf.reduce_min(x),tf.reduce_max(x))
print(tf.reduce_min(y),tf.reduce_max(y))


#创建一个数据集，一次取到一个batch_size,因为上面一次取一个。
train_db = tf.data.Dataset.from_tensor_slices((x,y)).batch(128)
train_iter = iter(train_db)   #迭代器
sample = next(train_iter)
print("batch: ", sample[0].shape, sample[1].shape)

#创建权值，完成前向传播
#[batch,784] => [b, 256] => [b, 128] => [b, 10]
#w: [dim_in, dim_out]
#b: [dim_out]
w1 = tf.Variable(tf.random.truncated_normal([784, 256], stddev=0.1))#原来均值为0，方差维为1,现在方差变为0.1
b1 = tf.Variable(tf.zeros([256]))
w2 = tf.Variable(tf.random.truncated_normal([256, 128], stddev=0.1))
b2 = tf.Variable(tf.zeros([128]))
w3 = tf.Variable(tf.random.truncated_normal([128, 10], stddev=0.1))
b3 = tf.Variable(tf.zeros([10]))

lr = 1e-3

#前向运算


for epoch in range(10):         #iterate 迭代整个数据集10次。
    # 外层for: 对所有的图片做循环。
    #for (x, y) in train_db:
    for step, (x, y) in enumerate(train_db):  #迭代for every batch
        #x: [128, 28, 28]
        #y: [128]

        #维度变换; [b, 28, 28]-> [b, 28*28]
        x = tf.reshape(x, [-1, 28*28])
        #x: [b, 28*28]
        #h1 = x@w1 + b1
        #[b, 784]@[784, 256] + [256] = [b, 256] + [256] => [b, 256] + [b, 256]

        #使用tensorflow自动求导的过程,其中: w,b。tf.GradientTape()参与梯度计算的代码放到这里面。
        with tf.GradientTape() as tape:
            #GradientTape里面默认只会跟踪tf.Variable()类型。如果类型不是这个的话。这里为tf.tensor,tf.Variable是tf.tensor的一种特殊类型。
            #因此简单的包装一下。

            h1 = x@w1 + tf.broadcast_to(b1, [x.shape[0], 256]) #直接自动广播机制，也可以手动
            h1=tf.nn.relu(h1)
            #[b, 256] -> [b, 128]
            h2 = h1@w2 + b2
            h2=tf.nn.relu(h2)
            #[b, 128] -> [b, 10]
            out = h2@w3 + b3  #得到前向输出结果。

            #computer loss: 计算误差均方差。
            # out维度: [b, 10]
            # 真实的y:  [b],维度这里需要把y变成一个one-hot 编码
            y_onehot = tf.one_hot(y, depth=10)

            #mse = mean((y_onehot-out)^2)
            #shape : [b, 10]
            loss = tf.square(y_onehot - out)

            #mean: scalar
            #loss = tf.reduce_mean(loss) / b / 10 一般来说除以一个b就够了，每个batch上的一个均值。取决于怎么理解，都是可以的。
            loss = tf.reduce_mean(loss) #这里相当于一个放缩，正向放缩不会影响梯度的方向。没有影响的。
            #loss = tf._reduce_mean(tf.reduce_sum(loss,axis=1))#,我自己的理解。

        #得到一个梯度。需要求解梯度的有哪些呢？
        grads = tape.gradient(loss, [w1, b1, w2, b2, w3, b3])
        #print(grads)  #结果：[None, None, None, None, None, None]
        # w1 = w1 - lr* w1_grad, 这里为了细节，手写。实际可以不用手写。

             #b1 = b1 - lr * grads[1]
        #w2 = w2 - lr * grads[2]
        #b2 = b2 - lr * grads[3]
        #w3 = w3 - lr * grads[4]
        #b3 = b3 - lr * grads[5]   #第一for增加一个step
        #w1 = w1 - lr * grads[0]         	#这里两个w1为两个对象。原来的w1减去这个值赋值给一个新的对象.w1原来是
        									#tf.Variable,更新一次之后新的w1变为tf.Tensor类型了。新一次操作之后就会错误。
        w1.assign_sub(lr * grads[0])    	#原地更新,数据类型保持不变
        b1.assign_sub(lr * grads[1])
        w2.assign_sub(lr * grads[2])
        b2.assign_sub(lr * grads[3])
        w3.assign_sub(lr * grads[4])
        b3.assign_sub(lr * grads[5])

        # print(isinstance(b3,tf.Variable))
        # print(isinstance(b3,tf.Tensor))
        #每100论，看一下loss信息。
        if step % 100 == 0:
            print(epoch, step, 'loss:', float(loss))

# 0 loss: 385739.0
# 100 loss: nan
# 200 loss: nan
# 300 loss: nan
# 400 loss: nan  nan为梯度爆炸。初始化的时候，方差变小一点，变为0.1看上面的。

# 0 loss: 0.7686458826065063     结果立马变了
# 100 loss: 0.2187460958957672
# 200 loss: 0.18475660681724548
# 300 loss: 0.16235101222991943
# 400 loss: 0.17448323965072632   可以多迭代几次数据集。外层再加for

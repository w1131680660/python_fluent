import tensorflow as tf

a = tf.constant([1.0 ,2.0], name ='a')
b = tf.constant([2.0,3.0],name='b')

result = tf.add(a, b,name ='add')
print(result)
# 会话
# 创建一个会话
# sess = tf.compat.v1.Session()
# z = sess.run() # 得到result的取值
# print(z)
# sess.close() # 关闭会话，使得资源被解放
# with tf.compat.v1.Session() as sess:
#     sess.run()
sess = tf.compat.v1.Session()
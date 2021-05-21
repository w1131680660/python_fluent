# 从一个线程向另一个线程发送数据最安全的方式可能就是使用
# queue 库中的队列了。创建一个被多个线程共享的 Queue 对象，
# 这些线程通过使用 put() 和 get() 操作来向队列中添加或者删除元素。 例如：
from queue import  Queue
from threading import  Thread

def producer(out_q):
    i =1
    while True:
        ...

        out_q.put(i)
        i +=1
        if i >100:
            break
def consumer(in_q):
    while True:
        data = in_q.get()
        print('这是消费者',data)
        ...

q =Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
qq =[]
qq.append()
# 你正在写一个多线程程序 一个线程获取多个锁 ,怎么避免死锁问题


# 死锁问题多数为一个线程获取了第一个锁，然后获取第二个锁时发生了阻塞，然后阻塞了其它程序执行，然后程序假死


import threading
from contextlib import contextmanager

# 获取本地线程状态，用于存储已获取锁的信息

_local = threading.Lock()


@contextmanager
def acquire(*locks):

    locks = sorted(locks, key=lambda x: id(x))
    print('this is locks:',locks)
    acquired = getattr(_local, 'acquired', [])

    if acquired and max(id(lock) for lock in acquired >= id(locks[0])):
        raise RuntimeError('Lock order Violation')
    acquired.extend(locks)

    _local.acquire = acquired
    try:
        for lock in locks:
            lock.acquire() # 加锁
        yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


x_lock = threading.Lock()
y_lock = threading.Lock()


def thead_1():

    while True:
        with acquire(x_lock, y_lock):
            print('Thead_1')



def thead_2():

    while True:
        print(223)
        with acquire(y_lock, x_lock):
            print('Thead_2')


t1 = threading.Thread(target=thead_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thead_2)
t2.daemon = True
t2.start()

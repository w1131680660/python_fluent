'''
python解释器被一个全局解释器保护着，保证任何时候都会只有一个线程运行
在计算密集型的程序只会有一个单cpu运行，但是程序只是设计到I/O,比如网络交互，就可以使用多线程，因为他们大多时间在等待。
因此采用并发编程

'''

import multiprocessing  # 开启进程
pool = multiprocessing.Pool()
# 列如有以下代码

def some_work(args):
    ...
    result =0
    return result

def some_thread():
    args = ...
    while True:
        ...
        r = some_work(args) # 串行执行
        r = pool.apply(some_work, (args)) # 开启进程池















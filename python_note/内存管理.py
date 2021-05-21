import os
import psutil


def show_memory_info(hint):

    ''' 查看内存使用情况 '''
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss/1024./1024
    print('{} memory used:{} MB'.format(hint, memory))


def func():
    ''' 这是查看函数的内存调用情况的 '''
    # global a
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    show_memory_info('after a created')

# func()
# show_memory_info('finished')

#这个过程为 创建之前为20MB 内存，在生成a后为407M,然后又为 20MB

# 查看引用计数

import sys
b = []
print(sys.getrefcount(b))

def func_1(b):
    print(sys.getrefcount(b))

func_1(b)
print(sys.getrefcount(b))
# 在 func_1 b一共被引用了几次
#　答：一共四次，一次来自ｂ＝［］，一次来自func_1(b),
# 其一次来自print(sys.getrefcount(b))，一次函数参数
# 而在函数外则是2次
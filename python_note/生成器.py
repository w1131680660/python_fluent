import os
import psutil
import time


def log_time():

    def inner(func):
        def wrapper(*args, **kwargs):
            begin = time.time()
            result = func(*args,**kwargs)
            over = time.time()
            print(over-begin)
        return wrapper
    return inner

def show_memory(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss/1024/1024
    print('{} memory used:{} MB'.format(hint,memory))


@log_time()
def test_iterator():
    show_memory('initing iterator')
    list_1 = [i for i in  range(100000000)]
    show_memory('after iterator initated')
    print(sum(list_1))
    show_memory('after sym called')

@log_time()
def test_generator():
    show_memory('initing iterator')
    list_2 = (i for i in range(100000000))
    print(sum(list_2))
    show_memory('after sum called')

# 迭代器生成的元素都会保存到内存中
# test_iterator()
#
# # 生成器就不需要那么多内存，只会带调用next()函数的时候才会生成下一个变量
# # 且生成时间比迭代器时间少
# test_generator()、

# 生成器新花样


def generator(k):
    i = 1
    while True:
        yield i**k
        i += 1


gen_1 = generator(1)
gen_3 = generator(3)
print(gen_1)
print(gen_3)


def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3  = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1,sum_3)
get_sum(8)
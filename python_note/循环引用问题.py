import psutil
import os,sys
import objgraph
a ='123123'
b= '12317723'
print(sys.getrefcount(a), sys.getrefcount(b))
def show_memory_info(hint):
     pid = os.getpid()
     p = psutil.Process(pid)
     info = p.memory_full_info()
     memory = info.uss/1024./1024
     print('{} memory used:{} MB'.format(hint,memory))


def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after, a,b created')
    a.append(b)
    b.append(a)
    # objgraph.show_refs([a])
    objgraph.show_backrefs([a])
func()
show_memory_info('finished')
import gc
gc.collect()

show_memory_info('gc')
print(sys.getrefcount(a), sys.getrefcount(b))
# 这里a,b互相引用，并且作为局部在函数结束后就应该没了，但是内存依旧被占有
# 这是a,b互相引用，导致引用数不为0

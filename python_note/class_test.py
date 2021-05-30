import os
import psutil


def show_memory_info(hint):

    ''' 查看内存使用情况 '''
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss/1024./1024
    print('{} memory used:{} MB'.format(hint, memory))

class test_a():

    object_is = None
    def __init__(self,args):
        self.args =args


    # def __new__(cls, *args, **kwargs):
    #     if not cls.object_is:
    #         cls.object_is = object.__new__(cls)
    #     return cls.object_is

    def test(self):
        z = [i for i in range(10000000)]
        return 123
show_memory_info('bezn')
z =test_a('a')
z=z.test()
print(id(z))
show_memory_info('over')
w =test_a('a')
w =w.test()
print(id(w))
show_memory_info('zz')
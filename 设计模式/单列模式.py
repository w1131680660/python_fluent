import  threading

class Singleton(object):

    _instance_lock = threading.local()

    def __init__(self,num):
        self.num = num

    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(Singleton, "_instance"):
    #         Singleton._instance = object.__new__(cls)
    #     return Singleton._instance

    def __call__(self,):
        z = self.num
        return 'hello这是__call__ %s'%(z)

# obj1 = Singleton()
# obj2 = Singleton()
# print(Singleton()(1,3))
# print(obj1,obj2)
def task(arg):
    obj = Singleton(arg)
    print(obj())

for i in range(10):
    t = threading.Thread(target=task,args=[i])
    t.start()
    print(t.getName())
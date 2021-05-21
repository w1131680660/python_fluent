

class My_test(object):

    args = {'code':200}
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args,**kwargs)
        return cls._instance
    def __init__(self):
        pass

    def list(self,if_test):
        if if_test :
            self.args['code'] =400
            print(2222)

        return self.args

a =My_test()
print(a.list(''),id (a))
a =My_test()
print(a.list('1'),id(a))
a = My_test()
print(a.list(0),id(a))
print(a.list('2'),id(a))
a = My_test()
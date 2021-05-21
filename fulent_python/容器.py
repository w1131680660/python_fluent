
class test(object):

    def __init__(self,alist):
        self.alist =  alist if isinstance(alist,list) else []


    def __add__(self,):
        return sum(self.alist)

    def __call__(self, *args, **kwargs):
        return '???'

a =test([1,23,4])
print(a())
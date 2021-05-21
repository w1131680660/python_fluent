
# 定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self,maxbytes =-1):
        pass

    @abstractmethod
    def write(self,data):
        pass


# 抽象类的一个特点不能被直接实例化
# a = IStream() # 报错

# 抽象类的目的1 .就是让别的类继承它并实现特定的抽象方法：

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print(213)
        return 222
    def write(self, data):
        pass
P =SocketStream()

# 2. 抽象基类的一个主要用途是在代码中检查某些类是否为特定类型，实现了特定接口：x
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass
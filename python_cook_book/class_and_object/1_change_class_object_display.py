
# 将对象的实列打印
# python的容器：抽象概念:专门用来容纳其他对象的数据类型的统称
'''
    每个内置的容器都是满足多个接口定义的组合实体，都是可迭代的

'''

class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    def __repr__(self):
        # 都一样的可视化撕实列方法

        return 'Pair_repr_{0.x!r},{0.y!r}'.format(self)

    # def __str__(self):
    #     # __str_方法会将实列转换为一个字符串然后返回
    #     # 就是可视化实列内容  如果__str__和__repr__都有默认调用__str_-
    #     return 'Pair_str_{0.x!s},{0.y!s}'.format(self)

p = Pair(3,4)
 # 在容器的条件喜爱执行__repr__
print(p)

def greeting(name:str) ->str:
    # name参数是str类型,并且返回str类型
    # 这是类型标注支持的写法
    return 'Hello'+name

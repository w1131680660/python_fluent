


# 实现自定义的类来模拟内置的容器类功能，比如列表和字典。但是你不确定到底要实现哪些方法。

class Items:

    def __init__(self,initial):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] =value
        return self._items

    def __delete__(self, instance):
        return self._items.pop()

    def insert(self,key,value):
        self._items.index(key,value)
        return self._items

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return '{0}'.format(self._items)

q =Items([1,3,4])
z=[1,2,3,4,5,1,6]
print(z.remove(1),z)
print(q)

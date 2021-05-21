import weakref
'''
对一个对象的弱引用（weak reference）。相对于通常的引用来说，\
如果一个对象有一个常规的引用，它是不会被垃圾收集器销毁的，但是如果一个对象只剩下一个弱引用，那么它可能被垃圾收集器收
'''
s1 ={1,2,3}
s2 =s1 #

def bye():# ‘该函数不能为要销毁的对象的绑定方法，否则有一个指向对象的引用
    print('gone with the wind')

ender = weakref.finalize(s1,bye)# 在s1对象上注册对象bye的回调

print(ender.alive)# 调用在finalize对象之前，.alive属性的值为true
del  s1
print(ender.alive) # del 不是删除对象而是删除对象的引用

s2 = 'hello'
print(ender.alive) # 重新绑定s2 发现对象调用了bye的回调为false


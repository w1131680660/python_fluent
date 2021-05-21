
class MyInt(int):

    def __add__(self, other):
        return int.__add__(self,other) +10

a = MyInt(1)
b = MyInt(2)
print(a+b)
# 实列相加
# s =a
# z =1
# del a
# print(s
#       )
a="very goodaaaaaaaaaaaaaaaaaaaaaaa"
b ="very goodaaaaaaaaaaaaaaaaaaaaaaa"
print(a is b)
a= []
b =[]
print(a is b) # false
import sys
a = [1,2,3]
# sys.getrefcount(a)
print(sys.getrefcount(a))

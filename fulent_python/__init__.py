# a = 1  # [1]
# def f():
#     a =2 #[2]
#     print(a,id(a)) #[3]：输出结果为2
#     def x():
#         global a
#
#         print(a)
#         a =333
#     x()
#     print('111',a)
# f()
# print('3333',a) #// 4\
a =1
print(a, id(a))
def f(a=2,b=2):

    print(a, id(a))

f(a)
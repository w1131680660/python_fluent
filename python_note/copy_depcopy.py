import copy
l1 = [[1, 2], (30, 40)]
l2 = l1 #这是指向同一引用
l3 = l1.copy()  # 浅拷贝
l4 = list(l1)  #  浅拷贝


l1[0].append(3)
l1.append(3)
print(l1,'\n' ,l2,'\n',l3,'\n',l4,'\n')
import copy



import copy
x = [1]
x.append(x)
for i in x:
    print(i)
y = copy.deepcopy(x)
# 以下命令的输出是？
# print(x == y) # 报错了

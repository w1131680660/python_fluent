
l1 =([1,1,1],1)
print(l1)
key_1 = {'qqq':2222,'zzz':2323,'asdadwad':23123}
print(key_1.items())
print(sorted(key_1.items(),key=lambda x:x[-1],reverse=True))

x_1= [12,3123,213,123,123]
y = [x *2 if x>0 else -x *2 for x  in x_1]
print(y)
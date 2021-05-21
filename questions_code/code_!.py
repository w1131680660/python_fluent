v = dict.fromkeys(['k1','k2'],[])
print(v)
v['k1']=666
print(v)

def num():
    return [lambda x:i*x for i in range(4)]

for i in num():
    print([i(2)])
# print([m(2) for m in num()])
# z = [ i%2 for i in range(10)]
# print(z)
# print([i*i for i in range(1,11)])
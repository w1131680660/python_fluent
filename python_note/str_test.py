
a ='aaaa'
b ='aaaa'
print(a is b, id(a), id(b))
q =11111
w=11111
print(q is w)

e =257
b =257
print(e is b, id(e), id(b))


a = 257
b = 257

print(a == b)

print(id(a) ,id(b),a is b)

l1 = [1, 2, 3]
l2 = [1,2,3]
print(l2)
print( l1 is l2,id(l2), id(l1))
print(isinstance(l1,list))


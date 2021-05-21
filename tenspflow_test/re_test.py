z = 'w1.3s'
w ='w2,3z'
q = '5つ中の2.8'
e ='4.3 out of 5'
q1 ='5つ中の5'
e1 = '4.3 out of 5'
import re
patern = '\d+.\d+|\d+,\d+'
zz = re.findall(patern,e)
print(zz)
zzz = {}
for k,v in zzz.items():
    print(k,v)
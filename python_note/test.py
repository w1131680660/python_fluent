import sys
a = []

# 两次
# b = a
def func(a):
    print(sys.getrefcount(a))
func(a)

print(sys.getrefcount(a))

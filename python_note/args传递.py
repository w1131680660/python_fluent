

a = 1



l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l2
print(id(l1),id((l2)))


import time,functools
def log_time():

    def wrapper(func):
        @functools.wraps(func)
        def inner(*args,**kwargs):
            begin =time.time()
            func(*args,**kwargs)
            over = time.time()
        return inner
    return wrapper

@log_time()
def func(b):
    print(id(b),id(a),a,b)
    b =2
    print(id(b),id(a))
    return b
z = func(a)


import time



import functools
# def log_time():
#
#     def inner(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             begin = time.time()
#
#             func(*args,**kwargs)
#             over = time.time()
#             print(over-begin)
#         return wrapper
#     return inner


# def log_time(func):
#     def warpper(*args, **kwargs):
#         begin = time.time()
#         func(*args,**kwargs)
#         over = time.time()
#         print(over-begin)
#     return warpper

def log_time():

    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            begin = time.time()

            func(*args,**kwargs)
            over = time.time()
            print(over-begin)
        return wrapper
    return inner

@log_time()
def login(test):
    print(test)

login(123)
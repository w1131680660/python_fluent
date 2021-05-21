
import time
from functools import wraps
def timethis(func):
    # @wraps(func)
    def wapper(*args,**kwargs):
        begin = time.time()
        result =func(*args,**kwargs)
        end = time.time()
        print(func.__name__, end-begin)
        return result
    return wapper

@timethis
def countdown(n):
    while n>0:
        n -=1

countdown(100000)
countdown = timethis(countdown(1000000))
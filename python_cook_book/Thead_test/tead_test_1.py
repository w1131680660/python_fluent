from threading import  Thread
import time


def countdown(n):
    while n>0:
        print('T-minus',n)
        n -=1
        time.sleep(5)

# t = Thread(target=countdown, args=(10,))
t  = Thread(target=countdown, args=(10,), daemon=True) # 开启后台线程
t.start() # 开启该线程对象  在线程开启后程序就会继续向下执行
if t.is_alive():
    print('Still runing')
else:
    print('Completed')
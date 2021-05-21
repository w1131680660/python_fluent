from threading import Thread
import time

class CountdownTask:

    def __init__(self):
        self.runing = True

    def terminate(self):
        self.runing = False

    def run(self,n):
        while self.runing and n >0:
            print('T-minus',n)
            n -=1
            time.sleep(1)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
#c.terminate()# 手动终止线程
t.join() #将一个线程加入当前线程，并等待他终止
# c.terminate()# 手动终止线程
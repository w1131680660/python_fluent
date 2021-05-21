



# 对多线程程序中的临界区加锁避免竞争条件
import threading
class SharedCounter:

    def counter(self, inital_value= 0):
        self._value = inital_value
        self._value_lock = threading.Lock()

    def incr(self,delta =1):
        with self._value_lock:
            self._value += delta

    def decr(self,delta=1):
        '''
        Lock 对象和with语句一起使用可以保证互斥执行，保证每一个线程
        只会执行with语句的代码
        :param delta: 
        '''
        with self._value_lock:
            self._value -= delta

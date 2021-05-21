from socket import  socket, AF_INET, SOCK_STREAM
import threading

# 问题： 保存线程的运行状态,这个状态对其他线程不可见
# 方案: 使用Thead.local(),创建一个本地线程存储对象，这个线程的操作只会对执行线程可见

class LazyConnection:

    def __init__(self,address,family = AF_INET, type = SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local

    def __enter__(self):
        if hasattr(self.local,'sock'):
            raise  RuntimeError('Already connectd')
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock
        


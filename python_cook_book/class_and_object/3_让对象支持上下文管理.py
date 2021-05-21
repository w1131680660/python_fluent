

# 你想让你的对象支持上下文管理协议(with语句)。

from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:

    def __init__(self,address, family=AF_INET,type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None
    '''
    當with語句在開始運行時，會在上下文管理器對象上調用 __enter__ 方法。
    with語句運行結束後，會在上下文管理器對象上調用 __exit__ 方法

    这个类的连接的建立和关闭是使用 with 语句自动完成的，例如：
    '''
    def __enter__(self):
        if self.sock is not  None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


conn = LazyConnection(('www.python.org', 80))
from functools import partial
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed
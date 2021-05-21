
from  queue import Queue
from threading import  Thread,Event

''' actort 是一种最简单的并行和分布式计算的解决方案
简单来说 一个 actor 就是一个并发执行的任务,简单的执行发给它的消息任务,响应这些消息时,
他还可能给其他的actor发送更进一步的消息, actor之间的通信是单向和异步的.因此消息的发送者不知道消息什么被发送,
也不知道消息已被处理的回应或通知 '''


class ActorExit(Exception):
    pass

class Actor:

    def __init__(self):
        self._mailbox = Queue()

    def send(self,msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise  ActorExit()

        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True # 开启守护进程 主线程运行结束时不对这个子线程进行检查而直接退出，子进程也一起退出
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.wait()

    def run(self):
        # 由用户来决定运行
        while True:
            msg = self.recv()

class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('GOT:',msg)
p = PrintActor()
p.start()
p.send('HELLO')
p.send('world')
p.close()
# p.join()
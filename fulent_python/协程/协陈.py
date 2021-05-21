import asyncio
import threading

# @asyncio.coroutine
# def hello():
#     print('hello world')
#     r = yield from asyncio.sleep(1)
#     print('hello again')
#
# # 获取Event loop
# loop = asyncio.get_event_loop()
# # 执行countine
#
# loop.run_until_complete(hello())
# loop.close()

@asyncio.coroutine
def hello():
    ''''
        在遇见yield是这直接执行下一个，且为同一个
    '''
    print('1 hello world %s'%(threading.currentThread()))
    yield from asyncio.sleep(0.5)
    print('2 hello agin %s'%(threading.currentThread()))

@asyncio.coroutine
def hello_1():
    ''''
        在遇见yield是这直接执行下一个，且为同一个线程
    '''
    print('2 hello world %s'%(threading.currentThread()))
    yield from asyncio.sleep(0.5)
    print('3 hello agin %s'%(threading.currentThread()))
loop = asyncio.get_event_loop()
tasks = [ hello(), hello_1() ]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


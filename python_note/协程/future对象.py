import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('666')

# asyncio.Future对象


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # 创建一个Feature对象,没绑定任何行为，这这个任务不知道什么时候结束
    fut = loop.create_future()
    # 创建一个任务（Task），绑定set_after,函数，函数在
    # 秒之后会给fut赋值，即手动设置future任务的最终结果，那么fut就可以结束了
    await loop.create_task( set_after(fut))

    # 等待 Futre对象获取最终结果，否则一直等下去
    data = await fut
    print(data)

asyncio.run(main())

#concurrent.futures.Futures 对象
# 使用线程池或进程池实现异步操作用到的对象

import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def func(value):
    time.sleep(1)
    print(value)

# 创建线程池

thead_pool = ThreadPoolExecutor(max_workers=5)
# 创建进程池子
Process_pool = ProcessPoolExecutor(max_workers=4)

for i in range(10):
    fut = thead_pool.submit(func, i)
    print(fut)


# crm 80%都是基于协程的异步协程编程+mysql
print('future对象创建')
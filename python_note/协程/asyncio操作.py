
import asyncio

# 协程函数 定义函数时候东风恶 asyncio def 函数名
# 协程对象，执行协程函数()得到的对象


async  def func():
    print(123)

result = func()
#注意协程函数创建协程对象，函数内部并不会直接执行

# 去生成一个或者获取一个事件循环
loop = asyncio.get_event_loop()
# 将任务放到任务列表
loop.run_until_complete(result)

# await + 可等待对象(协程对象，Future,Task ->IO等待)

import asyncio, time



# asyncio.run(func())
# 在开启时间循环后 遇见await 会执行其他时候ijian
import functools
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


async def func():
    print('来往啊')
    response = await asyncio.sleep(2)
    print('结束',response)
    return '返回值'


# @log_time()

async def go():
    print('执行协程函数代码')
    # 串行调用

    task1 = asyncio.create_task(func())

    task2 = asyncio.create_task(func())
    response = await task1
    print('这第二个')
    response_1 = await task2
    print(response,response_1)

async  def main():
    print('执行task任务的并发编程')
    task_list = [
        asyncio.create_task(func(), ),
        asyncio.create_task(func(), )
    ]

    print('执行结束')
    done,pending = await  asyncio.wait(task_list, timeout=None)
    print(done)
z =time.time()
asyncio.run(main())
w =time.time()
print(w-z)
# await 就等待程序完了后再往下执行

# TASK 对象：在事件循环中添加多个任务

# TASKS 用于并发调度协程，通过asyncio.create_task(协程对象)的方式创建Task对象
# 这样可以让协程加入时间循环中等待别调度执行，当然还可以使用loop.create_task() 或 ensure_future()函数
# 不见尾手动实例化Task对象

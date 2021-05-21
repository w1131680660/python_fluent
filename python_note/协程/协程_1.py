
import time
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


def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))

@log_time()
def main(urls):
    for url in urls:
        print(url)
        crawl_page(url)

urls = ['url_1','urll_2','url_3','url_4','url_5']

# main(urls) 串行为15秒

# 并发执行

import asyncio


async def crawl_page_1(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

# @log_time()

async def main_1(urls):
    tasks =[asyncio.create_task(crawl_page_1(url))for url in urls]
    # 通过创建任务来调度执行
    for task in tasks:
        await task
z = time.time()
asyncio.run(main_1(urls))
w =time.time()
print(w-z)
print(123)
print('第一次提交测试')
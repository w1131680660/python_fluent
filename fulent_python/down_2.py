from concurrent import futures
from fulent_python.dow_1 import save_flag,get_flag,show,main


MAX_WORKERS = 20

def download_on(cc):
    print(123,cc)
    image = get_flag(cc)
    show(cc)
    save_flag(image,cc.lower()+'.gif')
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    # 开线程池
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_on, sorted(cc_list))
    return len(list(res))

if __name__ == '__main__':
    main(download_many)

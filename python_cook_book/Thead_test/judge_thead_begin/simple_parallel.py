import gzip
import io
import glob
from concurrent import  futures
# 问题：有个程序需要cpu密集型操作，需要cpu多核的优势


# 列入下面是一个脚本，从这些日志文件找到所有访问过robots.txt的文件

def find_robots(filename):
    robots =set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6] =='/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    files = glob.glob(logdir +'.*.log.gz')
    all_robots = set()
    # 在串行执行
    # for robots in map(find_robots, files):
    #     all_robots.update(robots)
    # 改为多核cpu
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots
import redis

import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
host_master = '1.15.243.233' # 1
salve_host = '1.116.137.163' #2
salve_host_1 = '175.27.129.7' # 3
# 1131680660zxcV,
r = redis.Redis(host=salve_host_1, port=6379, decode_responses=True,)
mast_r =  redis.Redis(host=host_master, port=6379, decode_responses=True,password='1131680660zxcV,')
# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
mast_r.set('name', 'junxi1')  # key是"foo" value是"bar" 将键值对存入redis缓存
print(mast_r.get('name'))
# print(r.get('name'))  # 取出键name对应的值
# print(type(r.get('name')))
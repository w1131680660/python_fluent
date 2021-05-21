
import pika
import json
user = 'admin'
pwd = 'admin'
credentials = pika.PlainCredentials(user,pwd) # mq的账号和密码

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                             port=5672,virtual_host = '/',
                                                               credentials = credentials))
channel=connection.channel()

# 声明消息队列，消息在这个队列传递，如不存在，则创建。
# durable = True 代表消息队列持久化存储，False 非持久化存储默认为false，非持久化会存盘，但是会随着服务器重启而丢失

# queue 队列名称
result = channel.queue_declare(queue='python_test',durable=True)

# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建.durable = True 代表exchange持久化存储，False 非持久化存储
# result = channel.exchange_declare(exchange = 'python-test', durable = True)

for i in range(1000):
    message = json.dumps({'order_id':'test_id_%s'%(i)})
    # 向队列插入数值 routing_key是队列名。delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化
    # exchange是交换机, routing_key 指定队列名称
    channel.basic_publish(exchange='', routing_key='python_test', body=message,
                          properties=pika.BasicProperties(delivery_mode = 2))

    print(message)

connection.channel()

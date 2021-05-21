import pika , sys, os

user = 'admin'
pwd = 'admin'
credentials = pika.PlainCredentials(user,pwd) # mq的账号和密码

connection = pika.BlockingConnection(pika.ConnectionParameters(host='1.15.243.233',
                                                             port=5672,virtual_host = '/',
                                                               credentials = credentials))
channel = connection.channel()

# 创建交换机  exchange 指定交换机的名称
result = channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"


for i in range(50):
    message = ''.join(sys.argv[0]) or "Hello World!"
    message ='%s %s'%(i, message)
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(" [x] Sent %r" % message)
connection.close()
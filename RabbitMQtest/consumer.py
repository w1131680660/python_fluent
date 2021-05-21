import pika

user = 'admin'
pwd = 'admin'
credentials = pika.PlainCredentials('admin','admin') # mq的账号和密码

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                             port=5672,virtual_host = '/',
                                                               credentials = credentials))


channel = connection.channel()
# 协程用于回调函数
# 定义一个回调函数来处理消息队列的中的消息，这里并将它打印出来
def callback(ch,method, properties, body):
    ch.basic_ack(delivery_tag= method.delivery_tag)
    print(body.decode())

# 告诉rabbitmq，用callback来接受消息
channel.basic_consume('python_test', callback)
# 开始接收消息，并进入阻塞状态，队列里有消息才会调用callback进行处理
channel.start_consuming()
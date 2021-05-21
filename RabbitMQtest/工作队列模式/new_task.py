import pika , sys, os

user = 'admin'
pwd = 'admin'
credentials = pika.PlainCredentials(user,pwd) # mq的账号和密码

connection = pika.BlockingConnection(pika.ConnectionParameters(host='1.15.243.233',
                                                             port=5672,virtual_host = '/',
                                                               credentials = credentials))
channel = connection.channel()

result = channel.queue_declare(queue='task_queue', durable=True)

message = ''.join(sys.argv[0]) or "Hello World!"
for i in range(50):
    message = ''.join(sys.argv[0]) or "Hello World!"
    message ='%s %s'%(i, message)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent ＃使消息持久
        ))
    print(" [x] Sent %r" % message)
connection.channel()
connection.close()
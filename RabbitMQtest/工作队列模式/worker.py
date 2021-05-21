import pika, time

user = 'admin'
pwd = 'admin'

credentials = pika.PlainCredentials(user, pwd)

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='1.15.243.233',
    port= 5672, virtual_host='/',
    credentials = credentials
))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(' [x] Received %r'% body.decode())
    time.sleep(body.count(b'.'))
    print("  [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
# auto_ack设置成 False，在调用callback函数时，未收到确认标识，
# 消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
# auto_ack= False
channel.basic_consume(queue='task_queue' ,
                      on_message_callback= callback,
                      auto_ack = False)

channel.start_consuming()
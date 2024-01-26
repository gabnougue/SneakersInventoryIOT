import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='sneakers_queue')

channel.basic_publish(exchange='',
                      routing_key='sneakers_queue',
                      body='Hello, this is a message about sneaker inventory!')

print(" [x] Sent 'Hello, this is a message about sneaker inventory!'")

connection.close()

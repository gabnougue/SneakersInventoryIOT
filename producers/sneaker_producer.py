import pika
import time


def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='sneakers_queue')

    while True:
        message = "Info about sneakers"
        channel.basic_publish(exchange='',
                              routing_key='sneakers_queue',
                              body=message)
        print(f" [x] Sent '{message}'")
        time.sleep(5)

    connection.close()


if __name__ == "__main__":
    run()

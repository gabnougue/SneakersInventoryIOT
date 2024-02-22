import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters('broker'))
    channel = connection.channel()

    channel.queue_declare(queue='sneakers_queue')

    channel.basic_consume(queue='sneakers_queue',
                          on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    connection.close()

    if __name__ == "__main__":
        run()


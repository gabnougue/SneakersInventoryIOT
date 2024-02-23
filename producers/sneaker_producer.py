import pika
import json
import time

def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters('broker'))
    channel = connection.channel()

    channel.queue_declare(queue='sneakers_queue')

    while True:
        sneaker = {
          "name": "Air Max 90",
          "brand": "Nike",
          "size": 10,
          "color": "Black/White",
          "price": 120.00
        }

        location = {
            "name": "Nike Store",
            "address": "123 Main St",
            "city": "New York",
            "state": "NY",
            "zip": 10001,
            "temperature": 70
        }

        quantity = 10

        message = {
            "sneaker": sneaker,
            "location": location,
            "quantity": quantity
        }

        # Sérialisation du dictionnaire en JSON
        message_json = json.dumps(message)

        channel.basic_publish(exchange='',
                              routing_key='sneakers_queue',
                              body=message_json)
        print(f" [x] Sent '{message_json}'")
        time.sleep(5)

    connection.close()

if __name__ == "__main__":
    run()

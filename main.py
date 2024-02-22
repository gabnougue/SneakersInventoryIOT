# main.py
import threading
from producers import sneaker_producer
from consumers import sneaker_consumer


def start_producer():
    sneaker_producer.run()


def start_consumer():
    sneaker_consumer.run()


if __name__ == "__main__":
    producer_thread = threading.Thread(target=start_producer)
    producer_thread.start()

    consumer_thread = threading.Thread(target=start_consumer)
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

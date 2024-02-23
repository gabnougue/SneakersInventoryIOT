# main.py
import os

from producers import sneaker_producer
from consumers import sneaker_consumer


def start_producer():
    sneaker_producer.run()


def start_consumer():
    sneaker_consumer.run()


if __name__ == "__main__":

    operator = os.environ['OPERATION']
    if operator == 'producer':
        start_producer()

    elif operator == 'consumer':
        start_consumer()

    else:
        raise ValueError("Invalid operator")
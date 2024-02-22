import subprocess

if __name__ == '__main__':
    # Define the paths to the Python scripts
    consumer_script = './consumers/sneaker_consumer.py'
    producer_script = './producers/sneaker_producer.py'

    # Launch both scripts simultaneously
    consumer_process = subprocess.Popen(['python', consumer_script])
    producer_process = subprocess.Popen(['python', producer_script])

    # Wait for both processes to complete
    consumer_process.wait()
    producer_process.wait()

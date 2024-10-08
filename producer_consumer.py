import threading
import queue
import time

def producer(event_queue):
    for i in range(5):
        event_queue.put(f'Event {i}')
        print(f'Produced Event {i}')
        time.sleep(1)

def consumer(event_queue):
    while True:
        event = event_queue.get()
        if event is None:
            break
        print(f'Consumed {event}')
        time.sleep(2)

event_queue = queue.Queue()

# Start Producer and Consumer Threads
producer_thread = threading.Thread(target=producer, args=(event_queue,))
consumer_thread = threading.Thread(target=consumer, args=(event_queue,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
event_queue.put(None)  # Signal to stop the consumer
consumer_thread.join()

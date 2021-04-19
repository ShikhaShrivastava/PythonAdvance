from threading import *
import time
def Producer():
    print('Producer is producing the items')
    time.sleep(5)
    print('Producer thread produced the item')
    print('Produced thread notified consumer thread')
    e.set()

def Consumer():
    print('Consumer thread is in waiting state')
    e.wait()
    print('Consumer thread got notified by producer')
    print('Consumer thread is consuming the items')
    print('Consumer Consumed the items')

if __name__=='__main__':
    e=Event()
    producer_thread=Thread(target=Producer)
    consumer_thread=Thread(target=Consumer)
    producer_thread.start()
    consumer_thread.start()
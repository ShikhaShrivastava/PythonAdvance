from threading import *
import time
def Producer():
    print('Producer is producing the items')
    time.sleep(5)
    print('Producer thread produced the item')
    print('Produced thread notified consumer thread')
    e.set()

def Consumer1():
    print('Consumer1 thread is in waiting state')
    e.wait()
    print('Consumer1 thread got notified by producer')
    print('Consumer1 thread is consuming the items')
    print('Consumer1 Consumed the items')

def Consumer2():
    print('Consumer2 thread is in waiting state')
    e.wait()
    print('Consumer2 thread got notified by producer')
    print('Consumer2 thread is consuming the items')
    print('Consumer2 Consumed the items')

def Consumer3():
    print('Consumer3 thread is in waiting state')
    e.wait()
    print('Consumer3 thread got notified by producer')
    print('Consumer3 thread is consuming the items')
    print('Consumer3 Consumed the items')

if __name__=='__main__':
    e=Event()
    producer_thread=Thread(target=Producer)
    consumer1_thread=Thread(target=Consumer1)
    consumer2_thread=Thread(target=Consumer2)
    consumer3_thread=Thread(target=Consumer3)
    consumer1_thread.start()
    consumer2_thread.start()
    consumer3_thread.start()
    producer_thread.start()
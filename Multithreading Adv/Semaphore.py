from threading import *
import time

def get_result():
    my_lock.acquire()
    for i in range(3):
        print(current_thread().name ,'is accessing the result')
        time.sleep(1)
    my_lock.release()

if __name__ == '__main__':
    my_lock= Semaphore(3)
    thread1=Thread(target=get_result , name='Shikha')
    thread2=Thread(target=get_result , name='Shubham')
    thread3=Thread(target=get_result , name='Raina')
    thread4=Thread(target=get_result , name='Amar')
    thread5=Thread(target=get_result , name='Nikita')

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
'''from threading import *
import time

def Printer():
    my_lock.acquire()
    for i in range(3):
        print('Printing the code: ' , current_thread().name)
        time.sleep(2)
    my_lock.release()
if __name__ == '__main__':
    my_lock=Lock()
    thread1 = Thread(target=Printer(), name = 'Python')
    thread2 = Thread(target=Printer(), name = 'Java')
    thread3 = Thread(target=Printer(), name = 'Angular')
    thread1.start()
    thread2.start()
    thread3.start()'''

#Applying synchronization upon main():

from threading import *
if __name__ == '__main__':
    my_lock=Lock()
    my_lock.acquire()
    #my_lock.acquire()--->Deadlock
    print('Main code has been locked')
    my_lock.release()
    #my_lock.release()
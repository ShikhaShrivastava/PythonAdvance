#Program-1
'''from threading import *
import time

def my_task():
    print('Current thread is Daemon', current_thread().daemon)
    while(True):
        print('Autosuggestion')
        time.sleep(1)

if __name__ == '__main__':
    my_thread=Thread(target=my_task, name='Autosuggestedthread')
    my_thread.setDaemon(True)
    my_thread.start()
    for i in range(5):
        print('Typing code in python')
        time.sleep(1)
        print('typing completed ,Program Saved')'''

#---------------------------------------------------------------------------------------------------
#Program-2 (Printer shared among all the three thread result in DATA INCONSISTENCY)

from threading import *
import time

def Printer():
    for i in range(3):
        print('Printing the code: ' , current_thread().name)
        time.sleep(2)
if __name__ == '__main__':
    thread1 = Thread(target=Printer(), name = 'Python')
    thread2 = Thread(target=Printer(), name = 'Java')
    thread3 = Thread(target=Printer(), name = 'Angular')
    thread1.start()
    thread2.start()
    thread3.start()
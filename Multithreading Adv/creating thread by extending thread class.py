from threading import *
import time
class my_thread(Thread):
    def run(self):
        sq_num(lst)

def sq_num(lst):
    for i in lst:
        time.sleep(2)
        print(i**2)

class your_thread(Thread):
    def run(self):
        dub_num(lst)


def dub_num(lst):
    for i in lst:
        time.sleep(2)
        print(i * 2)

if __name__=='__main__':
    lst=[1,2,3,4,5]
    thread1 = my_thread()
    thread2 = your_thread()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

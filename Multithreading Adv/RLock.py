#Demo
'''from threading import *
if __name__ == '__main__':
    my_lock= RLock()
    my_lock.acquire()
    my_lock.acquire()
    print('Main code has been locked')
    my_lock.release()
    my_lock.release()'''

#__________________________________________________________________________________

#program-1

from threading import *
import time
def fact(num):
    my_lock.acquire()
    if num ==0:
        return 1
    else:
        return num*fact(num-1)
    my_lock.release()

def print_num(num):
    print('The factorial of' , num , 'is:' , fact(num))

if __name__=='__main__':
    my_lock=RLock()
    my_thread=Thread(target=print_num(5))
    my_thread.start()
from threading import *

if __name__=='__main__':
    my_lock= BoundedSemaphore(3) #if replaced with Semaphore it will not give any value Error
    my_lock.acquire()
    print('Main is trying to acquire the lock for the first time.')
    my_lock.acquire()
    print('Main is trying to acquire the lock for the second time.')
    my_lock.acquire()
    print('Main is trying to acquire the lock for the third time.')
    my_lock.release()
    print('Main is trying to release the lock for the first time.')
    my_lock.release()
    print('Main is trying to release the lock for the second time.')
    my_lock.release()
    print('Main is trying to release the lock for the third time.')
    my_lock.release()
    print('Main is trying to release the lock for the fourth time.')



'''from threading import *
if __name__=='__main__':
    print(current_thread().name, 'is daemon' , current_thread().isDaemon())
    #current_thread().setDaemon(True)
    print(current_thread().name, 'is daemon' , current_thread().daemon)'''


from threading import *
import time

def helper():
    for i in range(5):
        print('I am a Helper Thread')
        time.sleep(1)

if __name__=='__main__':
    my_thread=Thread(target=helper())
    my_thread.setDaemon(True)
    my_thread.start()
    time.sleep(3)

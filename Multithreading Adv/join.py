from threading import *
import time
def db_connect():
    for i in range(5):
        print('connect to database')
        time.sleep(2)

if __name__=='__main__':
    db_thread=Thread(target=db_connect, name='dbthread')
    db_thread.start()
    db_thread.join()
    for i in range(5):
        print('disconnect to database')

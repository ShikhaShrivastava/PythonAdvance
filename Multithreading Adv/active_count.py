from threading import *
import time

def print_data():
    print(current_thread().getName(),'got started')
    time.sleep(3)
    print(current_thread().getName(),'got ended')


if __name__=='__main__':
    print('No of thread active are:',active_count())

    first_thread=Thread(target=print_data, name='FirstChild')
    second_thread=Thread(target=print_data, name='SecondChild')

    print('No of thread active are:', active_count())

    first_thread.start()
    second_thread.start()

    print('No of thread active are:', active_count())
    time.sleep(10)
    print('No of thread active are:', active_count())


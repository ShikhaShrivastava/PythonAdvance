from threading import *
import time

def print_data():
    print(current_thread().getName(),'got started')
    time.sleep(3)
    print(current_thread().getName(),'got ended')


if __name__=='__main__':
    my_thread=enumerate()
    for thread in my_thread:
        print('Thread Name is:', thread.name)

    first_thread = Thread(target=print_data, name='FirstChild')
    second_thread = Thread(target=print_data, name='SecondChild')

    first_thread.start()
    second_thread.start()

    my_thread=enumerate()
    for thread in my_thread:
        print('Thread Name is:', thread.name)

    time.sleep(6)

    my_thread = enumerate()
    for thread in my_thread:
        print('Thread Name is:', thread.name)

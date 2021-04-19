from threading import *
import time

def print_data():
    print(current_thread().getName(),'got started')
    time.sleep(3)
    print(current_thread().getName(),'got ended')


if __name__=='__main__':
    print(current_thread().name, 'is alive' , current_thread().is_alive())

    first_thread = Thread(target=print_data, name='FirstChild')
    second_thread = Thread(target=print_data, name='SecondChild')

    first_thread.start()
    second_thread.start()

    print(first_thread.name, 'is alive' , first_thread.is_alive())
    print(second_thread.name, 'is alive', second_thread.is_alive())

    time.sleep(6)

    print(first_thread.name, 'is alive' , first_thread.is_alive())
    print(second_thread.name, 'is alive' ,second_thread.is_alive())

    print(current_thread().name, 'is alive' , current_thread().is_alive())


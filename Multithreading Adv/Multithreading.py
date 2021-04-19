from threading import *
import time


def sq_num(num):
    for i in num:
        time.sleep(5)
        print(i ** 2)


def dub_num(num):
    for i in num:
        time.sleep(5)
        print(i ** 2)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    first_thread = Thread(target=sq_num, args=(lst,))
    second_thread = Thread(target=dub_num, args=(lst,))

    start=time.time()
    first_thread.start()
    second_thread.start()
    first_thread.join()
    second_thread.join()
    end=time.time()
    print('The Time Taken by CPU is:' , end-start)



from threading import *
class mytask:
    def display(self):
        for i in range(5):
            print(current_thread().name)
if __name__=='__main__':
    ref=mytask()
    my_thread=Thread(target=ref.display)
    my_thread.start()
    for i in range(5):
        print(current_thread().name)
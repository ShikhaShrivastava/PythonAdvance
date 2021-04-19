from threading import *

if __name__=='__main__':
    print('The current thread is:', current_thread().getName())
    current_thread().setName('Shikha Thread')
    print('The current thread name is:',current_thread().getName())
    print('The ID of current thread:',current_thread().ident)
from threading import *
import time
def traffic_police():
    while True:
        print('Traffic police is going to give green signal in some seconds')
        time.sleep(10)
        print('Traffic police gave green signal')
        e.set()
        time.sleep(20)
        print('Traffic police gave red signal')
        e.clear()
def driver():
    number=1
    while True:
        print('Driver thread is waiting for green signal')
        e.wait()
        print('Got Green Signal from police')
        print('Vehicle started moving')
        while e.isSet():
            print('Vehical number',number,'is-moving')
            number=number+1
            time.sleep(2)
        print('Vehical stopped moving as police gave red signal')

if __name__ == '__main__':
    e=Event()
    police_thread= Thread(target=traffic_police)
    driver_thread=Thread(target=driver)
    police_thread.start()
    driver_thread.start()
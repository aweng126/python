# processLock.py
from multiprocessing import Process,Lock
import os
import time ,random
'''
如果没有锁
'''
def hello(num):
    time.sleep(random.randint(1,5))
    print("%s this is pid %s"%(num,os.getpid()))


def helloWithOrder(lock,num):
    lock.acquire()
    try:
        time.sleep(random.randint(1,5))
        print("%s this is pid %s"%(num,os.getpid()))
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        # Process(target = hello,args=(i,)).start()
        Process(target = helloWithOrder,args=(lock,i)).start()
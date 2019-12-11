# multiProcessTest1.py
from multiprocessing import Process
import os

def hello(name):
    print("hello %s this is pid %s"%(name,os.getpid()))

if __name__ == '__main__':
    print("this is main process pid = %s "%os.getpid())
    p = Process(target = hello,args=('bob',))
    p.start()
    p.join()
    print("child finished,this is main process pid = %s"%os.getpid())
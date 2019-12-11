# multiThread.py
# 重新run方法来实现多线程
import threading 
import os

def hello(i):
    print("pid = %s current_thread = %s I am %s"%(os.getpid(),threading.current_thread(),i))

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target = hello,args =(i,))
        t.start()
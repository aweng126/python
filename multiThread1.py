# -*- coding: UTF-8 -*-
# multiThread1.py 
# 通过继承threading.Thread来定义线程类，本质是重构Thread类中的run方法
import threading
import os

class helloThread(threading.Thread):
    def __init__(self, n):
        super(helloThread,self).__init__()
        self.n = n

    def run(self):
         print("pid = %s current_thread = %s I am %s"%(os.getpid(),threading.current_thread(),self.n))
 
if __name__ == '__main__':
     for i in range(10):
        t = helloThread(i)
        t.start()
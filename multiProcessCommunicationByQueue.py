import os
from multiprocessing import Process,Queue

def sendMsg(msg):
    q.put(msg)
    print("I am the child process %s send the message %s"%(os.getpid(),msg))

if __name__ == '__main__':
    q = Queue()
    p = Process(target= sendMsg,args = ("hello kingwen",))
    p.start()
    p.join()
    print("I %s received the messge %s"%(os.getpid(),q.get()))




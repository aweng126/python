# multiProcessCommunicationByPipe.py
from multiprocessing import Process,Pipe
import os
def sendMsg(conn,msg):
    conn.send("I am the child process %s send the message %s"%(os.getpid(),msg))

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    p = Process(target = sendMsg,args=(child_conn,"hello kingwen",))
    p.start()
    print("this is parent process %s ,msg from child is :%s"%(os.getpid(),parent_conn.recv()))
    p.join()
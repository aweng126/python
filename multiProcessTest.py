import os
# 主进程id
print("Process %s start "%(os.getpid()))

pid = os.fork()

if pid == 0:
    print("this is child process %s ,and my parents is %s"%(os.getpid(),os.getppid()))
else:
    print("I %s created my child %s "%(os.getpid(),pid))
    
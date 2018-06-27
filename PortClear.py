import os
import sys
import signal
#启动前先杀占用udp 8888端口进程
def kill():
    try:
        pid = os.popen("lsof -i udp:8888 | awk '{print $2}'").read().split('\n')[1]
        a = os.kill(int(pid), signal.SIGKILL)
        print('已杀死pid为%s的进程,　返回值是:%s' % (pid, a))
    except OSError:
        print('端口没有占用')
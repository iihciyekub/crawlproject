
import threading
import time
import random


def func(num):
    print("第%s条线程%s" % (num, threading.currentThread().getName()))
    time.sleep(random.randint(1, 3))


threads = [threading.Thread(target=func, args=(i,)) for i in range(4)]

for t in threads:
    t.start()
    while True:
        # 判断正在运行的线程数量,如果小于5则退出while循环,
        # 进入for循环启动新的进程.否则就一直在while循环进入死循环
        if(len(threading.enumerate()) < 5):
            break
        print("end")

import threading
import threadpool
import time


def run_pro(num):
    time.sleep(1)
    print("thread-%s" % (num))


# 创建线程池
tpool = threadpool.ThreadPool(10)
# 线程池中放中线程
tasks = threadpool.makeRequests(run_pro, [i for i in range(51)])
# 执行线程池中的线程
[tpool.putRequest(i) for i in tasks]
# 等待所有线程执行完毕
tpool.wait()

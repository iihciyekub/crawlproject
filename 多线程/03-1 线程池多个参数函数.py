# import threading
# import threadpool
# import time


# def run_pro(num,ie):
#     time.sleep(1)
#     print(num,ie)


# # 创建线程池
# tpool = threadpool.ThreadPool(10)
# # 线程池中放中线程


# list_var1 = [1,2]
# list_var2 = [4,5]
# par_list = ((list_var1, None), (list_var2, None))


# tasks = threadpool.makeRequests(run_pro, par_list)
# # 执行线程池中的线程
# [tpool.putRequest(i) for i in tasks]
# # 等待所有线程执行完毕
# tpool.wait()


import threading
import threadpool
import time


def run_pro(num,ie):
    time.sleep(1)
    print(num,ie)


# 创建线程池
tpool = threadpool.ThreadPool(10)
# 线程池中放中线程

list_ie = ['w1','w2','w3','w4','w5','w6','w7','w8','w9','w10']
list_num = [i for i in range(len(list_ie))]
list_none = [None for _ in range(len(list_ie))]
er=zip(zip(list_num,list_ie),list_none)
tasks = threadpool.makeRequests(run_pro, er)
# 执行线程池中的线程
[tpool.putRequest(i) for i in tasks]
# 等待所有线程执行完毕
tpool.wait()

from concurrent.futures import ThreadPoolExecutor
import time


def fun(num):
    time.sleep(1)
    print("start:%s" % num)


def second():
    st = time.time()
    for i in range(10):
        fun(i)
    end = time.time()
    print("全部线程执行完毕%.2f" % (end-st))


def main():
    start = time.time()
    et = ThreadPoolExecutor(5)
    et.map(fun, [i for i in range(10)])
    # 通过shutdown()方法等待线程结束后执行后面的代码
    et.shutdown()
    end = time.time()
    print("全部线程执行完毕%.2f秒" % (end-start))


if __name__ == "__main__":
    main()
    # second()

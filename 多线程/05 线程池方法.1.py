from concurrent.futures import ThreadPoolExecutor
import time


def fun(num):
    time.sleep(1)
    print("start:%s" % num)


def main():
    start = time.time()
    with ThreadPoolExecutor(5) as et:
        et.map(fun, [i for i in range(20)])
    end = time.time()
    print("全部线程执行完毕%.2f秒" % (end-start))


if __name__ == "__main__":
    main()

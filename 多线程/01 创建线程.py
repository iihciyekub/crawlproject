# import threading
# import time


# def run_pro(num):
#     time.sleep(2)
#     print("end %s" % (num))


# if __name__ == "__main__":
#     for i in range(11):
#         p = threading.Thread(target=run_pro, args=[str(i)])
#         p.start()
#     p.join()
#     help(p.join)
#     print('线程运行结束')

import threading
import time


def run_pro(num):
    time.sleep(2)
    print("end %s" % (num))


if __name__ == "__main__":

    for i in range(11):
        p = threading.Thread(target=run_pro, args=[str(i)])
        p.start()
    p.join()
    help(p.join)
    print('线程运行结束')

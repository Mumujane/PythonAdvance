"""
程序中是否有线程和进程

进程是操作系统分配资源的基本单位
线程是cpu挑食的基本单位, 就是用来执行代码的

"""
import threading

import multiprocessing


def main():
    print(threading.current_thread().name)
    print(multiprocessing.current_process().name)


if __name__ == '__main__':
    main()


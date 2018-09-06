"""
简单的使用进程

# 子进程中不能使用input函数
第一个执行的线程就叫 主线程
一个进程中就自带一个线程
线程是用来执行代码的, 进程是用来分配资源的

"""
import multiprocessing
import threading

import os

import time


def dance():
    print()
    print("子进程: ", multiprocessing.current_process().name)
    print("子进程线程: ", threading.current_thread().name)
    print("子进程中的pid", os.getpid()) # 进程号
    print("子进程中的ppid", os.getppid()) # 由那个主进程创建,我们叫这个进程为父进程

    for i in range(100):
        time.sleep(1)
        print("dance")


def sing():
    print()
    print("子进程: ", multiprocessing.current_process().name)
    print("子进程线程: ", threading.current_thread().name)
    print("子进程中的pid", os.getpid())  # 进程号
    print("子进程中的ppid", os.getppid())  # 由那个主进程创建,我们叫这个进程为父进程

    for i in range(100):
        time.sleep(1)
        print("sing")


def main():
    """ 开启进程, 一遍跳舞,一遍唱歌"""

    # 打印主进程名字
    print("主进程: ", multiprocessing.current_process().name) # MainProcess
    print("主进程中的线程: ", threading.current_thread().name) # MainThread
    print("主进程中pid:", os.getpid()) # # 进程号 每次不一样? => 因为系统每次分配的空间是随机的

    multiprocessing.Process(target=dance).start()
    multiprocessing.Process(target=sing).start()


if __name__ == '__main__':
    main()
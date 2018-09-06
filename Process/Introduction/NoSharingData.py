"""
进程之间数据是不共享的
    子进程会复制主进程的资源数据
    确定唯一的数据跟进程号+id
    并发epoll 技术
"""
import multiprocessing

import time

num = 0


def write():
    global num
    for i in range(100):
        num += 1
        print("写:", num, id(num))
        time.sleep(1)


def read():
    for i in range(100):
        print("读: ", num, id(num)) # 一直都是0 
        time.sleep(1)


def main():
    multiprocessing.Process(target=write).start()
    multiprocessing.Process(target=read).start()
    print("主进程: ", id(num))


if __name__ == '__main__':
    main()
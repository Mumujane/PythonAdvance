"""
Q:线程之间是否共享全局变量?

    定义两个线程,一个全局变量
    一个线程, 读
    一个线程, 写
"""
import threading
from time import sleep

num = 0


def fun1():
    global num
    while True:
        num += 1
        sleep(1)


def fun2():
    while True:
        sleep(1)
        print(num)


def main():
    thread_01 = threading.Thread(target=fun1)
    thread_01.start()
    thread_02 = threading.Thread(target=fun2)
    thread_02.start()

if __name__ == '__main__':
    main()
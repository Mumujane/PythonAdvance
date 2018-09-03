#定义一个全局变量,一个线程读, 一个线程写
import threading
from time import sleep

num = 0


def write():

    global num
    for i in range(100000):
        num += 1
        sleep(1)


def read():
    while True:
        print("读到的数据:", num)
        sleep(1)


def main():
    thread_write = threading.Thread(target=write)
    thread_write.start()

    thread_read = threading.Thread(target=read)
    thread_read.start()


if __name__ == '__main__':
    main()
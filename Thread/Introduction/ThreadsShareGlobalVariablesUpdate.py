"""
定义一个全局变量
多个线程同时修改这个变量
会出现问题

解决方案-> 加 锁


"""
import threading
from time import sleep

num = 0


# 定义一个锁
lock = threading.Lock()

def write1():
    global num
    for i in range(200000):
        lock.acquire()
        num += 1
        lock.release()
    print("write1 num = %d"%num)


def write2():
    global num
    for i in range(200000):
        lock.acquire()
        num += 1
        lock.release()
    print("write2 num = %d"%num)


def main():
    thread_write1 = threading.Thread(target=write1)
    thread_write1.start()

    thread_write2 = threading.Thread(target=write2)
    thread_write2.start()

    print("counting over")
    sleep(3)
    print(num)

if __name__ == '__main__':
    main()
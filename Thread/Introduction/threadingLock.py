"""
使用互斥锁完成2个线程对同一个全局变量各加100万次的操作

 => 加上互斥锁，那个线程抢到这个锁我们决定不了，那线程抢到锁那个线程先执行，没有抢到的线程需要等待
    加上互斥锁多任务瞬间变成单任务，性能会下降，也就是说同一时刻只能有一个线程去执行


#  没有显示出异常...,  这个代码有问题...
"""
import threading

import time

num = 0

# 创建全局互斥锁
# lock = threading.Lock()

def sum_num1():

    # lock.acquire()
    global num
    for i in range(1000000):
        num += 1

    print("sum 1:", num)
    # lock.release()

def sum_num2():

    # lock.acquire()
    global num
    for i in range(1000000):
        num += 1

    print("sum 2:", num)
    # lock.release()


def main():

    thread_01 = threading.Thread(target=sum_num1)
    thread_02 = threading.Thread(target=sum_num2)
    thread_01.start()
    thread_02.start()
    time.sleep(1)
    print("num: ", num)


if __name__ == '__main__':
    main()


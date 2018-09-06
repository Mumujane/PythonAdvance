"""
进程同步使用


进程池
    重复使用进程(复用我们创建的进程)
进程的问题
    gil 不能把cpu效率最高
    浪费资源

同步的特点:
    一个一个执行我们的任务

创建一个复制的任务

"""
import multiprocessing

import os

import time


def copy():
    print("copy ", os.getppid())
    time.sleep(3)

# 把任务加入到进程池内, 创建一个进程池:


pool = multiprocessing.Pool(3) # 创建三个进程在进程池中


# 循环加入五个任务 到池中
for i in range(5):
    pool.apply_async(copy) # 异步, 有问题,必须加入join和close

    pool.apply(copy) # 同步,一个一个任务执行 (有问题)

# 关闭不在接收新的任务
pool.close()

# 让我们的主进程等待进程池完成再结束
pool.join()





















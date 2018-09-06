"""
进程操作队列

"""
import time

import multiprocessing


queue = multiprocessing.Queue(2)


def write():

    for i in range(100):
        queue.put(i)
        time.sleep(1)


def read():
    for i in range(100):
        print("读到的: ", queue.get(i))
        time.sleep(2)


def main():
    multiprocessing.Process(target=write).start()
    multiprocessing.Process(target=read).start()



if __name__ == '__main__':
    main()
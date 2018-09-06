"""
关闭子进程
    # 实现两个任务
    # 线程执行是无序的
"""
import time

import multiprocessing


def sing():
	for temp in range(100):
		time.sleep(.5)
		print("sing")


def dance():
	for temp in range(10):
		time.sleep(.5)
		print("dance")


def main():
    sing_process = multiprocessing.Process(target=sing)
    sing_process.start()
    dance_process = multiprocessing.Process(target=dance)
    dance_process.start()

    time.sleep(1)

    sing_process.terminate()



if __name__ == '__main__':
    main()
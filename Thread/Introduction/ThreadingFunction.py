"""
一些线程的方法

多线程的创建步骤:
    1.创建一个任务
        一个函数 一个功能 一个任务
    def test():
        pass
    2.把任务加入到线程类中
        任务的线程对象 = threading.Thread(target= 任务的引用)
    3.开启任务
        任务的线程对象.start()


"""
import threading

import time


def coding():
    print("子线程", threading.current_thread().name)

    while True:
        code = input()
        print("coding: ", code)


def songs():
    print("子线程", threading.current_thread().name)
    while True:
        print("songs")
        time.sleep(1)


def main():
    print("主线程:", threading.current_thread().name)

    print("线程列表1", threading.enumerate()) # 查看当前正在运行的线程列表

    thread_coding = threading.Thread(target=coding)
    thread_coding.start()

    print("线程列表2", threading.enumerate())
    thread_songs = threading.Thread(target=songs)
    thread_songs.start()

    print("线程列表3", threading.enumerate())



if __name__ == '__main__':
    main()
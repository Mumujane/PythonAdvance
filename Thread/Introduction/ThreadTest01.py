"""
多线程的创建
    导包
    把任务加入到线程类中
    任务的线程对象 = threading.Thread(target=任务的引用)

    开启任务
    .start()


eg 一遍唱歌, 一边跳舞
"""
import threading
from time import sleep


def song(name, age):

    for i in range(3):
        print("sing a song %d"% i)
        sleep(1)


def dance(name, age):
    for i in range(3):
        print("age: %d name: %s dance in the floor %d" %(age ,name, i))
        sleep(1)

def main():
    thread_song = threading.Thread(target=song, kwargs={'name':'靖哥哥','age':18})
    thread_song.start()

    thread_dance = threading.Thread(target=dance, args=("靖哥哥", 19))
    thread_dance.start()


if __name__ == '__main__':
    main()
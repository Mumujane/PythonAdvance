"""
以下案例是 关于怎么使用协程

提示:

"""
import gevent
import time

from gevent import monkey

# 请猴子, 打补丁
monkey.patch_all()


def sing():
    while True:
        print("Sing a song")
        time.sleep(1)


def dance():
    while True:
        print("Dance in the floor")
        time.sleep(1)


def main():
    """ dance and dance in the meantime """
    sing_g = gevent.spawn(sing)
    dance_g = gevent.spawn(dance)

    gevent_list = list()

    gevent_list.append(sing_g)
    gevent_list.append(dance_g)

    gevent.joinall(gevent_list)

if __name__ == '__main__':
    main()
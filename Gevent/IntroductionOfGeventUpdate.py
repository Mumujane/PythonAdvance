"""
使用协程的步骤分析:

1. 导入gevent
2. 请求猴子打补丁
3. 加入任务
4. 加入等待列表

"""
import time
import gevent
from gevent import monkey

monkey.patch_all()

def sing(name, num):
    while True:
        print("Sing a song", name, num)
        time.sleep(1)


def dance():
    for temp in range(5):
        print("dance")
        time.sleep(1)


def main():
    sing_g = gevent.spawn(sing, "jay", "12")
    dance_g = gevent.spawn(dance)

    gevent_list = list()
    gevent_list.append(sing_g)
    gevent_list.append(dance_g)

    gevent.joinall(gevent_list)


if __name__ == '__main__':
    main()
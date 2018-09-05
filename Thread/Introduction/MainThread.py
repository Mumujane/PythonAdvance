"""
守护主线程

#测试主线程是否会等待子线程执行完成以后程序再退出
设置成为守护主线程 主线程退出后子线程直接销毁不再执行子线程的代码

"""
import threading
from time import sleep


def task():
    for i in range(5):
        print("test", i)
        sleep(.5)


def main():
    # 创建子线程守护主线程
    # 守护主线程方式1
    # sub_thread = threading.Thread(target=task, daemon=True)
    sub_thread = threading.Thread(target=task, daemon=False)

     #

    # 守护主线程方式2
    sub_thread.setDaemon(True)
    # =======分割线

    sub_thread.start()
    sleep(.5)
    print("over")


if __name__ == '__main__':
    main()
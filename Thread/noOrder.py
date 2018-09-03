"""
线程之间执行是无序的
主线程会等待所有子线程结束后才结束
"""
import threading
from time import sleep


def task():
    sleep(1)
    print("当前线程:", threading.current_thread())

def main():
    for i in range(15):
        sun_thread = threading.Thread(target=task)
        sun_thread.start()

        # sun_thread2 = threading.Thread(target=task)
        # sun_thread2.start()

        # sun_thread3 = threading.Thread(target=task)
        # sun_thread3.start()

    sleep(1)
    print("over")

if __name__ == '__main__':
    main()
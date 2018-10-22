"""
计算函数的执行次数
"""
import time


def set_fun(func):
    num = 0

    def call_fun(*args, **kwargs):
        nonlocal num
        num += 1

        print("当前次数:", num)

        return func(*args, **kwargs)

    return call_fun


@set_fun
def becounted_fun():
    print("test")

becounted_fun()
becounted_fun()
becounted_fun()


""" 计算函数的执行时间 """


def set_fun(func):
    def call_fun(*args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        # 第一次时间
        first_time = time.time()
        fun = func(*args, **kwargs)
        # 时间差
        end_time = time.time() - first_time
        print("执行时间为: ", end_time)
        return fun

    return call_fun


@set_fun
def count_time():
    print("count_time")
    time.sleep(1)


@set_fun
def count_time2():
    print("count_time2")
    time.sleep(2)


count_time()
count_time2()
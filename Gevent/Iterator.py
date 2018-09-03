"""
自定义迭代器

    迭代器就是一个可以被for 遍历的对象
    实现两个魔法方法 __iter__ 和 __next__
    如果 只实现了 __iter__ 这个不是迭代器,只是一个可迭代对象
"""
from collections import Iterable


class MyIter(object):
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        if self.num >= 50:
            raise StopIteration
        return self.num


a = list()
# for temp in MyIter():
#     print(temp)
#
# print()
# print(len(a))
my_iter = MyIter() # 迭代器, 可迭代对象
iter_my = iter(my_iter) #通过iter()函数获取这些可迭代对象的迭代器 可以对获取到的迭代器不断使⽤next()函数来获取下⼀条数据。iter()函数实际上就是调⽤了可迭代对象的    __iter__    ⽅法。

print(iter_my)

print(next(iter_my))
print(next(iter_my))
print(next(iter_my))

# a = list()
# print(MyIter()) # <__main__.MyIter object at 0x108914400>
# print(isinstance(MyIter(), Iterable)) # True
#
# # for temp in range(50):
# #     a.append(temp)
#
# # print(len(a))
# # for temp in a:
#     print(temp)

# # 常用的：
# import psutil
# import os
#
# # 查看内存
# info = psutil.virtual_memory()
# print(u'内存使用：', psutil.Process(os.getpid()).memory_info().rss)
# print(u'总内存：', info.total)
# print(u'内存占比：', info.percent)
# print(u'cpu个数：', psutil.cpu_count())

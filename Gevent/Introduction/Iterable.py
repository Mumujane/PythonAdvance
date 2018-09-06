"""
自定义可迭代对象

"""
# 常用的：
import psutil
import os

# 创建一个list列表
a = list()
for i in range(1000000):
    a.append(i)

for temp in a:
    print(temp)

# 查看内存
info = psutil.virtual_memory()
print (u'内存使用：',psutil.Process(os.getpid()).memory_info().rss)
print (u'总内存：',info.total)
print (u'内存占比：',info.percent)
print (u'cpu个数：',psutil.cpu_count())
"""
# 可迭代的对象

"""
from collections import  Iterable

a = "1234ksadk"
for temp in a:
    print(temp)

print(isinstance(a, Iterable))

# isinstance : 判断类型是否一致, isinstance(a, Iterable) 判断是否可迭代

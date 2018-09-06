"""
生成器

# 第一式列表推导式

"""
a = [x for x in range(20)]
print(a) # a 是一个列表
for temp in a:
    print(temp)


a = (x for x in range(10)) # 生成器
print(a) # <generator object <genexpr> at 0x10d63bb48>

# 生成器是一种特殊方式产生的迭代器,可以使用for循环遍历
# for temp in a:
#     print(temp)


"""
生成器 

第二式
"""
def my_iter():
    for temp in range(10):
        yield temp

print("**********分割线*******")
print(my_iter()) #<generator object my_iter at 0x106031ba0>
# for temp in my_iter():
#     print(temp)

iter_my = iter(my_iter())
print(iter_my) #<generator object my_iter at 0x10bc22ba0>

print(next(iter_my))
print(next(iter_my))
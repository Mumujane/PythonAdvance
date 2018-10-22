""" 类装饰器 """


class MyFun(object):
    def __init__(self):
        print("初始化")

    def __call__(self, *args, **kwargs):
        print("实例对象()")


fun = MyFun()
fun()  # 实例对象() 会调用 call 方法

print("====")


class MyFun2(object):
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print("添加额外的功能")
        self.fun()


@MyFun2
def funtest():
    print("test")


funtest()

print("=====")
"""
类装饰器传参
"""


class MyFun3(object):
    def __init__(self,fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print("额外的功能")
        self.fun()

    @classmethod
    def set_value(cls, value):
        print(type(cls))
        print(value)

        return cls


@MyFun3.set_value("younghui") # 1,得到类的引用 @MyFun3.set_value("younghui") , 2,@类的引用(@MyFun)
def fun3test():
    print("test")


fun3test()
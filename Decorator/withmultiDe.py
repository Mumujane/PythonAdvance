"""
多个装饰器装饰一个函数
"""


def set_fun1(fun1):
    print("fun1")

    def call_fun1():
        print("call_fun1")
        fun1()

    return call_fun1


def set_fun2(fun2):
    print("fun2")

    def call_fun2():
        print("call_fun2")
        fun2()

    return call_fun2


@set_fun2  # => tfun = set_fun2(tfun)
@set_fun1
def tfun():
    print("test")


# tfun()
print("==== 分割线 ====")

""" 
    装饰器传参 
    
    固定的写三个函数的嵌套
    最外层必须返回闭包的引用, 第三次必须有参数
    (不会更改原来装饰器得到的结论)

"""


def set_value(value):
    print("set_value")

    def set_fun(func):
        print("set_fun")

        def call_fun(*args, **kwargs):
            print("添加权限", value)
            return func(*args, **kwargs)

        return call_fun

    return set_fun


@set_value("name")
def funte():
    print("test")


funte()

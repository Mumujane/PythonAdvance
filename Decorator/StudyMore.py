"""
使用装饰器

"""
# 初级模板:


def set_fun(func):
    def call_fun():
        print("添加额外的功能")
        func()
    return call_fun


@set_fun # @set_fun ==>  decotest = set_fun(decotest)
def decotest():
    print("test")


#decotest()

# 函数情况:
# 无参,无返回
# 无参,有返回
# 有参,无返回
# 有参,有返回

def set_defun(func):
    def call_fun(*args, **kwargs):
        print("call_fun:", args)
        print("call_fun:", kwargs)
        return func(*args, **kwargs)

    return call_fun()


def detest(*args, **kwargs):
    print(args)
    print(kwargs)
    return 100


print(detest())
#
# print(detest(1, 2, 3))
# print(detest(233,3,a=1,b=2))
#
# detest(1,2,name="okd")
"""万能装饰器"""


def set_fun(func):
    def call_fun(*args, **kwargs):
        print("test add 1")
        return func(*args, **kwargs)
    return call_fun


@set_fun
def funtest1(args):
    print("test", args)
    return args

print(funtest1(123))

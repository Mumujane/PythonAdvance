class MyFun(object):
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print("hello")
        self.fun()


@MyFun # MyFun => test = MyFun(test)
def fun1():
    print("test")


fun1()
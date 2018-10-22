# 装饰器的推导3:
def set_fun(func):
    def call_fun():
        print("权限认证")
        func()

    return call_fun


@set_fun
def transfer():
    print("转账")

@set_fun
def get_money():
    print("收钱")


transfer()
get_money()
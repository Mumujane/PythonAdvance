""""闭包修改外层函数的值"""

# 关键字 global

num = 100

def set_value(value):
    def inner():
        print(value)
        global num
        num += 1
        print(num)
    return inner

inner_fun = set_value(123)
inner_fun()


# 关键字 nonlocal
def set_innervalue(value):
    def inner():
        nonlocal value
        value += 1
        print(value)

    return inner

inner_fun = set_innervalue(123)
inner_fun()
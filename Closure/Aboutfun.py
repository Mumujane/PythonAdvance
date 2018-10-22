"""
关于函数的学习
"""

def tes(args):
    print("test", args)


def tes2(args):
    print(args)
    args(66666)


def main():
    tes(123)
    tes2(tes)


if __name__ == '__main__':
    main()




def tes(args):
	print("test",args)

tes(123)


# print(test) # 引用
#
# test() # 调用



def tes2(args):
	print(args)

	# 调用
	args(6666)

# test2(123)

tes2(tes)
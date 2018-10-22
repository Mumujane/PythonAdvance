"""
查询结果
    search 不会从头开始匹配,只要匹配到数据就结束
    案例:匹配出文章阅读的次数中的次数
    数据:"阅读次数为 9999"

"""
import re


# 只能找一次  search
str_data = "阅读次数为 9999alsdkfjasdf789"
print(re.search("\d+", str_data).group())


# 查询结果集 findall
# 案例: 统计出python、c、c + +相应文章阅读的次数
# 数据: "python = 9999, c = 7890, c++ = 12345"
str_data = "python = 9999, c = 7890, c++ = 12345"
print(re.findall("\d+", str_data))

# 字符串切割 split
# 切割字符串“info:xiaoZhang 33 shandong”, 根据:或者空格
str_data = "info:xiaoZhang 33 shandong"
print(re.split(":|\s", str_data))

# 替换数据 sub
# 案例: 将匹配到的阅读次数换成998
# 数据: "python = 997"
# re.sub("匹配","替换成什么","在那里替换")  # 生成一个新的数据

str_data = "python = 997 = 000 = 12345"
print(re.sub("\d+", "998", str_data))


# 通过函数来修改值
# macth匹配的对象会传入

def test(match):
    print(match.group())
    return "1998"


str_data = "python = 90909"
print(re.sub("\d+", test, str_data))


# [^字符]
#   这个是固定的一个语法,这个意思就是非
#   场景oldyang@163.com oldyang@163.com,我们想取到第一个邮箱
#   如果写字符串有可能会有错,他会去匹配一个字符串出错

str = " oldyang@163.com oldyang@qq.com  oldyang@gmail.com"
print(re.match("[^@]+@163\.com", str).group()) # ^@和 @ 一起用的 ; 只能匹配第一个@符合要求的邮箱, 如果不符合,后面符合也找不到了

# [^字符]字符  非字符

# 非b
print(re.match('[^bc]+', '3433wfdebcsf').group())


str = " oldyang@gmail.com oldyang@163.com  oldyang@163.com oldyang2@gmail.com oldyang@163.com"
print(re.match(".+@gmail.com", str).group())
print(re.match(".+?@gmail.com", str).group())

# => 多字符是修改单字符  ,?是对多字符的限定
# python默认是贪婪的 ?就是非贪婪


"""
原字符
    作用:让我们少写\\的转转义
    原字符的\\\\转成\\
"""
print("\\")
print("\\\\")
print("\\\\\\\\")

# r 原字符
print(re.match("\\\\", "\\").group())
print(re.match("\\\\\\\\", "\\\\").group())
print(re.match("\\\\\\\\\\\\\\\\", "\\\\\\\\").group())

# r 的作用是原始\\ 不需要转义
print(re.match(r"\\", "\\").group())
print(re.match(r"\\\\", "\\\\").group())
print(re.match(r"\\\\\\\\", "\\\\\\\\").group())














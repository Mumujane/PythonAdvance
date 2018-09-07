"""
匹配单个字符

.  匹配任意1个字符,除了/n
[] 匹配 [ ] 中列举的字符,[abc232e] [a-z]
\d 匹配数字 0-9
\D 匹配非数字
\s 匹配空白, 即空格, tab键\t, \n
\S 匹配非空白
\w 匹配单词字符, a-z, A-Z, 0-9, _, 国家的汉子
\W 匹配非单词字符


"""
import re

str = "helloworld1"

print(re.match('helloworld\d', str).group())  # helloworld1

# []
# [范围... ]
str = "helloworld3"
print(re.match("helloworld[135]", str).group())  # helloworld3
print(re.match("helloworld[12345]", str).group())  # helloworld3
print(re.match("helloworld[1-5]", str).group())  # helloworld3


# 格式3:[数字字符]
# 判断用户输入的helloworld 1到8或者helloworld a-h
str = "helloworld6"
print(re.match('helloworld[12345678]', str).group())
print(re.match('helloworld[1-8]', str).group())
print(re.match('helloworld[1-8a-h]', str).group())

# 使用\w 即a-z、A-Z、0-9、_这个范围太广,不要轻易用,汉字也可以匹配,其他的国家的语言也可以匹配
# 匹配的单词字符
# 判断用户输入包含速度与激情
str = "helloworldいきった"
print(re.match('helloworld\w', str).group())

# 使用 \s
# 匹配空白字符, 空格 或 tab(\t)  \n
str = "helloworld\t00"
print(str)
print(re.match("helloworld\s00", str).group())

str = "helloworld\n1"
print(str)
print(re.match('helloworld\s1', str).group())

# 大写是所有小写的非

# 匹配任意一个字符
# -- 匹配任意的字符
# -- 判断包含helloworld 字符串的
str = "helloworld 8"
print(re.match("helloworld..", str).group())
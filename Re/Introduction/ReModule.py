"""
re：通过正则表达式在字符串中进行模式匹配

re.match 用来匹配数据
re.group 用来获取匹配的数据
"""

a = "helloworld!"
print(a.startswith("hell"))  # True
print(a.endswith("ld!"))  # True

# 使用正则
import re

# 使用match进行匹配
# re.match("匹配的规则","要匹配的内容")
#  => 匹配了返回一个对象, 没有返回 None
# match 是从头开始匹配的

print(re.match("he", a))  # <_sre.SRE_Match object; span=(0, 2), match='he'>


match = re.match("^hell", a)
if match:
    print(match.group())  # 得到匹配的值 => hell
else:
    pass



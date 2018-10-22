"""
^ 以什么开始 python语言的match是自动添加的,其他语言不是这样,所以必须添加
$ 以什么结尾

匹配变量名是否有效~
    字母_开头,后面可以写数字,字母_
    匹配规则: 字母_开头,
    匹配的数据:

"""""
import re

names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "------"]

for temp in names:
    match = re.match("^[a-zA-Z_][a-zA-Z\d_]*$", temp)
    # match = re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', temp)
    if match:
        print(match.group())
    else:
        print("没匹配", temp)


""""
转义

\进行转义

在正则特殊的符号, 想以字符串的形式使用 需要使用转义

举例: 匹配出gmail的邮箱地址，且 @ 符号之前有4到20位字符, 以.com结尾

"""
print("++++++++")
str = "janezeng052@gmail.com"
print(re.match(".{4,20}@gmail\.com", str).group())


"""
分组 | 
    | 相当于python中的or
    
    案例:匹配出163或者126的邮箱
    
    
()还可以单独取出匹配的某一部分数据
分组的作用就是取某一段匹配的数据
在正则中写一个()代表加一个组


# \num用来取第几组用()包裹的数据  \1取第一个内部的括号位置的值
# 格式(xxx)\1 :\1表示获取(xxx)的值
# 案例<html>hh</html>  # 这个一定是有字母,开始跟结束的字母必须一样

"""
str = "oldyang@163.com"
# str = "oldyang@126.com"
# print(re.match(".{4,20}@(163|126).com", str).group())
print(re.match('(.{4,20})@(163|126)\.com', str).group())

str = "<html>hh</html>"
print(re.match('<([a-zA-Z]+)>.*</\\1>', str).group())


str_data = "<html><body>hh</body></html>"
print(re.match('<([a-zA-Z]+)><([a-zA-Z]+)>.*</\\2></\\1>', str_data).group())


"""
使用别名给分组取别名
    格式:(?P<别名>xxx)(?P=别名)

案例<html><body>hh</body></html>
"""
str_data = "<html><body>hh</body></html>"
re.match("<(?P<name1>[a-zA-Z]+)><(?P<name2>[a-zA-Z]+)>.*</(?P=name2)></(?P=name1)>", str_data).group()


# 练习:

str = """
	<div>
        <p>岗位职责：</p>
		<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
		<p><br></p>
		<p>必备要求：</p>
		<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
		<p>&nbsp;<br></p>
		<p>技术要求：</p>
		<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
		<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
		<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
		<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案 </p>
		<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
		<p>&nbsp;<br></p>
		<p>加分项：</p>
		<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

	</div>
	"""
# 从上面的数据中获取文本数据
# 提示 # re.sub("匹配","替换成什么","在那里替换")  # 生成一个新的数据
print(re.sub("<.+?>|\s|nbsp;", " ", str))








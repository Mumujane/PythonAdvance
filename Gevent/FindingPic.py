""" 网络操作

从网络下载图片到本地
# 文件读写三个,网络操作也是三步
"""
from urllib.request import *

# 打开对应图片的地址
url_f = urlopen("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3506739232,2945471821&fm=27&gp=0.jpg")
# 读取
content = url_f.read()

# 保存内容
with open("./1.jpg", 'wb') as f:
	f.write(content)

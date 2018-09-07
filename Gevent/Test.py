# import  re
# str = "0211234567"
#
# print(re.match("\d{3,4}-?\d{7,8}", str).group())
#

# 1. 读取文件
# 2. 通过正则获取所有图片地址
# 3. 批量下载
import ssl

import gevent
from gevent import monkey
from  urllib.request import *
import re

#打个补丁
monkey.patch_all()

def down_image(url_path,save_path):
    """
    下载图片
    :param url_path: 下载的路径
    :param save_path: 保存的路径
    :return: NONE
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    #下载图片
    response_data = urlopen(url_path)
    #读取内容
    content = response_data.read()

    #保存图片
    with open(save_path,'wb') as f:
        f.write(content)


def main():
    """图片下载"""
    # 1. 读取文件
    with open("1.html") as f:
        content = f.read()

    # 2. 通过正则获取所有图片地址
    images_List = re.findall("""data-original="(https?://.+?\.jpg)""", content)
    print(images_List)

    #图片下载的序号
    num = 0

    #创建一个等待的列表
    gevent_list= list()

    # 3. 批量下载
    for temp in images_List:
        #下载
        save_path = "./images/%s.jpg" % num
        #save_path = "/Users/jinjing/PycharmProjects/python高级/day9/images/%s.jpg" % num

        #下载是比较耗时的
        gevent_list.append(gevent.spawn(down_image,temp,save_path))

        #序号加1
        num += 1
    gevent.joinall(gevent_list)



if __name__ == '__main__':
    main()

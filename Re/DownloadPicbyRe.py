"""
图片批量下载器
    读取文件
    通过正则获取所有图片地址
    批量下载
"""
import re
from urllib.request import urlopen


def down_image(url_path, save_path):
    """
    下载图片
    :param url_path: 下载路径
    :param save_path: 保存路径
    :return: NONE
    """
    # 下载图片
    response_data = urlopen(url_path)

    # 读取内容
    content = response_data.read()

    # 保存图片
    with open(save_path, 'wb') as f:
        f.write(content)


def main():
    """图片下载"""
    # 1. 读取文件
    with open("./1.html") as f:
        content = f.read()

    # 2.通过正则获取所有图片的地址
    images_list = re.findall("""data-original="(https?://.+?\.jpg)""", content)
    print(images_list)

    num = 0

    # 3.创建gevent等待列表
    gevent_list = list()

    # 4.批量下载
    for temp in images_list:
        save_path = "./images/%s.jpg"%num
        # TODO 多任务
        down_image(temp, save_path)
        num += 1

    # 5.加入等待


if __name__ == '__main__':
    main()

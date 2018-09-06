"""
gevent多任务图片下载
    创建一个批量的图片的列表
    循环下载 图片

    协程根据耗时自动切换

"""
import gevent

from gevent import monkey

monkey.patch_all()

from urllib.request import urlopen


def download_image(down_path, save_path):
    """

    :param down_path: 下载的地址
    :param save_path: 保存的地址
    :return: NONE
    """
    print("Begin Downloading~", save_path)
    # 打开下载的图片
    image = urlopen(down_path)

    # 得到内容
    content = image.read()

    # 保存
    with open(save_path, 'wb') as f:
        f.write(content)

    print("done", save_path)


def main():
    """ 批量下载图片"""
    image_list = list()
    image_list.append("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3506739232,2945471821&fm=27&gp=0.jpg")
    image_list.append("https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1293860636,1088191402&fm=27&gp=0.jpg")
    image_list.append("https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3711458043,3147749033&fm=27&gp=0.jpg")

    # 图片的位置
    num = 1

    gevent_list = list()
    for temp in image_list:
        save_path = "./images/%s.jpg"%num

        # download_image(temp, save_path)
        g_down_image = gevent.spawn(download_image, temp, save_path)
        gevent_list.append(g_down_image)

        num += 1

    gevent.joinall(gevent_list)


if __name__ == '__main__':
    main()
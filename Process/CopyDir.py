"""
使用进程池完成多任务文件夹的拷贝

    创建一个新的文件夹
    把复制的文件夹的文件遍历一遍
    复制文件的操作(读取文件的内容,在新的文件中创建文件并写入)
"""
import os

import shutil


def copy_file(copy_file_path, new_file_path):
    """
    复制文件
    :param copy_file_path: 要复制的文件路径
    :param new_file_path:   新的文件路径
    :return: NONE
    """
    # 读取文件的内容
    with open(copy_file_path, 'rb') as f:
        content = f.read()

    # 创建新的文件
    with open(new_file_path, 'wb') as f:
        f.write(content)


def main():
    """复制文件夹"""

    # 定义一个旧的文件夹路径
    dir_path = "./Introduction"

    # 定义 一个新的文件夹路径
    copy_dir_path = "./copy_files"

    #
    if not os.path.exists(dir_path):
        print("文件不存在", dir_path)
        return

    #如果存在文件夹则删除
    if os.path.exists(copy_dir_path):
        shutil.rmtree(copy_dir_path)

    #创建文件夹
    os.mkdir(copy_dir_path)

    #遍历文件夹
    dir_list = os.listdir(dir_path)
    print(dir_list)

    #循环复制文件
    for temp in dir_list:
        copy_file_path = dir_path + "/" + temp
        new_file_path = copy_dir_path + "/" + temp

        copy_file(copy_file_path, new_file_path)



if __name__ == '__main__':
    main()
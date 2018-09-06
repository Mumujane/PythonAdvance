# 唱歌,跳舞
def sing():
    while True:
        print("sing a song")
        yield


def dance():
    while True:
        print("dance on the floor")
        yield


def main():
    """生成器使用"""
    # 唱歌的迭代器对象
    song_iter = iter(sing())

    # 跳舞的迭代器对象
    dance_iter = iter(dance())

    while True:
        next(song_iter)
        next((dance_iter))



if __name__ == '__main__':
    main()
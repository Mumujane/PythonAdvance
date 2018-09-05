"""
tcp文件下载客户端

1. 发送路劲
2. 循环返回的数据
3. 写入到一个文件中

"""
import socket

import time


def main():
    """ 客户端"""
    # 初始化
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect(("", 8081))

    tcp_client.send("1.JPG".encode("utf-8"))

    #循环接收数据
    with open("1_back.JPG", 'wb') as f:
        while True:
            data = tcp_client.recv(1024)

            if data == b'001':
                print("文件不存在")
                break

            if data:
                f.write(data)
                print("存储成功~!",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            else:
                break
    tcp_client.close()


if __name__ == '__main__':
    main()
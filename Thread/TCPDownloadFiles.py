""""

文件下载服务器端

# 1. tcp文件下载服务器端
# 2. 读取我们客户端过来的路径,
# 3. 根据路径返回数据,每次返回1024字节
# 4. 发送给客户端

"""
import socket

import os


def client_extc(client):
    data = client.recv(1024)

    file_path = data.decode("utf-8")

    if os.path.exists(file_path):
        f = open(file_path, "rb")
        while True:
            content = f.read(1024)
            if content:
                client.send(content)
            else:
                break
        f.close()
    else:
        error_info = b"001"
        client.send(error_info)
    client.close()


def main():

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(("", 8080))
    tcp_server.listen(128)
    client, addr = tcp_server.accept()

    while True:
        client_extc(client)

    tcp_server.close()


if __name__ == '__main__':
    main()
""""
文件下载服务器端

# 1. tcp文件下载服务器端
# 2. 读取我们客户端过来的路径,
# 3. 根据路径返回数据,每次返回1024字节
# 4. 发送给客户端

"""
import socket

import os
import threading

import time


def client_extc(client):
    data = client.recv(1024)

    file_path = data.decode("utf-8")
    print(file_path)

    if os.path.exists(file_path):
        f = open(file_path, "rb")
        while True:
            content = f.read(1024)
            if content:
                client.send(content)
                print("发送数据ing~", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                # time.sleep(1)
            else:
                print("发送完毕!", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                time.strftime("")
                break
        f.close()
    else:
        error_info = b"001"
        client.send(error_info)
    client.close()


def main():

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置socket选项，防止程序退出端口不立即释放的问题(端口复用)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    tcp_server.bind(("", 8081))
    tcp_server.listen(128)

    # 循环接收用户的请求
    while True:
        client, addr = tcp_server.accept()
        print(addr)
        # client_extc(client)
        client_thread = threading.Thread(target=client_extc, args=(client,))

        client_thread.setDaemon(True)

        client_thread.start()

    tcp_server.close()


if __name__ == '__main__':
    main()
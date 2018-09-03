"""
# tcp聊天服务器端
# 初始化
# 绑定
# 被 动
# 循环接收用户的请求
# 处理数据
# 关闭

"""
import socket
import threading


def client_extc(client):
    #接收用户数据
    while True:
        data = client.recv(1024)
        if data:
            print("接收的数据:", data.decode("utf-8"))
        else:
            break

    client.close()


def main():
    """tcp聊天器"""

    #初始化
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #端口复用, 固定
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    #绑定地址
    tcp_server.bind(("", 8089))

    #被动
    tcp_server.listen(128)

    #循环接收用户请求
    while True:
        client, address = tcp_server.accept()
        # client_extc(client)
        threading.Thread(target=client_extc, args = (client,)).start()

    tcp_server.close()


if __name__ == '__main__':
    main()
"""
TODO:
    没有找到模拟两个tcp客户端连接服务器端,同时发送信息的测试,直接写了代码

"""
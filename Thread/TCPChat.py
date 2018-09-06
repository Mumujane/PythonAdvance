"""
# 服务器TCP聊天工具,  并实现多线程(多个人同时连接服务器)
# 创建套接字
# 绑定端口
# 设置监听
# 循环接收用户的请求
# 处理用户的请求
# 关闭

"""
import socket
import time


def client_ext(client_sock):

    while True:
        data = client_sock.recv(1024)
        if data:
            value = data.decode("utf-8")
            print(value)
            client_sock.send("We have received your message. THX!".encode("utf-8"))
            time.sleep(1)
        else:
            print("客户端断开连接")
            break
    client_sock.close()

def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server.bind(("", 8081))
    print("Client Conneting the Server! ")
    tcp_server.listen(12 )

    while True:
        client_sock, addr = tcp_server.accept()
        client_ext(client_sock)

    tcp_server.close()


if __name__ == '__main__':
    main()
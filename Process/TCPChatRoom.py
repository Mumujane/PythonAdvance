"""
tcp聊天室 -- 多任务进程版
    创建tcp 套接字
    绑定端口以及复用端口
    改成监听模式
    循环接收用户的请求, 并做出回复
    处理用户的请求
    关闭

"""
import socket

import multiprocessing


def client_exe(client):
    while True:
        data= client.recv(1024)
        if data:
            print(data.decode("utf-8"))
            client.send("We have received your message. THX!".encode("utf-8"))
        else:
            break


    client.close()

def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(("", 8082))
    # 复用端口
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.listen(128)


    # 循环接收用户请求:
    while True:
        client, addr = tcp_server.accept()

        multiprocessing.Process(target=client_exe, args=((client,))).start()

        client.close() # 子进程会复制主进程资源??
        # TODO

    tcp_server.close()


if __name__ == '__main__':
    main()



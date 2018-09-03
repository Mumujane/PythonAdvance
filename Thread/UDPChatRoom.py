"""
UDP 聊天室多任务版本案例

初始化udp
绑定端口
循环处理我们的指令
关闭
"""
import socket
import threading


def send_msg(udp_server):
    print("请输入发送的数据")
    data = input()

    print("请输入ip地址:")
    ip = input()

    print("请输入端口号:")
    port = input()

    # 数据的发送
    num = udp_server.sendto(data.encode("utf-8"),(ip, int(port)))
    # print(data)
    # print((ip, int(port)))
    # print(num)


def recive_msg(udp_server):
    # 接收
    data = udp_server.recvfrom(1204)
    print(data[0].decode("utf-8"))
    print(data[1])


def main():
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind(("127.0.0.1", 8082))
    while True:
        print("== == == == == == == == == == == == == == ==")
        print("1: 发送消息")
        print("2: 接收消息")
        print("== == == == == == == == == == == == == == ==")
        print("请输入要操作的功能序号:")

        action = input()
        print(action)
        if action == "1":
            # 发送消息
            send_msg(udp_server)
        elif action == "2":
            # 接收消息

            # 因为只能一条一条接收, 如果对方一次发送多条 服务器这边会出现阻塞问题
            #所以加入多线程
            threading.Thread(target=recive_msg, args=(udp_server,)).start()
        else:
            print("请重新输入")
    udp_server.close()


if __name__ == '__main__':
    main()


"""
TODO : 发送消息 网络助手收不到(接收区不显示发送的内容)
 但是下面👇 的终端可以接收

"""

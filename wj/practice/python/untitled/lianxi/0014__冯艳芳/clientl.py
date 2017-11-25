
#coding=utf8
from socket import *


HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

#创建socket，指明协议
tcpCliSock = socket(AF_INET, SOCK_STREAM)

#连接远程地址和端口，发送syn，等待 syn ack
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('>> ')
    if not data:
        break
    tcpCliSock.send(data)                #发送消息

    # 阻塞式等待接收消息
    data = tcpCliSock.recv(BUFSIZ)
    # 当对方关闭连接的时候，返回空字符串
    if not data:
        break

    print data

tcpCliSock.close()
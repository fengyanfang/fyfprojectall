# coding=utf-8

import thread,socket

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 新线程执行的函数，每个线程负责和一个客户端进行通信
def on_new_client(clientsocket,addr):
    while True:
        data = clientsocket.recv(1024)
        # 当对方关闭连接的时候，返回空字符串
        if not data:
            print u'%s 关闭了连接' % addr
            break
        print '%s:%s' % (addr,data)
        clientsocket.send(data)

    clientsocket.close()


# 主线程 创建监听的socket
serversocket = socket.socket()

serversocket.bind((HOST, PORT))
serversocket.listen(5)

# 在while循环里面 不断接受新的连接请求，
# 并创建新线程专门和这个客户端进行通信
while True:
   clientsocket, addr = serversocket.accept()     # Establish connection with client.
   addr = str(addr)
   print u'从 %s 来的连接' % addr
   thread.start_new_thread(on_new_client,(clientsocket,addr))

serversocket.close()
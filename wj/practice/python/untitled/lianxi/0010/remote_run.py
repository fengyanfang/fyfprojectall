#coding=utf-8
import paramiko,time

# 创建sshcliet的实例对象
ssh = paramiko.SSHClient()

#调用方法，表示没有存储远程机器的的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程主机
ssh.connect("192.168.20.128",22,"fyf","136066")

stdin,stdout,stderr = ssh.exec_command("ls")
lscontend = stdout.read()

#创建目录
cmd1 = "mkdir fengyanfang"

try:
    ssh.exec_command(cmd1)

except:
    print "The dicotionary is alredy existed"


sftp = ssh.open_sftp()
sftp.put('memory.py','/fengyanfang/memory.py')
#检查文件是否传输成功，可以将检查文件是否存在机器做成一个函数

#考虑到长时间没有接受消息，网络可能断开，所以设置一个保持连接的参数
transport = ssh.get_transport()
transport.set_keepalive(30)


cmd2 = "cd fengyanfang;python memory.py"
ssh.exec_command(cmd2)
time.sleep(300)

sftp.get("/fengyanfang/ret.txt","ret.txt")



sftp.close()

ssh.close()

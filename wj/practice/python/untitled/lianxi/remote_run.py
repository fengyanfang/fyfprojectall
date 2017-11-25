#coding=utf-8
import paramiko,time

# 创建sshcliet的实例对象
ssh = paramiko.SSHClient()

#调用方法，表示没有存储远程机器的的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程主机
ssh.connect("192.168.20.128",22,"fyf","136066")
#创建目录
cmd1 = "mldir fengyanfang"

try:
    ssh.exec_command(cmd1)

except:
    print "The dicotionary is alredy existed"


sftp = ssh.open_sftp()
sftp.put('memory.py','/home/fengyanfang/memory.py')
cmd2 = "cd fengyanfang;python memory.py"
ssh.exec_command(cmd2)

stdin,stdout,stderr = ssh.exec_command(cmd2)
info = stdout.read()
with open("ret.txt","w") as f:
    f.write(info)
sftp.get("/home/fengyanfang/ret.txt","ret.txt")



sftp.close()

ssh.close()

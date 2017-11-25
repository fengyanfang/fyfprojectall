#coding=utf-8
import paramiko,time

# 创建sshcliet的实例对象
ssh = paramiko.SSHClient()

#调用方法，表示没有存储远程机器的的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程主机
ssh.connect("192.168.20.128",22,"fyf","136066")

while True:

    start_time = time.time()
    cmd = "cat /proc/meminfo"
    stdin,stdout,stderr = ssh.exec_command(cmd)
    time.sleep(5)
    mem = stdout.read()+stderr.read()

    mem = mem.splitlines()
    m_total = int(mem[0].split(":")[1][:-2].strip())

    #格式化后也是字符串
    m_total = float("%.2f"% m_total)
    # print type(m_total)

    m_free = int(mem[1].split(":")[1][:-2].strip())

    buffers = int(mem[2].split(":")[1][:-2].strip())

    cached = int(mem[3].split(":")[1][:-2].strip())

    avamem = (m_free+buffers+cached)/m_total
    with open("ret.txt","w+") as f:
        f.write(str(avamem))

    time1 = time.strftime("%Y-%d-%m_%H:%M:%S",time.localtime())
    print "%s %.2f" %(time1,avamem)
    time.sleep(5)


    end_time = time.time()
    if start_time-end_time == 120:
        break
    ssh.close()

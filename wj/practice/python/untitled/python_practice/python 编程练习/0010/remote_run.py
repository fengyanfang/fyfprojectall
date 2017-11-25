# coding=utf8
import time

# MemTotal:        1920648 kB
# MemFree:           87788 kB
# Buffers:          229704 kB
# Cached:          1180244 kB
def getContent(lines,field):
    for line in lines:
        if field in line:
            value = line.split(':')[1].split('kB')[0].strip()
            return int(value)

count = 0
while True:
    count += 1

    with open('/proc/meminfo') as f:
        beginlines = f.readlines()[:8]

    memTotal = getContent(beginlines,'MemTotal')
    memFree  = getContent(beginlines,'MemFree')
    buffers  = getContent(beginlines,'Buffers')
    cached   = getContent(beginlines,'Cached')

    # print memTotal,memFree,buffers,cached
    # 先忘了 * 100
    memUsage = (memFree + buffers + cached) *100.0/memTotal
    # 搜索时间格式
    memUsage = '%s     %.2f%%' % (time.strftime('%Y%m%d_%H:%M:%S'),memUsage)
    print memUsage

    with open('ret.txt','a') as f:
        f.write(memUsage+'\n')

    time.sleep(5)

    # 防止一直运行
    if count>15:
        break
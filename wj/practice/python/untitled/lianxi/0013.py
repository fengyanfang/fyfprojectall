#coding=utf8
import requests,threading
from time import sleep,ctime

url_list=[
    "http://mirrors.163.com/centos/6.8/isos/x86_64/README.txt",
    "http://mirrors.163.com/centos/6.9/isos/x86_64/README.txt"
    ]

thread_num = len(url_list)

# 对应urls 依次存储网页文件内容, 先创建同样个数的元素占位
reslist=[None for one in url_list]
print reslist

#调用lock函数，返回一个锁对象
info_lock = threading.Lock()
def thread1_entry(url,idx):
    res = requests.get(url)

    # 在代码访问共享对象之前，给共享对象枷锁
    info_lock.acquire()
    reslist[idx]=res.text

    # 访问完共享对象之后，一定要释放锁，否则会成为死线程
    info_lock.release()




if __name__ == "__main__":               # 是__main__ 别写错啦
    print "the main thread start"
    #线程池
    th_pool = []

    for i in range(thread_num):

        #创建线程函数，指定啦新线程的入口函数
        t1 = threading.Thread(target=thread1_entry,args=(url_list[i],i))   #tuple元素为1个时候，后面必须加“，”
        t1.start()
        th_pool.append(t1)

    for th in th_pool:
        # 等th线程结束
        th.join()

    ret = "\n\n\n----------------------------------------------------\n\n\n".join(reslist)
    with open("C:/classes/ap/redmin89.txt","a") as f:
            f.write(ret)
    print"main thread end"

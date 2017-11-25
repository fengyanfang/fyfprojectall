#coding:utf8
import os,time,glob

res = raw_input("请选择输入的操作,1：录制视频，2：合并视频 :")
# print type(res)
ffmpegdir = "C:/classes/ap/ffmpeg.exe"
if res == "1":
    outputfile = "C:/classes/" +time.strftime("%Y%m%d_%H%M%S",time.localtime())+".mp4"

    #\ 表示这一行字符串还没有写完
    settings ="-y -rtbufsize 100M -f gdigrab -framerate 20"\
            "-draw_mouse 1 -i desktop -c:v libx264 -r 20"\
            "-crf 35 -pix_fmt yuv420p -fs 100M -movflags +faststart %s"%outputfile  #-movflags +faststart 是一体的

    ret = os.system(ffmpegdir+" "+settings)  #文件中的命令必须是字符串

else:
    #列出当前目录下以MP4结尾的文件
    filelist = glob.glob("*.mp4")

    if filelist:
        print u"目录中有视频文件"
    else:
        print u"目录中没有视频文件"

    #创建一个列表，用来记录 1 f.txt形式的文件
    flist = []

    #创建一个字典，用来记录具体的键值对
    filedict = {}

    #enumrate函数是用来显示索引和列表元素的
    for c,f in enumerate(filelist):
        #c是int型
        a = str(c) + " " + f
        flist.append(a)
        for i in flist:
            index = str(i.split(" ")[0])
            file = str(i.split(" ")[1])
            filedict[index] = file
    # print filedict["1"]

    res = raw_input("请选择要合并的文件序号：")
    with open("C:/classes/concat.txt","w") as f:
        #用len函数来做判断
        if len(res) == 1:
          pass
        else:
            #对输入的值存在一个列表中
            res = res.split(",")
            # print res
            for i in res:
                fname = "file " + filedict[i]
                #写在文件中要用换行符，否在挤在一行
                f.write(fname+"\n")
           #注意循环之后再对concat.txt整体操作，所以os.system 要左空两格
            os.system("C:/classes/ap/ffmpeg.exe -f concat -i C:/classes/concat.txt -codec copy out.mp4")








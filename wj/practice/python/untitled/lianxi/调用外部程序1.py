#coding:utf-8
import os,time

outputfile = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()).decode("gbk")+".mp4"

#工具目录
ffmpegDir = "D:/MyDownloads/Download/ffmpeg.exe"

settings = [
    '-y -rtbufsize 100M -f gdigrab -framerate 20', #帧率等
    # '-offset_x 1000 -offset_y 0 -video_size 640*480',录制制定屏幕
    '-draw_mouse 1 -i desktop -c:v libx264',#视频编码格式
    '-r 20 -crf 35 -pix_fmt yuv420p -fs 100M "%s"'%outputfile,
]
recordingcmdline = ' '.join([ffmpegDir]+settings)  #连接起来

# print  recordingcmdline

#调用外部程序
os.system(recordingcmdline)

#看返回值是否是0，0是正确的
# print ret
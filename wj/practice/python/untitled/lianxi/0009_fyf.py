#coding=utf8
import time,threading
from random import randint
import threading,os
class Tiger:
    classname = "tiger"

    def __init__(self,weight=200):
        self.weight = weight

    def tellweight(self):
        print 'my weight is %s'%(self.weight)

    def eat(self,food):
        self.food = food
        if food == "meat":
            self.weight += 10
            print "good weight+10"
        else:
            self.weight -= 10
            print "good weight-10"

    def row(self):
        print 'row!!!'
        self.weight -= 5



class Sheep:
    classname = 'sheep'
    def __init__(self,weight=100):
        self.weight = weight

    def tellweight(self):
        print 'my weight is %s' %(self.weight)

    def eat(self,food):
        if food == "grass":
            self.weight += 10
            print "good weight+10"
        else:
            self.weight -= 10
            print"bad weight -10"

    def row(self):
        print 'mie mie!!!'
        self.weight -= 5


class Room:

    def __init__(self,num,animal):
        self.num = num
        self.animal = animal

# 先随机给动物分配房间
rooms = []
for num in range(10):
    # 循环和条件一起使用，不能用双重循环
    if randint(0, 1) == 0:
        ani = Tiger()
    else:
        ani = Sheep()
    room = Room(num + 1, ani)
    rooms.append(room)


#创建一个线程，记录游戏时间，因为主线程里记录时间涉及用户输入，属于阻塞式的
def count_thread():
    # 记录下游戏开始时间，在循环之前记录，在循环里记录，就是循环一次的时间
    starttime = time.time()
    while True:
        time.sleep(0.1)
        curtime = time.time()
        if curtime - starttime >= 5:
            break

    print u"游戏结束"
    # 游戏结束，输出各个房间的动物和体重
    for room in rooms:
        print u"房间是%s,里面是%s,体重是%s" % (room.num, room.animal.classname, room.animal.weight)

    os._exit(0) #程序正常退出，进程退出

t= threading.Thread(target=count_thread)
t.start()

#循环做如下事情
while True:

    curroomindex = randint(0,9)
    room = rooms[curroomindex]

    #不能用input，不能识别变量
    ai = raw_input(u"欢迎来到房间%s，请选择敲门【q】还是喂食【f】:" %room.num+"\n")

    if ai == "f":
        feed = raw_input(u"请输入你选择喂的食物：")
        room.animal.eat(feed)

    elif ai == "q":
        room.animal.row()
    else:
        print "请重新输入"






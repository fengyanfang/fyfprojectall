#coding=utf8
import time
from random import randint
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
        else:
            self.weight -= 10

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
        else:
            self.weight -= 10
    def row(self):
        print 'mie mie!!!'
        self.weight -= 5


class Room():

    def __init__(self,num,animal):
        self.num = num
        self.animal = animal


#先随机给动物分配房间
def getroom():
    rdict = {}
    rlist = []
    while len(rlist) != 10:
        roomid = randint(1,10)
        if roomid not in rlist:
            rlist.append(roomid)

    animal = ["Tiger","Sheep"]

    for roomid in rlist:
        rdict[roomid] =animal[randint(0,1)]
        ani = rdict[roomid]
        if ani == "Tiger":
            anim = Tiger()
        else:
            anim = Sheep()

        while True:

            time1 = time.time()
            a = int(input(u"开始游戏啦，请选择敲门还是喂食？（2代表敲门，1代表喂食):"))
            roomid = randint(1, 10)
            if a == 1:
                print roomid
                room = Room(roomid, anim)
                f = raw_input(u"请输入你选择喂的食物：")
                room.animal.eat(f)

            else:
                room.animal.row()

            time2 = time.time()
            if time2 - time1 == 10:
                print "房间号:%s ----%s----weight:%s" %(roomid,ani,room.animal.weight)
                break


getroom()












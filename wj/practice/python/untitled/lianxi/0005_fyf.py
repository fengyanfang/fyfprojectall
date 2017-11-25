#coding:utf8


def putInfoToDict(fileName):
    with open(fileName, "r") as fp:
        f = fp.readlines()
        for one in f:
            one = one.replace("(","").replace(")","").replace("'","").split(",")
            # print one
            #分别取出时间，课程号和用户id
            time = one[0].strip()
            courseid = one[1].strip()
            userid = one[2].strip()


            sdict = {}
            # 如果字典中没有useid，
            if userid not in sdict:
                sdict[userid] = [{'time':time,'courseid':courseid}]

            # 否则
            else:
                sdict[userid].append({'time':time,'courseid':courseid})

            print sdict



putInfoToDict("F:/0005_1.txt")


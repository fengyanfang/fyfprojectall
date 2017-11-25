#coding:utf8

#将课程信息做成字典
with open("F:/course.txt") as fc:
    fco = fc.read().decode("utf8")
    fco = fco.splitlines()
    fco.pop(0) #去除第一行内容：字段名称

    course_dict = {}
    for line1 in fco:
        one1 = line1.split(";")
        cour_id = one1[0].strip()
        cour_name = one1[1].strip()
        course_dict[cour_id] = cour_name
    #for c,n in course_dict.items():
        #print c,n

#将老师信息做成字典
with open("F:/teacher.txt") as fs:
    fst =fs.read().decode("utf8")
    fst = fst.splitlines()
    techer_dict = {}
    fst.pop(0)
    for line2 in fst:
        one2 = line2.split(";")
        tea_id = one2[0].strip()
        tea_name = one2[4].strip()
        techer_dict[tea_id] = tea_name
    #for t,n in techer_dict.items():
        #print t,n

#运用字典去实现teacher_course 表中的对应关系
with open("F:/teacher_course.txt") as tc,open("con.txt","w") as fw:
    tch = tc.read().decode("utf8")
    tch = tch.splitlines()
    tch.pop(0)

    for info in tch:
        info = info.split(";")
        tea_id,cour_id = info
        # 防止出错
        if (tea_id not in techer_dict) or (cour_id not in course_dict):
            continue
        con =  "%-s:%-s"%(techer_dict[tea_id],course_dict[cour_id])
        fw.write(con.encode("utf8")+"\n")

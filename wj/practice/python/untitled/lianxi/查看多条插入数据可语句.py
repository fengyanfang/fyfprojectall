#coding=utf8
import sys,time

for i in range(1, 10):
    id = str(i)
    inspection_num = 'NJ' + str(100000 + i)
    car_id = i + 1

    #localtime 是元组类型的，strftime把元祖转化成字符串
    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # # @@@@@字符串用双引号加单引号"''"
    # sql = 'insert into car (id,inspection_num,car_id, create_uid)\
    #    values('+id+',"' + inspection_num + '",' + car_id + ',238);'
    #
    # sql = 'insert into car (id,inspection_num,car_id,create_uid，create_time,update_time) values({},{},{},{},{},{})'.\
    #     format(id,inspection_num,car_id,238,create_time,update_time)

    sql = 'insert into car (id,inspection_num,car_id,create_uid，create_time,update_time) values(%s,%s,%d,%s,%s,%s)'\
       % (id,inspection_num,car_id,238,create_time,update_time)
    print sql


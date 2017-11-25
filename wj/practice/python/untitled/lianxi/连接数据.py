#coding=utf8
from pymysql import connect,cursors
from pymysql.err import  OperationalError
import sys,time

import requests


class DataBase():   #类名和模块名一致，robot导入时不用写类名@@@@@
    def __init__(self,mysql_name):
        try:
            self.conn = connect(host='123.57.214.110',
                                port=3306,
                                user='mysql630',
                                password='YjCsXdL#@.a64L',
                                db=mysql_name,
                                charset ='utf8mb4',
                                cursorclass = cursors.DictCursor
                                )

        except OperationalError as e:
            print e

    def select(self,table_name):

        #sql语句之间应该有空格
        sql = 'select * from '+table_name+';'
        cursor = self.conn.cursor()

        cursor.execute(sql)
        self.conn.commit()
        results = cursor.fetchall()
        for row in results:
            print row
    def insert_inspection_list(self,table_name):
        for i in range(1,10):

            id = str(i)
            inspection_num = 'NJ'+ str(100000+i)
            car_id =  i+1

            create_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            update_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

            # # @@@@@字符串用双引号加单引号"''"
            # sql = 'insert into car (id,inspection_num,car_id, create_uid)\
            #    values('+id+',"' + inspection_num + '",' + car_id + ',238);'
            #
            # sql = 'insert into car (id,inspection_num,car_id,create_uid，create_time,update_time) values({},{},{},{},{},{})'.\
            #     format(id,inspection_num,car_id,238,create_time,update_time)

            sql = 'insert into car (id,inspection_num,car_id,create_uid，create_time,update_time) values(%s,%s,%d,%s,%s,%s)' \
                  % (id, inspection_num, car_id, 238, create_time, update_time)
            print sql
            cursor = self.conn.cursor()

            cursor.execute(sql)
            self.conn.commit()








    # 关闭数据库
    def close(self):
        self.conn.close()
if  __name__ == '__main__':
    tb = DataBase('manager')
    tb.insert_inspection_list('inspection_list')

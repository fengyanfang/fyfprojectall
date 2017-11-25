#coding=utf8
from pymysql import connect,cursors
from pymysql.err import  OperationalError
import sys

import requests


class mysql_data():   #类名和模块名一致，robot导入时不用写类名@@@@@
    def __init__(self,dataname):
        try:
            self.conn = connect(host='123.57.214.110',
                                port=3306,
                                user=dataname,

                               password='YjCsXdL#@.a64L',
                                db='manager',
                                charset ='utf8mb4',
                                cursorclass = cursors.DictCursor
                                )

        except OperationalError as e:
            print e

    def clear(self,table_name):

        #sql语句之间应该有空格
        sql = 'truncate table'+' '+table_name+';'
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(sql)
        self.conn.commit()

    # 插入数据
    def nj_insert(self, carid):
        url = 'http://123.57.217.108:8892/index.php?r=minspection/create'
        paras = {'car_id': carid, 'content':'hello world', 'uid': 238, 'key': 'fe065d03b3bb2c8b06cdc8c3222cc69a',\
                 'clientversion': 1188}


        r = requests.post(url, data=paras)

        # json方法将数据转化为字典
        ret = r.json()
        assert ret['msg'] == u'创建成功'
        assert ret['status'] == 0

    # 关闭数据库
    def close(self):
        self.conn.close()

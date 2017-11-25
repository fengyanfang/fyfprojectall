#coding=utf8
from pymysql import connect,cursors
from pymysql.err import  OperationalError
import sys

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

    def clear(self,table_name):

        #sql语句之间应该有空格
        sql = 'truncate table'+' '+table_name+';'
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(sql)
        self.conn.commit()

    # 关闭数据库
    def close(self):
        self.conn.close()

    #创建充电单
    def cd_insert(self,carid):

        url = 'http://123.57.217.108:8892/index.php?r=charge/create'
        paras = {'car_id': carid, 'uid': 238, 'key': 'fe065d03b3bb2c8b06cdc8c3222cc69a', 'clientversion': 1188}

        r = requests.post(url, data=paras)

        # json方法将数据转化为字典
        ret = r.json()
        assert ret['msg'] == u'创建成功'
        assert ret['status'] == 0
        print ret['data']["chargeId"]



    #修改充电单
    def cd_change_record(self,status,charge_id=1,charge_point=23,amount=30,money=30,charge_company_id=5,):
        url = 'http://123.57.217.108:8892/index.php?r=charge/addoperate'
        paras = {'charge_id': charge_id, 'uid': 238, 'key': 'fe065d03b3bb2c8b06cdc8c3222cc69a',\
                 'clientversion': 1188,'content':'123','status':status,'charge_point':charge_point,\
                 'amount':amount,'money':money,'charge_company_id':charge_company_id}

        r = requests.post(url, data=paras)

        # json方法将数据转化为字典
        ret = r.json()
        print ret
        assert ret['msg'] == u'添加成功'
        assert ret['status'] == 0

    #删除充电单
    def cd_delete(self,charge_id):
        url = 'http://123.57.217.108:8892/index.php?r=charge/chargedel'
        paras = {'charge_id': charge_id, 'uid': 238, 'key': 'fe065d03b3bb2c8b06cdc8c3222cc69a', 'clientversion': 1188}

        r = requests.post(url, data=paras)

        # json方法将数据转化为字典
        ret = r.json()
        assert ret['msg'] == u'删除成功'
        assert ret['status'] == 0

   #创建调度单
    def dd_insert(self,car_id):
        url = 'http://123.57.217.108:8892/index.php?r=mdispatch/create'
        paras = {'car_id': car_id, 'uid': 238, 'start_point':'406','start_point_type':1,'content':'hello',\
                 'key': 'fe065d03b3bb2c8b06cdc8c3222cc69a', 'clientversion': 1188}

        r = requests.post(url, data=paras)

        # json方法将数据转化为字典
        ret = r.json()
        print ret
        assert ret['status'] == 0

    #修改调度单
    def dd_modify(self,dispatch_id):
        url = 'http://123.57.217.108:8892/index.php?r=mdispatch/addoperate'
        paras = {'status': 2, 'uid': 238, 'start_point': '406', 'start_point_type': 1, 'content': 'hello', \
                 'dispatch_id':dispatch_id,'key': 'fe065d03b3bb2c8b06cdc8c3222cc69a', 'clientversion': 1188,\
                 'end_point':8,'end_point_type':1}
        r = requests.post(url, data=paras)
        ret = r.json()
        assert ret['status'] == 0

    #删除调度单
    def dd_delete(self,dispatch_id):
        url = 'http://123.57.217.108:8892/index.php?r=mdispatch/chargedel'
        paras = { 'uid': 238,'dispatch_id': dispatch_id, 'key': 'fe065d03b3bb2c8b06cdc8c3222cc69a', \
                  'clientversion': 1188}

        r = requests.post(url, data=paras)
        ret = r.json()
        assert ret['status'] == 0



if __name__  == '__main__':
    dd=DataBase('manager')
    dd.dd_modify(1)
    dd.dd_delete(2)









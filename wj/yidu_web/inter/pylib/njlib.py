#coding=utf-8
import json,requests

class njlib():


    cd_url = 'http://123.57.217.108:8892/index.php?r=minspection/'

    def real_url(self,path):
        return self.cd_url + path


    def nj_create(self):
        paras = {'car_id': 2, 'content':'hello world','uid': 238, 'key': 'fe065d03b3bb2c8b06cdc8c3222cc69a', 'clientversion': 1188}

        r = requests.post(self.real_url('create'), data=paras)

        #将json字符串转化成字典
        ret = r.json()
        return ret





    def nj_list(self):
        data = {'start': 0, 'offset': '10', 'uid': 238, 'key': 'fe065d03b3bb2c8b06cdc8c3222cc69a', \
                'clientversion': 1188, 'status': '1,2,3', 'sort': 0, 'cityId': 1}

        r = requests.post(self.real_url('inspectionalllist'), data=data)
        print r.headers
        ret = r.text

        ret = r.json()


        return ret

if __name__  == '__main__':
    nj = njlib()
    nj.nj_list()




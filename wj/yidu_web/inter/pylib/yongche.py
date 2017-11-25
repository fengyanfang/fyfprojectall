#coding=utf-8
import json,requests

class yongche():


    yc_url = 'https://test_new.yiduyongche.com'
    def real_url(self,path):
        return self.yc_url + path


    def list_coupon(self):
        paras = {'clientversion':'ios_2910', 'systemversion':'10.3.3','uid': 1192, 'type':'coupon','status':1}
        r = requests.post(self.real_url('/customer/info.html'), data=paras,verify=False)

        #将json字符串转化成字典
        ret = r.json()
        print ret
        return ret


if __name__  == '__main__':
    yc = yongche()
    yc.list_coupon()


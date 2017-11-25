#coding=utf8
from appium import webdriver
import time, traceback


class AppOp():                                   #找不到这个模块看下面有没有init这个文件@@@
    ROBOT_LIBRARY_SCOPE = 'GLOBLE'
    dr = None

    def OpenSession(self):
        desired_caps = {}

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'test'
       # desired_caps['app'] = r'c:/fyf/yidutool2-v1.1.87-fir_im-release.apk_1.1.87.apk'
        desired_caps['appPackage'] = 'com.yidu.yidutool2'
        desired_caps['appActivity'] = 'com.yidu.yidutool.activity.LoginActivity'
        desired_caps['unicodeKeyboard'] = True      #一定要有否则输入的unicode命令无效
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        desired_caps['newCommandTimeout'] = 60
        # 启动Remote RPC
        if AppOp.dr:
            return

        AppOp.dr= webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        AppOp.dr.implicitly_wait(10)


    def CloseSession(self):
        AppOp.dr.quit()


    def LoginApp(self,username,passwd):

        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/et_phone_number').send_keys(username)
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_get_code').click()
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/et_input_code').send_keys(passwd)
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_start_use').click()
        time.sleep(1)


    def Logout(self):
        AppOp.dr.implicitly_wait(5)
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/ib_title_bar_left').click()
        AppOp.dr.implicitly_wait(2)

        code = u'new UiSelector().text("退出登陆")'
        AppOp.dr.find_element_by_android_uiautomator(code).click()


        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/btn_right').click()


    def SelectVin(self,vin):
        #点击车辆查询
        code = u'new UiSelector().text("车辆查询")'
        ele = AppOp.dr.find_element_by_android_uiautomator(code)
        ele.click()
        time.sleep(2)

        #输入vin,点击查询
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/et_car_vin').send_keys(vin)
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/btn_search').click()
        time.sleep(2)

    def GetVin(self):

        #查询到的车的vin
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_cardetails_carVin')
        VinText = ele.text[-6:]

        return VinText


    def SelectChePai(self,carnum):
        try:
            ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/et_car_num')
            ele.click()
            ele.send_keys(carnum)
            #点击查询
            AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/btn_search').click()
            time.sleep(2)
        except:
            raise Exception(u'查询车牌出错啦')


    def GetCarNum(self):

        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_cardetails_carID')
        carnum = ele.text
        return carnum


    def WdSelect(self,wd_name):
        #判断右上角按钮是地图还是列表

        code = u'new UiSelector().text("地图")'
        map = AppOp.dr.find_elements_by_android_uiautomator(code)
        if map:
            map[0].click()
        #点击网点button
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/ib_title_bar_right').click()

        #点击网点，输入网点查询
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/ll_search_yidu_wd')
        ele.click()

        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/et_title_bar_title')
        ele.send_keys(wd_name)
        time.sleep(1)


        #点击网点名称
        xpath = u'//android.widget.ListView/android.widget.RelativeLayout[1]'
        AppOp.dr.find_element_by_xpath(xpath).click()
        time.sleep(2)



    def GetWdText(self):
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_networkdotcarList_ParkinglotAddress')
        wdtext = ele.text
        print wdtext

        return  wdtext

    #充电单查询,进入充电单查询页面
    def CdSelect(self):
        time.sleep(2)
        code = u'new UiSelector().text("地图")'
        map_button = AppOp.dr.find_elements_by_android_uiautomator(code)
        if map_button:
            time.sleep(1)

            ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_all_charging')
            ele.click()

        else:
            code = u'new UiSelector().text("列表")'
            AppOp.dr.find_element_by_android_uiautomator(code).click()
            time.sleep(1)

            ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_all_charging')
            ele.click()


    def CdSelectVin(self,vin):
        time.sleep(2)
        #点击vin输入框，输入vin
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_charginglist_title')
        ele.click()

        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/et_car_vin')
        ele.click()
        ele.send_keys(vin)

        #点击查询
        code =  u'new UiSelector().text("查询")'
        AppOp.dr.find_element_by_android_uiautomator(code).click()

    def CdGetVin(self):

        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_adapterChargingList_carNum')
        print ele.text[-6:]

        return ele.text[-6:]

    def CdChePaiSelect(self,chepai):
        time.sleep(1)
        #点击工单查询输入框
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_charginglist_title').click()
        #输入车牌
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/et_car_num')
        ele.click()
        ele.send_keys(chepai)

        #点击查询
        code = u'new UiSelector().text("查询")'
        AppOp.dr.find_element_by_android_uiautomator(code).click()


    def CdGetChePai(self):
        time.sleep(1)
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_adapterChargingList_carNum')
        print ele.text[:7]

        return ele.text[:7]

    def CdNumSelect(self,cdnum):
        time.sleep(1)
        # 点击工单查询输入框
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_charginglist_title').click()
        # 输入工单
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/et_fault_num')
        ele.click()
        ele.send_keys(cdnum)

        # 点击查询
        code = u'new UiSelector().text("查询")'
        AppOp.dr.find_element_by_android_uiautomator(code).click()

    def CdGetNum(self):
        time.sleep(1)
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_adapterChargingList_num')
        print ele.text[-6:]

        return ele.text[-6:]

    #返回一次
    def ComeMain1(self):
        AppOp.dr.press_keycode(4)

    #返回两次
    def ComeMain2(self):
        for i in range(2):
            AppOp.dr.press_keycode(4)
            time.sleep(1)

    def ComeMain3(self):
        for i in range(3):
            AppOp.dr.press_keycode(4)
            time.sleep(1)

    def ComeMain4(self):
        for i in range(4):
            AppOp.dr.press_keycode(4)
            time.sleep(1)

   #删除充电单列表
    def DeleteCdList(self):
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/swipe_target')
        eles = ele.find_elements_by_class_name('android.widget.LinearLayout')
        while True:
            if eles==[]:
                break

            #通过找到 操作者 用户的元素，再通过坐标去找到删除按钮
            ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_adapterChargingList_worker')
            locat = ele.location
            del_x = locat['x']
            del_y = locat['y']
            AppOp.dr.tap([(del_x,del_y),],2000)
            #点击删除按钮
            AppOp.dr.tap([(del_x,del_y-255),],500)

            #删除后点击确定
            ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/btn_faultlistDialog_ok')
            ele.click()

    #创建充电单,进入车辆列表
    def CdCdCarTable(self):
        code = u'new UiSelector().text("地图")'
        map_button = AppOp.dr.find_elements_by_android_uiautomator(code)
        if map_button:
            time.sleep(1)

            ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_all_car')
            ele.click()

        else:
            code = u'new UiSelector().text("列表")'
            AppOp.dr.find_element_by_android_uiautomator(code).click()
            time.sleep(1)

            ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_all_car')
            ele.click()
    #创建充电单
    def CreateCd(self):

        #选择第2个车辆创建充电单
        code=u'//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]'
        ele = AppOp.dr.find_element_by_xpath(code)
        ele.click()
        #点击查看与新建工单
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/btn_cardetails_lookAndcreateOrder')
        ele.click()

        #点击充电工单
        ele=AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/btn_lookAndCreate_chargeWorkOrder')
        ele.click()

        #创建充电单
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/btn_charginglist__right')
        ele.click()

        # #选择充电状态，点击提交
        # ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/rb_buildCharging_changeToCharging')
        # if ele:
        #     ele.click()
        #     time.sleep(1)
        #点击提交
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/btn_buildCharging_ok').click()

        #点击弹框确定
        AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/btn_faultlistDialog_ok').click()

    def VerifyCdCreated(self):
        ele = AppOp.dr.find_element_by_id('com.yidu.yidutool2:id/tv_chargingDetails_orderState')
        if ele:
            return  True
        else:
            return  False






if __name__ == "__main__":
    op = AppOp()
    op.OpenSession()
    op.LoginApp("15833098119","1233")

    # op.SelectVin('114937')
    # op.GetVin()
    # op.WdSelect(u'878')
    # op.GetWdText()
    # op.ComeMain3()
    op.CdSelect()
    # op.CdSelectVin('112190')
    # op.CdGetVin()
    # op.CdNumSelect('100423')
    # op.CdGetNum()
    op.DeleteCdList()
    op.Logout()








# coding=utf8

from appium import webdriver
import traceback
from time import sleep

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'C:\classes\ap\HISpace.apk'
desired_caps['appPackage'] = 'com.huawei.appmarket'
desired_caps['appActivity'] = 'com.huawei.appmarket.MainActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 60
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)
    ele2 = u'new UiSelector().resourceId("com.huawei.appmarket:id/tabLayout").' \
           u'childSelector(new UiSelector().text("排行"))'

    driver.find_element_by_android_uiautomator(ele2).click()

    code = u'new UiSelector().text("总榜")'   #有汉字加上u
    zongbang = driver.find_element_by_android_uiautomator(code)
    zb_y = zongbang.location['y']

    driver.implicitly_wait(1)
    code = u'new UiSelector().text("口碑最佳")'
    while True:
        zuijia = driver.find_elements_by_android_uiautomator(code)  # 列表不会报错
        driver.swipe(400,zb_y+80,400,zb_y,1000)

        # 如果没有找到最佳就跳出本次循环，如果找到，就执行下面的代码
        if not zuijia:
            continue

        ele = zuijia[0]
        y1 = ele.location['y']    #location方法是个字典
        driver.swipe(400,y1,400,zb_y,3000)
        sleep(0.5)
        #如果找到就跳出整个循环
        break
    driver.implicitly_wait(10)

    code = u'new UiSelector().className("android.widget.TextView")'
    eles = driver.find_elements_by_android_uiautomator(code)
    str_list = []
    for ele in eles:
        print ele.text
        str_list.append(ele.text)

    str_f = '|||'.join(str_list)
    pos1 = str_f.find(u'口碑最佳')
    str_tar = str_f[pos1:]
    def getname(no):
        tp1 = str_tar.find(no+'|||')

        # 从tp1+4后面再找到‘|||’
        tp2 = str_tar.find('|||',tp1+4)

        return str_tar[tp1+4:tp2]  #:不要写成，

    print "========result==========="
    print getname('1')  #拼接的都是字符串
    print getname('2')
    print getname('3')









except:
    print traceback.format_exc()

driver.quit()






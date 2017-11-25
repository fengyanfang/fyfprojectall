# coding=utf8

from appium import webdriver
import time,traceback

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'C:\classes\ap\com.ibox.apk'
desired_caps['appPackage'] = 'com.yidu.yidutool2'
desired_caps['appActivity'] = 'com.yidu.yidutool.activity.LoginActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 60
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)

    # 根据id找到元素，并点击，id和 html 元素的id不同
    num3 = driver.find_element_by_id("com.ibox.calculators:id/digit3")
    num9 = driver.find_element_by_id("com.ibox.calculators:id/digit9")
    equ1 = driver.find_element_by_id("com.ibox.calculators:id/equal")
    jia = driver.find_element_by_id("com.ibox.calculators:id/plus")

    cheng = driver.find_element_by_id('com.ibox.calculators:id/mul')
    num5 = driver.find_element_by_id("com.ibox.calculators:id/digit5")

    num3.click()
    jia.click()
    num9.click()
    equ1.click()

    cheng.click()
    num5.click()
    equ1.click()
   #xpath定位
    code = '//*[@resource-id="com.ibox.calculators:id/cv"]/android.widget.TextView[2]'
    ret = driver.find_element_by_xpath(code)
    print ret.text
    if ret.text == '60':
        pass
    else:
        print "fail"


except:
    print traceback.format_exc()


raw_input('**** Press to quit..')

driver.quit()
# coding=utf8

from appium import webdriver
import traceback
from time import sleep

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'C:\fyf\ruanjian\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 600
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)

    code = '//*[@resourseId="io.manong.developerdaily:id/home_feature_recycler_view"]/' \
           'android.widget.LinearLayout[1]//android.widget.TextView'
    ele = driver.find_element_by_xpath(code)
    str1 = ele.text

    ele.click()

    ele2 = driver.find_element_by_id('io.manong.developerdaily:id/tv_title')
    str2 = ele2.text

    driver.press_keycode(4)
    if str1 == str2:
        print 'pass'
    else:
        print "fail"

except:
    print traceback.format_exc()

driver.quit()
#coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import traceback

dr = webdriver.Chrome()
dr.implicitly_wait(10)


try:
    #首页
    dr.get("https://www.vmall.com")

    #点击华为官网
    dr.find_element_by_css_selector('.s-hw>a').click()

    #切换到应用市场，使用鼠标悬停
    ac = ActionChains(dr)
    ac.move_to_element(dr.find_element_by_css_selector('.s-appsoft')).perform()
    dr.find_element_by_css_selector('.s-appsoft div.b a[href*=appstore]').click()

    def checkappstore():
        expects = u'''首页
游戏
软件
专题
品牌专区
华为软件专区'''



        eles = dr.find_elements_by_css_selector('.ul-nav>li')
        eletext = [ele.text for ele in eles]
        print 'checkappstore ...'

        if '\n'.join(eletext) == expects:
            print "ok"
        else:
            print 'fail'




    def checkhuawei():
        pass


    #窗口切换
    for handle in dr.window_handles:
        dr.switch_to.window(handle)
        if u'应用市场' in dr.title:
            checkappstore()

        elif u'华为智能手机' in dr.title:
            checkhuawei()



except:
    print "exception:" + traceback.format_exc()

finally:dr.quit()



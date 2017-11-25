#coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import traceback

dr = webdriver.Chrome()
dr.implicitly_wait(10)


def getinfo():
    try:
        dr.get("https://kyfw.12306.cn/otn/index/init")
        dr.find_element_by_link_text('车票预订').click()

        #点击出发地输入框,点击一下，才反应
        fromp = dr.find_element_by_id('fromStationText')
        fromp.click()
        fromp.clear()
        fromp.send_keys(u"北京西\n")


        #选择目的地
        ele = dr.find_element_by_id("toStationText")
        ele.click()
        ele.clear()
        ele.send_keys(u'邢台东\n')




        #选择时间端段
        Select(dr.find_element_by_id("cc_start_time"))\
            .select_by_visible_text('00:00--24:00')


        #选择出发时间,当前时间的第二天
        dr.find_element_by_css_selector('#date_range ul li:nth-of-type(14)').click()



        #选择二等座的区域
        eles= dr.find_elements_by_xpath('//*["@id=queryLeftTable"]/tr["@class"]/td[4]/../td[1]//a')
        for ele in eles:
            print ele.text



    except:
        print "exception:" + traceback.format_exc() #打印具体错误信息
    finally:dr.quit()



getinfo()
dr.quit()
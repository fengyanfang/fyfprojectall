#coding=utf8
from selenium import webdriver
import time
#显示等待
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.by import  By

dr = webdriver.Chrome()
dr.get("http://www.weather.com.cn/html/province/jiangsu.shtml")
dr.implicitly_wait(10) #全局变量,

#显示等待，是等待一个元素
ele = WebDriverWait(dr,10).until(ES.presence_of_element_located((By.ID,"forecastID")))
dls = ele.find_elements_by_tag_name("dl")
time.sleep(2)

lowerst = 100
citys = []

for dl in dls:
    city = dl.find_element_by_css_selector("dt").text
    lowweather =  dl.find_element_by_tag_name("b").text
    lowweather = int(lowweather.replace(u"℃",""))
    if lowweather < lowerst:
        lowerst = lowweather

        citys=[city]
    elif lowweather == lowerst:
        citys.append(city)

print u"温度最低为%s,城市有%s" %(lowerst," ".join(citys))
dr.quit()


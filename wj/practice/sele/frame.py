#coding=utf8
from selenium import webdriver
import time


dr = webdriver.Chrome()
#切换到iframe里面,可以是name也可以是id，也可以直接用索引，
dr.switch_to.frame(0)

#可以直接通过查找iframe各种属性定位到iframe
dr.switch_to.frame(dr.find_element_by_tag_name("iframe"))

#切换到主html里面
dr.switch_to.default_content()
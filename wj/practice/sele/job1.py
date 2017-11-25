#coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

dr = webdriver.Chrome()
dr.implicitly_wait(10)

def getinfo():
    dr.get("http://www.51job.com")
    dr.find_element_by_id("kwdselectid").send_keys("python")
    dr.find_element_by_css_selector('#work_position_input').click()

    dr.find_element_by_id('work_position_click_center_left_each_220200').click()
    citylist = dr.find_elements_by_css_selector('#work_position_click_center_right_list_220200 em')

    for one in citylist:

        cityName = one.text
        selected = one.get_attribute('class')
        print cityName
        if cityName == u'杭州':
            if selected != 'on':
                one.click()
        else:
            if selected == 'on':
                one.click()

    #之前是缩进错误，应该跳出循环
    dr.find_element_by_css_selector("#work_position_click_bottom_save").click()
    sleep(3)
    dr.find_element_by_css_selector('''button[onclick="kwdGoSearch($('#kwdselectid').val());"]''').click()

    joblist = dr.find_elements_by_css_selector("#resultList div[class=el]")
    for job in joblist:
        fields = job.find_elements_by_tag_name("span")
        str_field = [fileld.text  for fileld in fields]
        print '|'.join(str_field)



getinfo()
dr.quit()
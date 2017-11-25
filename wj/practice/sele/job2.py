#coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

dr = webdriver.Chrome()
dr.implicitly_wait(10)

def getinfo():
    dr.get("http://www.51job.com")
    dr.find_element_by_css_selector('a.more').click()
    dr.find_element_by_css_selector("#work_position_input").click()

    # dr.find_element_by_id('kwdselectid').send_keys('python')

    dr.find_element_by_id('work_position_click_center_left_each_220200').click()
    citylist = dr.find_elements_by_css_selector('#work_position_click_center_right_list_220200 em')

    for one in citylist:

        cityName = one.text
        selected = one.get_attribute('class')
        if cityName == u'杭州':
            if selected != 'on':
                one.click()
        else:
            if selected == 'on':
                one.click()

    #选择职业类别
    dr.find_element_by_css_selector("#work_position_click_bottom_save").click()
    dr.find_element_by_css_selector("#funtype_click").click()
    dr.find_element_by_css_selector("#funtype_click_center_right_list_category_0100_0100").click()
    dr.find_element_by_css_selector('#funtype_click_center_right_list_sub_category_each_0100_0106').click()
    dr.find_element_by_css_selector('#funtype_click_bottom_save').click()

    #选择公司性质

    dr.find_element_by_css_selector("#indtype_click").click()
    dr.find_element_by_css_selector("#indtype_click_center_right_list_category_01_01").click()
    dr.find_element_by_css_selector("#indtype_click_bottom_save").click()

    #选择行业类别
    dr.find_element_by_css_selector("div#cottype_list span").click()
    dr.find_element_by_css_selector("div#cottype_list div.ul span[data-value='01']").click()

    #选择工作年限
    dr.find_element_by_css_selector("#workyear_list span").click()
    dr.find_element_by_css_selector('#workyear_list div.ul span[data-value="02"]').click()

    #选择月薪
    # dr.find_element_by_css_selector('#providesalary_list span').click()
    # dr.find_element_by_css_selector('#providesalary_list div.ul span[data-value="08"]').click()

    #选择公司规模
    # dr.find_element_by_css_selector('#companysize_list span').click()
    # dr.find_element_by_css_selector('#companysize_list div.ul span[data-value="04"]').click()

    #选择学历要求
    # dr.find_element_by_css_selector('#degreefrom_list>span').click()
    # dr.find_element_by_css_selector('#degreefrom_list div.ul span[data-value="04"]').click()

    #选择工作类型
    # dr.find_element_by_css_selector('#jobterm_list span').click()
    # dr.find_element_by_css_selector('#jobterm_list div.ul span[data-value="01"]').click()   #没有click程序就不走啦

    dr.find_element_by_id('kwdselectid').send_keys('python')

    dr.find_element_by_css_selector('''span[onclick="kwdGoSearch($('#kwdselectid').val());"]''').click()

    #获取工作信息
    #之前是缩进错误，应该跳出循环

    joblist = dr.find_elements_by_css_selector("#resultList div[class=el]")
    for job in joblist:
        fields = job.find_elements_by_tag_name("span")
        str_field = [fileld.text  for fileld in fields]
        print '|'.join(str_field)

getinfo()
dr.quit()






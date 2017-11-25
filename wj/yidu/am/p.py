import time
from sele import webdriver


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://123.57.217.108:8889/index.php?r=login/index")

driver.find_element_by_css_selector("#username").send_keys("13411111111")
time.sleep(2)
driver.find_element_by_css_selector("#password").send_keys("YIDUyc123456")
time.sleep(2)
code1=raw_input("please input a code")
driver.find_element_by_name('verifyCode').send_keys(code1)
time.sleep(2)
driver.find_element_by_id('sub').click()
time.sleep(2)
driver.find_element_by_css_selector("dl>dt>i.Hui-iconfont").click()
time.sleep(3)
driver.find_element_by_css_selector("dd>ul>li>a").click()
time.sleep(10)
driver.find_element_by_css_selector("table[class='table table-border table-bordered table-bg']  tr:nth-of-type(2) td:nth-of-type(1)]").send_keys("13411111111")

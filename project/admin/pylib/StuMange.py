#coding=utf8
from selenium import webdriver
import sys,time
sys.path.append(r'D:\wj\project\admin')  #加r避免出错
import cfg


class StuMange():
    ROBOT_LIBRARY_SCOPE = 'GLOBLE'
    dr = None

    def OpenBrowser(self,driverType):
        if StuMange.dr:
            return
        elif driverType == 'chrome':
            StuMange.dr = webdriver.Chrome()

        elif driverType == 'firefox':
            StuMange.dr =webdriver.Firefox()

        else:
            raise Exception("unknown type of driverType")

        StuMange.dr.implicitly_wait(10)

    def CloseBrowser(self):
        StuMange.dr.quit()

    def WebLogin(self,name,passwd):
        StuMange.dr.get(cfg.uskid_login_url)
        ele = StuMange.dr.find_element_by_css_selector('input[type="text"]')
        ele.clear()
        ele.send_keys(name)

        ele = StuMange.dr.find_element_by_css_selector('input[type="password"]')
        ele.clear()
        ele.send_keys(passwd)

        ele = StuMange.dr.find_element_by_css_selector('button[type="button"]')
        ele.click()

        StuMange.dr.find_element_by_css_selector('.change-locale').click()

        StuMange.dr.maximize_window()

        time.sleep(1)

    def










if __name__ == "__main__":
    dr = StuMange()
    dr.OpenBrowser('chrome')
    dr.WebLogin('18800000001',"111111")
    dr.CloseBrowser()




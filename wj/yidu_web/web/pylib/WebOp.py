#coding=utf8
from selenium import  webdriver
import time,sys
from selenium.webdriver.support.ui  import Select
sys.path.append('C:/classes/yidu_web/web')
import unittest
import conf

#找不到测试用例是编码不对，该是utf8@@@@


class WebOp():
    ROBOT_LIBRARY_SCOPE= 'GLOBLE'
    dr = None

    def OpenBrowser(self,driverType):
        if WebOp.dr:
            return
        elif driverType == 'chrome':
            WebOp.dr = webdriver.Chrome()

        elif driverType == 'firefox':
            WebOp.dr = webdriver.Firefox()

        else:
            raise Exception('unknown type of webdriver')

        WebOp.dr.implicitly_wait(10)

    def CloseBrowser(self):
        WebOp.dr.quit()

    def LoginWebSite(self,username,passwd):
        WebOp.dr.get(conf.LoginUrl)
        WebOp.dr.find_element_by_css_selector('#username').send_keys(username)
        WebOp.dr.find_element_by_css_selector('#password').send_keys(passwd)

        WebOp.dr.find_element_by_css_selector('#code').click()
        time.sleep(8)

        WebOp.dr.find_element_by_css_selector('#sub').click()
        WebOp.dr.maximize_window()
        time.sleep(1)

        #滑动页面，使充电单可见
        js = 'window.scrollTo(100,500);'
        WebOp.dr.execute_script(js)
        time.sleep(1)

    #进入充电单列表
    def ToCdMenu(self):
        ele = WebOp.dr.find_elements_by_css_selector('dl:nth-of-type(24) dt')
        if ele:
            ele[0].click()
        WebOp.dr.find_element_by_css_selector(u'a[data-title="充电单列表"]').click()

        time.sleep(1)

        # 进入内嵌的充电单页面@@@@
        WebOp.dr.switch_to.frame(WebOp.dr.find_element_by_xpath('//div[@id="iframe_box"]/div[2]/iframe'))
        time.sleep(2)

    # 进入调度单列表
    def ToDdMenu(self):
        ele = WebOp.dr.find_element_by_css_selector('dl:nth-of-type(24) dt')

        eles = WebOp.dr.find_elements_by_css_selector(u'a[data-title="调度单列表"]')
        if eles:
            eles[0].click()
        else:
            ele.click()
            eles[0].click()


        time.sleep(1)

        #进入内嵌的故调度单页面
        WebOp.dr.switch_to.frame(WebOp.dr.find_element_by_xpath('//div[@id="iframe_box"]/div[2]/iframe'))
        time.sleep(1)

    def  DdNumberSelect(self,num):
        ele = WebOp.dr.find_element_by_css_selector('#number')
        ele.send_keys(num)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    def GetDdNumber(self,num):
        code='table[class="table table-border table-bordered table-bg table-hover"] tr td:nth-of-type(1)'
        eles = WebOp.dr.find_elements_by_css_selector(code)


        if eles:
            Numtext = [ele.text for ele in eles]
            for one in Numtext:
                if one[2:] == num:
                    return  True
                else:
                    return  False
        else:
            return  None


    def DdCarCompanySelect(self,company):
        ele = WebOp.dr.find_element_by_css_selector('#carcompany ')
        ele.click()
        #选择公司
        Select(ele).select_by_visible_text(company)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    def GetDdCarCompany(self,company):
        code='table[class="table table-border table-bordered table-bg table-hover"] tr td:nth-of-type(3)'
        eles =  WebOp.dr.find_elements_by_css_selector(code)

        if eles:
            for ele in eles:
                if ele.text == company:
                    continue
                else:
                    return  False
        else:
            return None
        return  True

   #查询vin号
    def  DdVinSelect(self,vin):
        ele = WebOp.dr.find_element_by_css_selector('#vin')
        ele.send_keys(vin)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    def  GetDdVin(self):
        eles = WebOp.dr.find_elements_by_css_selector('a[data-title="调度单详情"]')
        if eles:
            for ele in eles:
                ele.click()

                #返回到主页面
                WebOp.dr.switch_to.default_content()
                #进入到充电详情页面
                WebOp.dr.switch_to.frame(WebOp.dr.find_element_by_xpath('//div[@id="iframe_box"]/div[3]/iframe'))

                #获取vin号
                code = '//*[@class="follow"]//..//tr[4]/td[2]'
                ele = WebOp.dr.find_element_by_xpath(code)

                time.sleep(1)
                return ele.text[-6:]
        else:
            return None

    def  DdChepaiSelect(self,chepai):
        ele = WebOp.dr.find_element_by_css_selector('#license')
        ele.send_keys(chepai)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    def GetDdChepai(self,chepai):
        code = 'table[class="table table-border table-bordered table-bg table-hover"] tr td:nth-of-type(2)'
        eles = WebOp.dr.find_elements_by_css_selector(code)

        if eles:
            for ele in eles:
                if ele.text == chepai:
                    return  True
                else:
                    return  False
        else:
            return  None

    def DdStatusSelect(self,status):
        ele = WebOp.dr.find_element_by_css_selector('#liststatus')
        ele.click()

        Select(ele).select_by_visible_text(status)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    def GetDdStatus(self,status):
        code = 'table[class="table table-border table-bordered table-bg table-hover"] tr td:nth-of-type(7)'
        eles = WebOp.dr.find_elements_by_css_selector(code)

        if eles:
            for ele in eles:
                if ele.text == status:
                    continue
                else:
                    return  False
        else:
            return None
        return  True


    def DdFollowerSelect(self,follower):
        ele = WebOp.dr.find_element_by_css_selector('#person')
        ele.send_keys(follower)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    def GetDdFollower(self,follower):

        i = 0
        while True:

            time.sleep(1)
            # 点击调度单详情
            eles1 = WebOp.dr.find_elements_by_css_selector('a[data-title="调度单详情"]')
            if eles1:
                eles1[i].click()
                time.sleep(1)
                i += 1
                WebOp.ComeMainToXq(self)

                # 获取vin,通过子元素的唯一性实现父元素定位，再定位父元素的子元素
                eles = WebOp.dr.find_elements_by_xpath("//*[@class='follow']//tr/td[1]")
                follower_list = [ele.text for ele in eles]

                WebOp.CloseXiangQing(self)

                if follower not in follower_list:
                    return False
                # 回到主页面@@@@，循环不了是因为，没有重新进入充电页面,进入内嵌的充电单页面@@@@
                WebOp.ComeMainToGd(self)

                if i >= len(eles1):
                    break
            else:
                return None

        return True

    def DdCreatetimeSelect(self,startmin,startmax):
        time.sleep(1)
        ele = WebOp.dr.find_element_by_css_selector('#startmin')
        ele.send_keys(startmin)

        ele = WebOp.dr.find_element_by_css_selector('#startmax')
        ele.send_keys(startmax)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()
        time.sleep(2)

    def GetDdCreatetime(self,startmin,startmax):
        i=0
        startmax = time.mktime(time.strptime(startmax,'%Y-%m-%d %H:%M:%S'))
        startmin = time.mktime(time.strptime(startmin, '%Y-%m-%d %H:%M:%S'))
        while True:
            time.sleep(1)
            eles1 = WebOp.dr.find_elements_by_css_selector(u'a[data-title="调度单详情"]')

            if eles1:
                eles1[i].click()
                i +=1
                self.ComeMainToXq()

                code = '//*[@class="follow"]//tr[last()]/td[2]'
                ele = WebOp.dr.find_elements_by_xpath(code)

                createtime = ele[0].text
                self.CloseXiangQing()

                createtime = time.mktime(time.strptime(createtime,u'%Y年%m月%d日 %H:%M:%S'))
                if not (float(createtime)>= (float(startmin)) and  (float(createtime))<= (float(startmax))):
                    return False


                self.ComeMainToGd()
                if i >=len(eles1):
                    break

            else:
                return None

        return True  #跳出循环，不然遇到return程序会终止

    def DdFinishedtimeSelect(self,endmin,endmax):
        time.sleep(1)
        ele = WebOp.dr.find_element_by_css_selector('#endmin')
        ele.send_keys(endmin)

        ele = WebOp.dr.find_element_by_css_selector('#endmax')
        ele.send_keys(endmax)
        # 任意点击去掉时间框
        WebOp.dr.find_element_by_id('license').click()

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()
        time.sleep(2)

    def GetDdFinishedtime(self,endmin,endmax):
        i = 0
        endmin = time.mktime(time.strptime(endmin,'%Y-%m-%d %H:%M:%S'))
        endmax = time.mktime(time.strptime(endmax,'%Y-%m-%d %H:%M:%S'))
        while True:
            time.sleep(1)
            eles1 = WebOp.dr.find_elements_by_css_selector(u'a[data-title="调度单详情"]')

            if eles1:
                eles1[i].click()
                i +=1
                self.ComeMainToXq()

                code = '.follow tr:nth-of-type(2)  td:nth-of-type(2)'
                eles = WebOp.dr.find_elements_by_css_selector(code)

                finishedtime = eles[0].text
                self.CloseXiangQing()

                finishedtime = time.mktime(time.strptime(finishedtime,u'%Y年%m月%d日 %H:%M:%S'))
                if not (float(finishedtime)>= (float(endmin)) and  (float(finishedtime))<= (float(endmax))):
                    return False


                self.ComeMainToGd()
                if i >=len(eles1):
                    break

            else:
                return None

        return True  #跳出循环，不然遇到return程序会终止

    def DdDelstatusSelect(self,status):
        ele = WebOp.dr.find_element_by_css_selector('#delstatus')
        Select(ele).select_by_visible_text(status)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()
        time.sleep(1)

    def GetDdDelstatus(self,status):
        code='//*[@class="table table-border table-bordered table-bg table-hover"]//tr/td[6]'
        eles = WebOp.dr.find_elements_by_xpath(code)

        if eles:
                for ele in eles:
                    if status == u'全部':
                        if ele.text ==u'否' or u'已删除':
                            continue

                    elif ele.text == status:
                        continue
                    else:
                        return False

        return  True

    def Comemain(self):
        WebOp.dr.switch_to.default_content()
    def CloseGd(self):
        WebOp.dr.find_element_by_css_selector('.active i').click()
        time.sleep(2)









    #充电单编号查询
    def CdNumSelect(self,cdnum):

        WebOp.dr.find_element_by_css_selector('input#number').send_keys(cdnum)

        #点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()


    def GetCdNum(self,cdnum):

        #找到充电单编号的元素
        code='table[class="table table-border table-bordered table-bg table-hover"] tr:nth-of-type(1)>td:nth-of-type(1)'
        eles = self.dr.find_elements_by_css_selector(code)
        if eles:
            NumText = [ele.text for ele in eles]
            for one in NumText:
                if one[2:] == cdnum:
                    return True
                else:
                    return  False
        else:
            return  None

    def ClearCdNum(self):
        WebOp.dr.find_element_by_css_selector('input#number').clear()



    #查询vin
    def CdVinSelect(self,vin):

        #找到vin元素
        ele = WebOp.dr.find_element_by_css_selector('#vin')
        ele.click()
        ele.send_keys(vin)

        #点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    def GetCdVin(self):

        #点击充电单详情
        eles = WebOp.dr.find_elements_by_css_selector('a[data-title="充电单详情"]')
        if eles:
            for ele in eles:
                ele.click()
        else:
            WebOp.dr.find_element_by_css_selector('#vin').clear()
            return  None



        time.sleep(1)

        #回到主页面@@@@
        WebOp.dr.switch_to.default_content()

        #进入详情的内嵌页面
        WebOp.dr.switch_to.frame(WebOp.dr.find_element_by_xpath('//div[@id="iframe_box"]/div[3]/iframe'))
        time.sleep(1)

        #获取vin,通过子元素的唯一性实现父元素定位，再定位父元素的子元素
        ele = WebOp.dr.find_element_by_xpath('//*[@class="follow"]/..//tr[3]//td[2]/span')

        return ele.text[-6:]

    def CloseXiangQing(self):
        time.sleep(1)
        WebOp.dr.switch_to.default_content()

        # 关闭充电单详情,充电单详情页面在主页面里头
        WebOp.dr.find_element_by_xpath('//*[@id="min_title_list"]/li[3]/i').click()

    def ClearVin(self):
        #进入工单页面删除筛选条件
        WebOp.dr.switch_to.frame(WebOp.dr.find_element_by_xpath('//div[@id="iframe_box"]/div[2]/iframe'))
        WebOp.dr.find_element_by_css_selector('#vin').clear()



    #查询车牌
    def CdChePaiSelect(self,chepai):

        #输入车牌
        ele = WebOp.dr.find_element_by_css_selector('input#license')
        ele.click()
        ele.send_keys(chepai)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    def GetCdChepai(self):
        # 点击充电单详情
        eles = WebOp.dr.find_elements_by_css_selector('a[data-title="充电单详情"]')
        if eles:
            eles[0].click()
            time.sleep(1)
        else:
            WebOp.dr.find_element_by_css_selector('input#license').clear()
            return  None

        # 回到主页面@@@@
        WebOp.dr.switch_to.default_content()

        # 进入详情的内嵌页面
        WebOp.dr.switch_to.frame(WebOp.dr.find_element_by_xpath('//div[@id="iframe_box"]/div[3]/iframe'))
        time.sleep(1)

        # 获取vin,通过子元素的唯一性实现父元素定位，再定位父元素的子元素
        ele = WebOp.dr.find_element_by_xpath('//*[@class="follow"]/..//tr[2]//td[2]/span')

        return ele.text

    def ClearCdChePai(self):
        # 充电单页面
        WebOp.dr.switch_to.frame(WebOp.dr.find_element_by_xpath('//div[@id="iframe_box"]/div[2]/iframe'))
        WebOp.dr.find_element_by_css_selector('input#license').clear()


    #充电单的车的公司查询
    def CdCarCompanySelect(self,company):
        ele = WebOp.dr.find_element_by_css_selector('#carcompany')
        ele.click()
        #选择公司
        Select(ele).select_by_visible_text(company)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    #获取充电单的公司查询数据
    def GetCdCarCompany(self,company):
        code = u"//*[@class='table table-border table-bordered table-bg table-hover']//tbody/tr/td[3]"
        eles = WebOp.dr.find_elements_by_xpath(code)
        if eles:
            for ele in eles:
                if ele.text == company:
                    continue
                else:
                    return  False
        else:
            return  None

        return  True

    #重置点击
    def Reset(self):
        WebOp.dr.find_element_by_css_selector('#reset_form').click()



    #充电单的车的状态查询
    def CdCarStatusSelect(self,status):
        ele = WebOp.dr.find_element_by_css_selector('#liststatus')
        ele.click()
        #选择状态
        Select(ele).select_by_visible_text(status)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    # 获取充电单状态查询数据
    def GetCdCarStatus(self,status):
        code = u"//*[@class='table table-border table-bordered table-bg table-hover']//tbody/tr/td[9]"
        eles = WebOp.dr.find_elements_by_xpath(code)
        if eles:
            for ele in eles:
                if ele.text == status:
                    continue
                else:
                    return False
        else:
            return  None

        return True



    #充电单是否删除查询
    def CdCarIsDeleteSelect(self,status):
        ele = WebOp.dr.find_element_by_css_selector('#delstatus')
        ele.click()
        #选择状态
        Select(ele).select_by_visible_text(status)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    # 获取充电单删除状态数据
    def GetCdIsDeleteStatus(self, status):
        code = u"//*[@class='table table-border table-bordered table-bg table-hover']//tbody/tr/td[8]"
        eles = WebOp.dr.find_elements_by_xpath(code)
        for ele in eles:
            if ele.text == status:
                continue
            else:
                return False

        return True



    #充电网点查询
    def CdWdSelect(self,cdwd):
        ele = WebOp.dr.find_element_by_css_selector('#maintain')
        ele.send_keys(cdwd)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    def GetCdWd(self,cdwd):
        code = u"//*[@class='table table-border table-bordered table-bg table-hover']//tbody/tr/td[4]"
        eles = WebOp.dr.find_elements_by_xpath(code)
        if eles:
            for ele in eles:
                if ele.text == cdwd:
                    continue
                else:
                    return False
        else:
            return  None

        return True




    #充电桩公司查询
    def CdCompanySelect(self,company):
        ele = WebOp.dr.find_element_by_css_selector('#charge_company')
        ele.send_keys(company)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()
    #获充电桩公司
    def GetCdCompany(self,company):
        code = u"//*[@class='table table-border table-bordered table-bg table-hover']//tbody/tr/td[5]"
        eles = WebOp.dr.find_elements_by_xpath(code)
        if eles:
            for ele in eles:
                if ele.text == company:
                    continue
                else:
                    return False
        else:
            return  None

        return True


    def  CdFollowerSelect(self,follower):
        #输入跟进人
        ele = WebOp.dr.find_element_by_css_selector('#person')
        ele.click()
        ele.send_keys(follower)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()
    def ComeMainToXq(self):
        # 回到主页面@@@@
        WebOp.dr.switch_to.default_content()

        # 进入详情的内嵌页面
        WebOp.dr.switch_to.frame(WebOp.dr.find_element_by_xpath('//div[@id="iframe_box"]/div[3]/iframe'))
        time.sleep(1)

    def ComeMainToGd(self):
        # 回到主页面@@@@
        WebOp.dr.switch_to.default_content()

        # 进入详情的内嵌页面
        WebOp.dr.switch_to.frame(WebOp.dr.find_element_by_xpath('//div[@id="iframe_box"]/div[2]/iframe'))
        time.sleep(1)


    def GetCdFollower(self,follower):
        i = 0
        while True:

            time.sleep(1)
            # 点击充电单详情
            eles = WebOp.dr.find_elements_by_css_selector('a[data-title="充电单详情"]')
            if eles:
                eles[i].click()
                time.sleep(1)
                i += 1
                WebOp.ComeMainToXq(self)

                # 获取vin,通过子元素的唯一性实现父元素定位，再定位父元素的子元素
                eles = WebOp.dr.find_elements_by_xpath("//*[@class='follow']//tr/td[1]")
                follower_list = [ele.text for ele in eles]

                WebOp.CloseXiangQing(self)

                if follower not in follower_list:
                    return  False
                # 回到主页面@@@@，循环不了是因为，没有重新进入充电页面,进入内嵌的充电单页面@@@@
                WebOp.ComeMainToGd(self)

                if i >=len(eles):
                    break
            else:
                return  None

        return  True


    def CdCreateTimeSelect(self,startmin,startmax):
        time.sleep(1)
        ele = WebOp.dr.find_element_by_id('startmin')
        ele.send_keys(startmin)

        ele = WebOp.dr.find_element_by_id('startmax')
        ele.send_keys(startmax)

        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()
        time.sleep(1)

    def GetCdCreatTime(self,startmin,startmax):
        i = 0
        #时间参数是共享参数，不能放进循环里，会导致格式不对
        startmin = time.mktime(time.strptime(startmin, '%Y-%m-%d %H:%M:%S'))
        startmax = time.mktime(time.strptime(startmax, '%Y-%m-%d %H:%M:%S'))
        while True:

            time.sleep(2)
            # 点击充电单详情
            eles = WebOp.dr.find_elements_by_css_selector('a[data-title="充电单详情"]')
            if eles:
                eles[i].click()
                time.sleep(1)
                i += 1
                WebOp.ComeMainToXq(self)

                # 获取vin,通过子元素的唯一性实现父元素定位，再定位父元素的子元素
                ele = WebOp.dr.find_elements_by_xpath("//*[@class='follow']//tr[last()]/td[2]")
                createtime = ele[0].text

                WebOp.CloseXiangQing(self)
                createtime = time.mktime(time.strptime(createtime, u'%Y年%m月%d日 %H:%M:%S'))

                if not ((float(createtime)) >= (float(startmin)) and (float(createtime))<= (float(startmax))):
                    return  False

                # 回到主页面@@@@，循环不了是因为，没有重新进入充电页面,进入内嵌的充电单页面@@@@
                WebOp.ComeMainToGd(self)

                if i >= len(eles):
                    break
            else:
                return None

        return  True


    def CdFinishedTimeSelect(self,endmin,endmax):
        ele = WebOp.dr.find_element_by_css_selector('#charge_list input#endmin')
        ele.send_keys(endmin)

        ele = WebOp.dr.find_element_by_css_selector('#charge_list input#endmax')
        ele.send_keys(endmax)
        #d任意点击去掉时间框
        WebOp.dr.find_element_by_id('license').click()


        # 点击查询
        WebOp.dr.find_element_by_css_selector('button.btn.btn-success').click()

    def GetCdFinishedTime(self,endmin,endmax):
        i = 0
        endmin = time.mktime(time.strptime(endmin, '%Y-%m-%d %H:%M:%S'))
        endmax = time.mktime(time.strptime(endmax, '%Y-%m-%d %H:%M:%S'))
        while True:

            time.sleep(2)
            # 点击充电单详情
            eles = WebOp.dr.find_elements_by_css_selector('a[data-title="充电单详情"]')
            if eles:

                eles[i].click()
                time.sleep(1)
                i += 1
                WebOp.ComeMainToXq(self)

                # 获取vin,通过子元素的唯一性实现父元素定位，再定位父元素的子元素
                ele = WebOp.dr.find_elements_by_xpath("//*[@class='follow']//tr[2]/td[2]")
                finishedtime = ele[0].text
                print finishedtime

                WebOp.CloseXiangQing(self)

                #将时间转换为元组，再转化为时间戳

                finishedtime = time.mktime(time.strptime(finishedtime, u'%Y年%m月%d日 %H:%M:%S'))

                if not ((float(finishedtime)) >= (float(endmin)) and (float(finishedtime)) <= (float(endmax))):
                    return  False

                # 回到主页面@@@@，循环不了是因为，没有重新进入充电页面,进入内嵌的充电单页面@@@@
                WebOp.ComeMainToGd(self)

                if i >= len(eles):
                    break
            else:
               return  None
        return True





if __name__ == "__main__":
    op = WebOp()
    op.OpenBrowser("chrome")
    op.LoginWebSite('15833098112','Fyf136066')
    op.ToCdMenu()
    # op.CdNumSelect('100400')
    # op.GetCdNum()
    # op.CdVinSelect('114913')
    # op.GetCdVin()
    # op.CdChePaiSelect(u'京QW8T07')
    # op.GetCdChepai()
    # op.CdCarCompanySelect('一度用车')
    # op.GetCdCarCompany(u'一度用车')
    op.CdCreateTimeSelect('2017-07-05 0:0:0','2017-07-18 23:59:59')
    a=op.GetCdCreatTime('2017-07-05 0:0:0','2017-07-18 23:59:59')
    print a







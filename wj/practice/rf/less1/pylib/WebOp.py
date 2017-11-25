#coding=utf8
from sele import webdriver


class WebOp():

    shared_wd = None

    def OpenBrowser(self):
        if WebOp.shared_wd:
            return


        WebOp.shared_wd = webdriver.Chrome()
        WebOp.shared_wd.implicitly_wait(2)

    def CloseBrowser(self):
        WebOp.shared_wd.quit()

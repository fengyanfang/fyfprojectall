#coding=utf8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from conf import  *
from WebOp import WebOp
import time
from robot.api import logger



class  WebOpAdmin(WebOp):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def LoginWebsite(self,username,password):

        WebOp.shared_wd.get(MgrLoginUrl)
        WebOp.shared_wd.find_element_by_css_selector('#username').send_keys(username)
        WebOp.shared_wd.find_element_by_css_selector('#password').send_keys(password)
        WebOp.shared_wd.find_element_by_tag_name("button").click()
        time.sleep(1)

    def DeleteAll(self,objname):
        tab = u'ul.nav a[ui-sref={}]'.format(objname)
        WebOp.shared_wd.find_element_by_css_selector(tab).click()
        time.sleep(1)

        while True:
            delbuttons =  WebOp.shared_wd.find_elements_by_css_selector('button[ng-click="delOne(one)"]')

            if delbuttons == []:
                break

            delbuttons[0].click()
            WebOp.shared_wd.find_element_by_css_selector('.modal-footer .btn-primary').click()
            time.sleep(1)



    def AddCourse(self,coursename,desc,idx):
        WebOp.shared_wd.find_element_by_css_selector('ul.nav a[ui-sref="course"]').click()
        time.sleep(1)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="showAddOne"]').click()

        ele =  WebOp.shared_wd.find_element_by_css_selector('input[ng-model="addData.name"]')
        ele.clear()
        ele.send_keys(coursename)


        ele =  WebOp.shared_wd.find_element_by_tag_name('textarea')
        ele.clear()
        ele.send_keys(desc)

        ele =  WebOp.shared_wd.find_element_by_css_selector('input[ng-model="addData.display_idx"]')
        ele.clear()
        ele.send_keys(idx)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="addOne"]').click()
        time.sleep(1)

    def AddTeacher(self,teachername,loginname,desc,idx,lesson):
        WebOp.shared_wd.find_element_by_css_selector('ul.nav a[ui-sref="teacher"]').click()
        time.sleep(1)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="showAddOne"]').click()

        ele =  WebOp.shared_wd.find_element_by_css_selector('input[ng-model="addEditData.realname"]')
        ele.clear()
        ele.send_keys(teachername)

        ele =  WebOp.shared_wd.find_element_by_css_selector('input[ng-model="addEditData.username"]')
        ele.clear()
        ele.send_keys(loginname)

        ele =  WebOp.shared_wd.find_element_by_tag_name('textarea')
        ele.clear()
        ele.send_keys(desc)

        ele =  WebOp.shared_wd.find_element_by_css_selector('input[ng-model="addEditData.display_idx"]')
        ele.clear()
        ele.send_keys(idx)

        ele = Select( WebOp.shared_wd.find_element_by_css_selector('select[ng-model*=courseSelected]'))
        ele.select_by_visible_text(lesson)
        WebOp.shared_wd.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="addOne"]').click()
        time.sleep(1)


    def AddTraining(self,classname,desc,idx,lesson):
        WebOp.shared_wd.find_element_by_css_selector('ul.nav a[ui-sref="training"]').click()
        time.sleep(1)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="showAddOne"]').click()

        ele =  WebOp.shared_wd.find_element_by_css_selector('input[ng-model="addEditData.name"]')
        ele.clear()
        ele.send_keys(classname)

        ele =  WebOp.shared_wd.find_element_by_tag_name('textarea')
        ele.clear()
        ele.send_keys(desc)

        ele =  WebOp.shared_wd.find_element_by_css_selector('input[ng-model="addEditData.display_idx"]')
        ele.clear()
        ele.send_keys(idx)

        ele = Select( WebOp.shared_wd.find_element_by_css_selector('select[ng-model*="courseSelected"]'))
        ele.select_by_visible_text(lesson)
        WebOp.shared_wd.find_element_by_css_selector('button[ng-click*="addEditData.addTeach"]').click()

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="addOne"]').click()
        time.sleep(1)


    def AddTrainingGrade(self,traininggrade,desc,idx,classname):
        WebOp.shared_wd.find_element_by_css_selector('ul.nav a[ui-sref="traininggrade"]').click()
        time.sleep(1)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="showAddOne"]').click()

        ele =  WebOp.shared_wd.find_element_by_css_selector('input[ng-model="addEditData.name"]')
        ele.clear()
        ele.send_keys(traininggrade)

        ele =  WebOp.shared_wd.find_element_by_tag_name('textarea')
        ele.clear()
        ele.send_keys(desc)

        ele =  WebOp.shared_wd.find_element_by_css_selector('input[ng-model="addEditData.display_idx"]')
        ele.clear()
        ele.send_keys(idx)

        ele = Select( WebOp.shared_wd.find_element_by_css_selector('select[ng-model*="addEditData.training_id"]'))
        ele.select_by_visible_text(classname)


        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="addOne"]').click()
        time.sleep(1)


    def AddStudent(self,realname,loginname,desc,classname,traininggrade):
        WebOp.shared_wd.find_element_by_css_selector('ul.nav a[ui-sref="student"]').click()
        time.sleep(1)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="showAddOne"]').click()

        ele =  WebOp.shared_wd.find_element_by_css_selector('ng-model="addEditData.realname"]')
        ele.clear()
        ele.send_keys(realname)

        ele =  WebOp.shared_wd.find_element_by_css_selector('ng-model="addEditData.username"]')
        ele.clear()
        ele.send_keys(loginname)

        ele =  WebOp.shared_wd.find_element_by_tag_name('textarea')
        ele.clear()
        ele.send_keys(desc)

        ele = Select( WebOp.shared_wd.find_element_by_css_selector('select[ng-model*="addEditData.training_id"]'))
        ele.select_by_visible_text(classname)

        ele = Select( WebOp.shared_wd.find_element_by_css_selector('select[ng-model*="addEditData.traininggrade_id"]'))
        ele.select_by_visible_text(traininggrade)


        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="addOne"]').click()
        time.sleep(1)

    def AddLesson(self,course,desc):
        WebOp.shared_wd.find_element_by_css_selector('ul.nav a[ui-sref="lesson"]').click()
        time.sleep(1)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^="showAddOne"]').click()

        ele = Select(WebOp.shared_wd.find_element_by_css_selector('select[ng-model*="addEditData.course_id"]'))
        ele.select_by_visible_text(course)

        WebOp.shared_wd.find_element_by_tag_name('textarea').send_keys(desc)

        WebOp.shared_wd.find_element_by_css_selector('button[ng-click*="addOne"]').click()
        time.sleep(1)


    def GetCourseList(self):
        WebOp.shared_wd.find_element_by_css_selector('ul.nav a[ui-sref="course"]').click()
        time.sleep(1)

        eles =  WebOp.shared_wd.find_elements_by_css_selector('tr>td:nth-child(2)') #elements
        courselist = [ele.text for ele in eles]

        return courselist

    def GetTeacherList(self):
        WebOp.shared_wd.find_element_by_css_selector('ul.nav a[ui-sref="teacher"]').click()
        time.sleep(1)

        eles =  WebOp.shared_wd.find_elements_by_css_selector('tr>td:nth-child(2)')  #elements
        teacherlist = [ele.text for ele in eles]

        return  teacherlist

    def  GetStudentList(self):
        WebOp.shared_wd.find_element_by_css_selector('ul.nav a[ui-sref="student"]').click()
        time.sleep(1)

        eles =  WebOp.shared_wd.find_elements_by_css_selector('tr>td:nth-child(2)')
        studentlist = [ele.text for ele in eles]

        return  studentlist

def test():
    wo = WebOpAdmin()
    # 打开浏览器，创建webdrier

    wo.OpenBrowser()
    wo.LoginWebsite('auto', 'sdfsdfsdf')

    wo.DeleteAll('student')
    wo.DeleteAll('traininggrade')
    wo.DeleteAll('training')
    wo.DeleteAll('teacher')
    wo.DeleteAll('course')

    wo.AddCourse(u'初中化学', u'...', '3')
    wo.AddTraining(u'初中班', '...', '1', u'初中化学')
    wo.AddTrainingGrade(u'初中班1期', '...', '1', u'初中班')
    wo.AddStudent(u'关羽', u'guanyu', '...', u'初中班', u'初中班1期')
    wo.GetStudentList()

    wo.DeleteAll('student')
    wo.DeleteAll('traininggrade')
    wo.DeleteAll('training')
    wo.DeleteAll('teacher')
    wo.DeleteAll('course')
if "__name__" == "__main__":
    test()




























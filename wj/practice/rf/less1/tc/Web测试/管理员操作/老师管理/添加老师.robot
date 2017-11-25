*** Settings ***
Library     Selenium2Library
Library     Collections
Library     pylib.WebOpAdmin


*** Test Cases ***
添加老师
     [Setup]  Run Keywords  DeleteAlllesson
     ...  AND     DeleteAllteacher
     ...  AND     AddCourse   初中语文     初中语文      1
     ...  AND     AddCourse   初中数学     初中数学      2

     AddTeacher   艳芳     yanfang     艳芳老师      1     初中数学
     ${teachers}=     GetTeacherList
     should be true     $teachers==[u'艳芳']


     AddTeacher   金凯    jinkai    金凯老师      2     初中语文
     ${teachers}=     GetTeacherList
     should be true     $teachers==[u'艳芳',u'金凯']

     [Teardown]  Run Keywords       DeleteAlllesson   AND   DeleteAllteacher


*** Settings ***
Library     Selenium2Library
Library     Collections
Library     pylib.WebOpAdmin


*** Test Cases ***
添加课程

     [Setup]    DeleteAlllesson

     AddCourse    初中数学     初中数学      2
     ${lessons}=     GetCourseList
     should be true     $lessons==[u'初中数学']


     AddCourse    初中语文     初中语文      1
     ${lessons}=     GetCourseList
     should be true     $lessons==[u'初中语文',u'初中数学']

     [Teardown]     DeleteAlllesson






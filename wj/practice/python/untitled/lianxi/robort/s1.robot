
*** Settings ***
Library    Selenium2Library


*** Test Cases ***
搜索北京时间
           Open Browser    http://www.114time.com/     chrome
           ${cur_year}=    Get Text                    css=#current-data
           set selenium implicit wait   5
           should be equal   ${cur_year}                2017
           close browser



*** Test Cases ***
练习变量的使用
           set variable

*** Settings ***
Library   Selenium2Library
Library   Dialogs       #c查看dialog模块（对话框）

*** Test Cases ***
半自动化
      Pause Execution                                                #提示输入验证码
      Execute Manual Step                                            #提示检查logo是否通过，输入错误信息
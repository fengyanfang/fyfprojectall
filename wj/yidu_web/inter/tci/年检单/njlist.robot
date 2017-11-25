*** Settings ***
Variables   cfg.py
Library     pylib.njlib
Library     pylib.mysql_data    manager
#Suite Setup   run keywords    clear  inspection_list
#          ...  AND   clear   inspection_operate_log


#找不到用例是右下角编码该为utf8
*** Test Cases ***

列出年检单001

       ${list}=          nj_list

       should be true    $list['status']==0
       should be true    $list['data']['inspectionCount']=='54'
       should be true    $list['data']['inspectionList'][0]['inspection_num']=='NJ100001'
       should be true    $list['data']['inspectionList'][0]['create_name']==u'安卓'


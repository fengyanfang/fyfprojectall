*** Settings ***
Variables   cfg.py
Library     pylib.yongche
Library     pylib.mysql_data    manager
#Suite Setup   run keywords    clear  inspection_list
#          ...  AND   clear   inspection_operate_log


#找不到用例是右下角编码该为utf8
*** Test Cases ***
列出优惠券
        ${ret}=        list_coupon

        should be true     $ret['status']==0
        should be equal        $ret['data'][0]['uid']==1192
*** Settings ***
Variables   conf.py
Library     pylib.WebOp
Library     pylib.DataBase    manager
Suite Setup   run keywords      clear   chargeup_list
      ...  AND   clear   chargeup_operate_log
      ...  AND   cd_insert  1
      ...  AND   cd_insert  2
      ...  AND   cd_insert  3
      ...  AND   cd_insert  4
      ...  AND   cd_change_record      2
      ...  AND   cd_delete    2
      ...  AND   close
      ...  AND  ToCdMenu

*** Test Cases ***
编号查询01

       CdNumSelect     100001
       ${GETNUM}=    GetCdNum   100001

       SHOULD BE TRUE     $GETNUM

       [Teardown]   ClearCdNum

编号查询02_查不到信息

       CdNumSelect     100987
       ${GETNUM}=    GetCdNum   100987

       should be true    $GETNUM==None

       [Teardown]   ClearCdNum


充电单vin查询03

      CdVinSelect   142726
      ${getvin}=     GetCdVin

      should be true    $getvin==u'142726'

      [Teardown]   run keywords     CloseXiangQing
       ...  AND   ClearVin

充电单vin查询04_查不到信息
      CdVinSelect   142777
      ${getvin}=     GetCdVin

      should be true    $getvin==None
       [Teardown]   Reset


充电单车牌查询05

       CdChePaiSelect      京QW8T07
       ${getchepai}=       GetCdChepai

       should be true     $getchepai==u'京QW8T07'

       [Teardown]   run keywords     CloseXiangQing
       ...  AND   ClearCdChePai

充电单车牌查询06_查不到信息
         CdChePaiSelect     京Q7NJ23
       ${getchepai}=       GetCdChepai

       should be true     $getchepai==None

       [Teardown]   Reset


充电单公司查询07

       CdCarCompanySelect   一度用车
       ${company}=   GetCdCarCompany   一度用车

       should be true  $company

       [Teardown]   Reset

充电单公司查询08_查不到信息

       CdCarCompanySelect   广州一度
       ${company}=   GetCdCarCompany   广州一度

       should be true  $company==None

       [Teardown]   Reset


充电单状态查询09
       CdCarStatusSelect   待充电
       ${status}=     GetCdCarStatus   待充电

       should be true   $status

       [Teardown]   Reset

充电单状态查询10
       CdCarStatusSelect  充电中
       ${status}=     GetCdCarStatus   充电中

       should be true   $status

       [Teardown]   Reset

充电单状态查询11
       CdCarStatusSelect  已完成
       ${status}=     GetCdCarStatus   已完成

       should be true   $status==None

       [Teardown]   Reset


充电单是否删除查询12
       CdCarIsDeleteSelect    是
       ${status}=   GetCdIsDeleteStatus   已删除

       should be true   $status

       [Teardown]   Reset


充电单是否删除查询13
       CdCarIsDeleteSelect    否
       ${status}=   GetCdIsDeleteStatus  否

       should be true   $status

       [Teardown]   Reset


充电网点查询14
      CdWdSelect   充电点Aa
      ${cdwd}=   GetCdWd    充电点Aa

      should be true   $cdwd

      [Teardown]   Reset

充电网点查询15
      CdWdSelect   充电点b
      ${cdwd}=   GetCdWd    充电点b

      should be true   $cdwd==None

      [Teardown]   Reset

充电桩公司查询16
      CdCompanySelect   特来电

      ${cdcompany}=    GetCdCompany   特来电

      should be true   $cdcompany

      [Teardown]   Reset


充电桩公司查询17_查不到信息
      CdCompanySelect   啊啊啊

      ${cdcompany}=    GetCdCompany   啊啊啊

      should be true   $cdcompany==None

      [Teardown]   Reset


充电单跟进人查询18
      CdFollowerSelect   yan
      ${follower}=   GetCdFollower  yan

      should be true    $follower
      [Teardown]   Reset

充电单跟进人查询19_查不到信息
      CdFollowerSelect   fyflove
      ${follower}=   GetCdFollower  fyflove

      should be true    $follower==None
      [Teardown]   Reset


创建时间查询20
      CdCreateTimeSelect     2017-07-18 0:0:0     2017-12-30 23:59:59
      ${createtime}=   GetCdCreatTime   2017-07-18 0:0:0     2017-12-30 23:59:59

      should be true   $createtime
      [Teardown]   Reset

创建时间查询21_查不到信息
       CdCreateTimeSelect      2017-07-14 0:0:0    2017-07-15 23:59:59
       ${createtime}=     GetCdCreatTime    2017-07-14 0:0:0    2017-07-15 23:59:59

       should be true   $createtime==None
       [Teardown]   Reset


完成时间查询22
      [Setup]   cd_change_record      5
      CdFinishedTimeSelect      2017-07-05 0:0:0    2017-12-30 23:59:59
      ${endtime}=     GetCdFinishedTime   2017-07-05 0:0:0    2017-12-30 23:59:59

      should be true   $endtime
      [Teardown]   Reset


完成时间查询23_查不到信息
      CdFinishedTimeSelect      2017-07-14 0:0:0  2017-07-15 23:59:59
      ${endtime}=    GetCdFinishedTime    2017-07-14 0:0:0  2017-07-15 23:59:59

      should be true   $endtime==None
       [Teardown]   run keywords    Reset
       ...   AND   Comemain
       ...   AND   CloseGd





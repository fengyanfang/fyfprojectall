*** Settings ***
Variables   conf.py
Library     pylib.WebOp
Library     pylib.DataBase    manager
Suite Setup   run keywords      clear   dispatch_list
      ...  AND   clear   dispatch_operate_log
      ...  AND   dd_insert  1
      ...  AND   dd_insert  2
      ...  AND   dd_insert  3
      ...  AND   dd_insert  4
      ...  AND   dd_modify  1
      ...  AND   dd_delete  2
      ...  AND   close
      ...  AND  ToDdMenu
*** Test Cases ***
调度单号查询_查到信息dd001
     DdNumberSelect         100001
     ${ddnum}=             GetDdNumber      100001

     should be true         $ddnum
     [Teardown]  Reset

调度单号查询_查不到信息dd001
      DdNumberSelect         100009
     ${ddnum}=             GetDdNumber      100009

     should be true         $ddnum==None
     [Teardown]  Reset

公司查询_查到信息一度用车dd002
      DdCarCompanySelect     一度用车
      ${company}=       GetDdCarCompany    一度用车

      should be true     $company
      [Teardown]  Reset

公司查询_查不到信息广州一度dd002
      DdCarCompanySelect     广州一度
      ${company}=       GetDdCarCompany     广州一度

      should be true     $company==None
      [Teardown]  Reset

vin号查询_查到信息dd003
       DdVinSelect     114963
       ${vin}=     GetDdVin


       should be true   $vin==u'114963'
       [Teardown]  run keywords   CloseXiangQing
       ...   AND    ClearVin

vin号查询_查不到信息dd003
      DdVinSelect     114964
      ${vin}=     GetDdVin

      should be true   $vin==None
      [Teardown]   Reset

车牌查询_查到信息dd004
       DdChepaiSelect     京Q2PK99
       ${chepai}=       GetDdChepai     京Q2PK99

       should be true     $chepai
       [Teardown]   Reset

车牌查询_查不到信息dd004
       DdChepaiSelect     京Q2PK98
       ${chepai}=       GetDdChepai     京Q2PK98

       should be true     $chepai==None
       [Teardown]   Reset

工单状态查询_调度中dd005
       DdStatusSelect   调度中
       ${status}=    GetDdStatus      调度中

       should be true     $status
       [Teardown]   Reset

工单状态查询_已完成dd005
       DdStatusSelect   已完成
       ${status}=    GetDdStatus      已完成

       should be true     $status
       [Teardown]   Reset

跟进人查询_查到信息dd006
        DdFollowerSelect    yan

        ${follower}=    GetDdFollower  yan
        should be true   $follower
        [Teardown]   Reset
跟进人查询_查不到信息dd006
        DdFollowerSelect    yann

        ${follower}=    GetDdFollower  yann
        should be true   $follower==None
        [Teardown]   Reset

创建时间查询_查到信息dd007
        DdCreatetimeSelect    2017-08-18 0:0:0     2018-12-30 23:59:59
        ${createtime}=   GetDdCreatetime      2017-08-18 0:0:0     2018-12-30 23:59:59

        should be true   $createtime
        [Teardown]   Reset


创建时间查询_查不到信息dd007
        DdCreatetimeSelect    2017-08-18 0:0:0     2017-08-19 23:59:59
        ${createtime}=    GetDdCreatetime      2017-08-18 0:0:0     2017-08-19 23:59:59

        should be true     $createtime==None    #注意是== 不是=
        [Teardown]   Reset


完成时间查询_查到信息dd008
        DdFinishedtimeSelect    2017-08-18 0:0:0     2018-12-30 23:59:59
        ${finishedtime}=   GetDdFinishedtime    2017-08-18 0:0:0     2018-12-30 23:59:59

        should be true   $finishedtime
        [Teardown]   Reset

完成时间查询_查不到信息dd008
        DdFinishedtimeSelect    2017-08-18 0:0:0      2017-08-19 23:59:59
        ${finishedtime}=     GetDdFinishedtime       2017-08-18 0:0:0     2017-08-19 23:59:59

        should be true   $finishedtime==None
        [Teardown]   Reset

工单删除状态查询_是dd009
        DdDelstatusSelect     是
        ${delstatus}=    GetDdDelstatus     已删除

        should be true    $delstatus
        [Teardown]   Reset

工单删除状态查询_否dd009
        DdDelstatusSelect     否
        ${delstatus}=    GetDdDelstatus    否

        should be true    $delstatus
       [Teardown]   Reset

工单删除状态查询_全部dd009
        DdDelstatusSelect     全部
        ${delstatus}=    GetDdDelstatus    全部

        should be true    $delstatus
       [Teardown]   run keywords    Reset
       ...   AND   Comemain
       ...   AND   CloseGd


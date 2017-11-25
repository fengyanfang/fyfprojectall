*** Settings ***
Library    pylib.AppOp

*** Test Cases ***
vin查询
      [Setup]   CdSelect

      CdSelectVin    114937
      ${cdvin}=   CdGetVin

      should be true   $cdvin==u'114937'

      [Teardown]   ComeMain1


车牌查询
     [Setup]   CdSelect
     CdChePaiSelect     京Q2PK25
     ${cdgetchepai}=   CdGetChePai

     should be true   $cdgetchepai==u'京Q2PK25'
      [Teardown]   ComeMain1

充电编号查询
      [Setup]   CdSelect

      CdNumSelect   100423
      ${cdnum}=    CdGetNum

      should be true     $cdnum==u'100423'

      [Teardown]   ComeMain1


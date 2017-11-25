*** Settings ***
Library    pylib.AppOp

*** Test Cases ***
vin查询
      SelectVin    114937
      ${vintext}=    GetVin

      log to console      ${vintext}

      should be true    $vintext==u'114937'

      [Teardown]   ComeMain1

车牌查询
     SelectChePai       京Q1NK05
     ${carnum}=    GetCarNum

     log to console   ${carnum}

     should be true   $carnum==u'京Q1NK05'
     [Teardown]   ComeMain2
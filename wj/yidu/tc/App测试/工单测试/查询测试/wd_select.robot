*** Settings ***
Library    pylib.AppOp

*** Test Cases ***
网点查询
       WdSelect    阳光

       ${wdtext}=    GetWdText
       should be true   $wdtext==u'阳光878东区(院内)地面停车场'

       [Teardown]   ComeMain3
*** Settings ***
Library    pylib.AppOp

*** Test Cases ***
创建充电单
     [Setup]  Run Keywords  CdSelect
     ...  AND     DeleteCdList
     ComeMain1

     CdCdCarTable
     CreateCd

     ${verirycd}=   VerifyCdCreated
     ComeMain4

     should be true    $verirycd



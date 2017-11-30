*** Settings ***
Variables   conf.py
Library     pylib.StuMange

Suite Setup        OpenBrowser    chrome
Suite Teardown     CloseBrowser

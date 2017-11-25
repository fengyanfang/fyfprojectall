*** Settings ***
Variables   conf.py
Library     pylib.WebOp

Suite Setup       OpenBrowser    chrome
Suite Teardown    CloseBrowser
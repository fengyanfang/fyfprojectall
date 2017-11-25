*** Settings ***
Library     pylib.WebOpAdmin
Variables     conf.py
Suite Setup    LoginWebsite     &{adminuser}[name]       &{adminuser}[pw]
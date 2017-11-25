# coding=utf8
from django.shortcuts import render


from django.http import HttpResponse

studentTable = {
    'zhangsan':{
        'loginname' : 'zhangsan',
        'name':u'张三',
        'age': 16
    },
    'lisi':{
        'loginname' : 'lisi',
        'name':u'李四',
        'age': 18
    },
    'wanger':{
        'loginname' : 'wanger',
        'name':u'王二',
        'age': 16
    },
    'xuda':{
        'loginname' : 'xuda',
        'name':u'许达',
        'age': 16
    },
}




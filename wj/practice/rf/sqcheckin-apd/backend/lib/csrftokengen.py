# coding=utf-8

import time,re,json,os

from django.shortcuts import redirect
from django.http import HttpResponse
from django.middleware import csrf


# def getToken(request):
#     csrf.get_token(request)
#     #print 'request csrf token'
#     returnUrl = request.GET.get('returnurl')
#     #print 'returnurl',returnUrl
#
#     return redirect(returnUrl)
#     #return HttpResponse('ok')

def getToken(request):
    csrf.get_token(request)

    return HttpResponse('ok')


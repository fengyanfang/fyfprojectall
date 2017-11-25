# coding=utf-8

import traceback

from django.http import JsonResponse


import logging
app_logger =  logging.getLogger("teacher")



Error_Not_Login = JsonResponse({'retcode': 1,'reason': u'未登录', 'redirect':'/teacher/login/login.html'})
Error_Not_Admin = JsonResponse({'retcode': 1,'reason': u'非法调用', 'redirect':'/teacher/login/login.html'})


def CheckUserIsTeacherForApiCaller(request):
    if not request.user.is_authenticated():
        return Error_Not_Login

    if 'ut' not in request.session :
        return Error_Not_Login

    if request.session['ut'] != 2:
        return Error_Not_Admin

    return True
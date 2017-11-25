# coding=utf-8

import os

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.middleware import csrf

from apps.student.share import app_logger
from project.settings_common import USER_TYPE
from services.datamodel.common.models import Student

class ReqHandler():
    def __init__(self):

        self.curDir = os.path.dirname(os.path.abspath(__file__))





    def loginReq(self,request):

        userName = request.POST.get('username')
        passWord = request.POST.get('password')

        user = authenticate(username=userName, password=passWord)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                # app_logger.debug("User is valid, active and authenticated")
                if hasattr(user, 'student') :
                    if user.student.graduated:
                        return JsonResponse({'retcode': 1, 'reason': u'您已经毕业，不能再使用该系统'})
                    login(request, user)
                    request.session['ut'] = USER_TYPE.STDUENT # user type 3 means student
                    request.session['studentid'] = user.student.id
                    request.session['realname'] = user.student.realname
                    return JsonResponse({'retcode': 0,'realname':user.student.realname})
                else:
                    return JsonResponse({'retcode':1,'reason':u'请使用学生账户登录'})
            else:
                return JsonResponse({'retcode':1,'reason':u'用户已经被禁用'})
        else:
            return JsonResponse({'retcode': 1,'reason':u'用户或者密码错误'})




    def logoutReq(self,request):
        logout(request)
        return JsonResponse({'retcode': 0})


handler = ReqHandler()

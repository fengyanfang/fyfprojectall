# coding=utf-8

from django.conf.urls import url
#  from django.conf.urls.static import static

import os,time
from apps.teacher.share import app_logger

from apps.teacher.handlers import loginout,teacher

from django.http import JsonResponse
from project.settings_common import USER_TYPE
from django.views.decorators.csrf import csrf_exempt

Error_Not_Login =  JsonResponse({'retcode': 302,'reason': u'未登录', 'redirect':'/teacher/login/login.html'})
Error_Not_Teacher = JsonResponse({'retcode': 1,'reason': u'请以老师帐号登录', 'redirect':'/teacher/login/login.html'})


mobile_Error_Not_Login =  JsonResponse({'retcode': 99,'msg': u'未登录'})
mobile_Error_Not_Teacher = JsonResponse({'retcode': 100,'msg': u'请以老师帐号登录'})




def CheckUserIsTeacherForApiCaller(request,*args,**kwargs):
    execStartTime = time.time()
    if 'ut' not in request.session :
        return Error_Not_Login

    if request.session['ut'] != USER_TYPE.TEACHER:
        return Error_Not_Teacher

    realCall = kwargs.pop('_viewFunc')
    ret = realCall(request,*args,**kwargs)

    execEndTime = time.time()
    # 所有大于100ms的操作，产生日志告警
    opTime = execEndTime-execStartTime
    if (opTime > 0.1):
        app_logger.warning('!! op takes %s seconds : function:%s %s  ' % (opTime,request.method,request.path))

    return ret



urlpatterns_api = []

def addPreCheck(urlpatterns,checkFunC):
    for pattern in urlpatterns:
        urlRegx = pattern[0]
        if type(urlRegx) != list:
            urlRegList = [urlRegx]
        else:
            urlRegList = urlRegx

        viewFunc = pattern[1]
        if len(pattern) == 2:
            for one in urlRegList:
                urlpatterns_api.append(url(one, checkFunC, {'_viewFunc': viewFunc}))

        elif len(pattern) == 3:
            otherPara = pattern[2]
            otherPara['_viewFunc'] = viewFunc
            for one in urlRegList:
                urlpatterns_api.append(url(one, checkFunC, otherPara))
        else:
            print '!!unsupported url format : %s' % pattern
            os._exit(3)



urlpatterns_api_agrs = [


    (r'^sq_teacher/$',
     teacher.teacher_handler.dispatch),



    ]

addPreCheck(urlpatterns_api_agrs,CheckUserIsTeacherForApiCaller)


urlpatterns = [

    url(r'^loginreq$', loginout.handler.loginReq),
    url(r'^logoutreq$', loginout.handler.logoutReq),


] + urlpatterns_api 

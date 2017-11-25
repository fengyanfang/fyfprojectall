# coding=utf-8

from django.conf.urls import url
#  from django.conf.urls.static import static


from apps.mgr.handlers import loginout,mgr
# from apps.mgr.handlers import school, school_class, teacher, student, schooltype
# from apps.mgr.handlers import product,operators,goods,yjaccount,notice
from apps.mgr.share import app_logger

import os,time

from django.http import JsonResponse
Error_Not_Login = JsonResponse(
    {'retcode': 302, 'reason': u'未登录', 'redirect': '/mgr/login/login.html'})
Error_UserType = JsonResponse(
    {'retcode': 1, 'reason': u'请以正确权限的帐号登录', 'redirect': '/mgr/login/login.html'})


# A simple security checking, more preventions are needed in risky APIs: modification, deletion, insert etc.
# user type to http referer string
HTTP_REFERER_DICT = {
    1: '/mgr/',
    1001: '/datainputer/',
    1002: '/ragent/',
}


def CheckUserIsAdminForApiCaller(request,*args,**kwargs):
    # if not request.user.is_authenticated():
    #     return Error_Not_Login

    execStartTime = time.time()

    if 'ut' not in request.session :
        return Error_Not_Login

    if (request.session['ut'] != 1) and (request.session['ut'] != 1002):
        return Error_UserType

    referer = request.META.get('HTTP_REFERER')
    if referer and (HTTP_REFERER_DICT[request.session['ut']] in referer):
        pass
    else:
        return Error_UserType

    realCall = kwargs.pop('_viewFunc')


    ret = realCall(request,*args,**kwargs)

    execEndTime = time.time()
    # 所有大于100ms的操作，产生日志告警
    opTime = execEndTime-execStartTime
    if (opTime > 0.1):
        app_logger.warning('!! op takes %s seconds : function:%s %s  ' % (opTime,request.method,request.path))
    else:
        app_logger.debug('op takes %s seconds : function:%s %s  ' % (opTime,request.method,request.path))

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






#     (r'^qiniu/video/(?P<action>\w+)$',
#      qiniucloud.qiniu_handler.dispatch, {'resource_type': 'video'}),
#     (r'^qiniu/img/(?P<action>\w+)$',
#      qiniucloud.qiniu_handler.dispatch, {'resource_type': 'img'}),


    (r'^sq_mgr/$',
     mgr.commonHandler.dispatch),

]

addPreCheck(urlpatterns_api_agrs,CheckUserIsAdminForApiCaller)


urlpatterns = [

    url(r'^login$', loginout.handler.login),
    url(r'^loginReq$', loginout.handler.loginReq),
    url(r'^logoutreq$', loginout.handler.logoutReq),
    url(r'^loginas_step2$', loginout.handler.mgrToOtherRole_step2),

] + urlpatterns_api

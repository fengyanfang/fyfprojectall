# coding=utf8

# 导入 认证用户，和登录 需要的函数
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

# 认证请求处理函数
def logincheck( request):

    # 从http请求中获取用户名密码
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # 调用 authenticate 方法进行认证，
    # 校验用户名密码：前端明文发送，数据库中是加密的密码。
    # 如果认证通过，返回结果就是该用户对应的一个用户实例对象
    # 否则就是None
    user = authenticate(username=userName, password=passWord)
    if user == None:
        return JsonResponse({'retcode': 1, 'reason': '用户或者密码错误'})
    else:
        if user.is_active:

            # 如果是管理员
            if user.is_superuser:
                ut = 'mgr'
                homeurl = '/mgr/index.html' # 重定向到
            else:
                ut = 'student'
                homeurl = '/student/index.html' # 重定向到

            print (request.user.is_authenticated) # 结果为False
            print (request.session.session_key)

            # 调用 认证系统 的方法 login,设置用户表中的lastlogin等 ，创建session等信息
            # session中标志该用户为已认证用户
            login(request, user)

            print (request.user.is_authenticated) # 结果为True
            print (request.session.session_key)

            # 可以在session 中 填入数据，方便后面的流程使用，不然后面还需要到数据库中获取
            request.session['ut'] = ut
            return JsonResponse({'retcode': 0, 'goto':homeurl})
        else:
            return JsonResponse({'retcode': 2, 'reason': '用户已经被禁用'})



# 退出登录请求处理函数
def logoutuser( request):
    # 该函数的实现 会将该登录的session数据清除
    logout(request)
    return JsonResponse({'retcode': 0})
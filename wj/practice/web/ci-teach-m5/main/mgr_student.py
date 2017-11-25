# coding=utf8

from django.http import HttpResponse, JsonResponse, QueryDict

from models import Course
from django.views.decorators.csrf import csrf_exempt
import json,traceback
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db.models import F

def dispatch(request):
    # 为了不同的method类型的http请求，都可以用统一的方法获取参数
    # 将参数统一放入 request.params 中
    if request.method == 'GET':
        params = request.GET
    elif request.method == 'POST':
        params = request.POST
    elif request.method == 'PUT':
        params = QueryDict(request.body)
    elif request.method == 'DELETE':
        params = QueryDict(request.body)
    else:
        # JsonResponse 类型，和以前的HTTP response 不同
        return JsonResponse({'retcode': 1, 'err': u'不支持的 method 类型'})

    # 存入request中，动态创建属性， request是每个请求独有的，由django框架生成
    request.params = params

    # 判断请求中是否有action参数
    if 'action' not in request.params:
        return JsonResponse({'retcode': 1, 'err': u'需要 action 参数'})

    action = request.params['action']

    # 根据action分发给不同的函数处理，对应不同的请求。这是url路由外的另一种 请求-处理函数  表的实现
    if action == 'list_student':
        return list_student(request)
    elif action == 'add_student':
        return add_student(request)
    elif action == 'delete_student':
        return delete_student(request)
    elif action == 'modify_student':
        return modify_student(request)
    else:
        return JsonResponse({'retcode': 1, 'err': u'action not supported'})


# 列出学生处理


def list_student(request):
    pagesize = json.loads(request.params['pagesize'])
    pagenum = json.loads(request.params['pagenum'])

    # 用户表对应的 类定义在  django.contrib.auth.models import User
    # 过滤条件，只获取学生信息。 注意annotate 可以用来修改字段名称
    qs = User.objects.filter(is_superuser=False) \
        .annotate(realname=F('last_name'))\
        .values('realname','id','username').order_by('-id')


    # 产生 Paginator 对象，用于分页
    pgnt = Paginator(qs, pagesize)

    # 返回指定页数的学生，注意是lazy load ， 前面不会先把
    # 所有学生信息都获取出来
    retlist = list(pgnt.page(pagenum))

    # total 是 告诉前端总共有多少页
    ret = {'retcode': 0, 'retlist': retlist, 'total': pgnt.count}
    return JsonResponse(ret, safe=False)


# 添加学生处理
from django.contrib.auth.hashers import make_password

def add_student(request):
    data = json.loads(request.params['data'])
    username = data['username']
    realname = data['realname']
    password = data['password']

    try:
        User.objects.create(
            username=username,
            password=make_password(password),
            last_name=realname,
        )
    except Exception,e:
        return JsonResponse({'retcode':2, 'reason':str(e)})

    ret = {'retcode':0}
    return JsonResponse(ret)



# 删除学生处理
def delete_student(request):
    rid = request.params['id']
    user = User.objects.get(id=rid)
    user.delete()
    ret = {'retcode': 0}
    return JsonResponse(ret, safe=False)


# 修改学生处理
def modify_student(request):

    record = User.objects.get(id=request.params['id'])

    # 由于是json编码，这里需要解码为对象
    newdata = json.loads(request.params['newdata'])
    record.username = newdata['username']
    record.last_name = newdata['realname']

    record.save()


    ret = {'retcode': 0}
    return JsonResponse(ret, safe=False)
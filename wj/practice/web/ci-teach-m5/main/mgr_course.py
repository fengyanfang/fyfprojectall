# coding=utf8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,QueryDict


from models import Course

import json


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
    if action == 'list_course':
        return list_course(request)
    elif action == 'add_course':
        return add_course(request)
    elif action == 'delete_course':
        return delete_course(request)
    elif action == 'modify_course':
        return modify_course(request)
    else:
        return JsonResponse({'retcode': 1, 'err': u'action not supported'})




# 列出课程处理
def list_course(request):
    courseList = Course.objects.all().values()
    ret = {'retcode': 0, 'data': list(courseList)}
    return JsonResponse(ret, safe=False)

# 添加课程处理
def add_course(request):
    # 前面可以有检查是否有data的逻辑
    print request.params['data']

    # 由于是json编码，这里需要解码为对象
    data = json.loads(request.params['data'])
    
    Course.objects.create(name=data['name'],
                          desc=data['desc'],
                          display_idx=data['display_idx'])
        
    ret = {'retcode':0}
    return JsonResponse(ret,safe=False)


# 删除课程处理
def delete_course(request):
    rid = request.params['id']

    try:
        Course.objects.filter(id=rid).delete()

    except Exception,e:
        return JsonResponse({'retcode':2, 'reason':str(e)})

    ret = {'retcode': 0}
    return JsonResponse(ret, safe=False)


# 修改课程处理
def modify_course(request):


    record = Course.objects.get(id=request.params['id'])

    # 由于是json编码，这里需要解码为对象
    newdata = json.loads(request.params['newdata'])
    record.name = newdata['name']
    record.desc = newdata['desc']
    record.display_idx = newdata['display_idx']

    record.save()


    ret = {'retcode': 0}
    return JsonResponse(ret, safe=False)
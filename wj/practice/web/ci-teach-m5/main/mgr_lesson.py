# coding=utf8

from django.http import HttpResponse, JsonResponse, QueryDict

from models import Lesson
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage
import json
from django.utils.dateparse import parse_datetime

def dispatch(request):
    if request.method == 'GET':
        params = request.GET
    elif request.method == 'POST':
        params = request.POST
    elif request.method == 'PUT':
        params = QueryDict(request.body)
    elif request.method == 'DELETE':
        params = QueryDict(request.body)
    else:
        return JsonResponse({'retcode': 1, 'err': u'不支持的 method 类型'})

    request.params = params

    # 判断请求中是否有action参数
    if 'action' not in request.params:
        return JsonResponse({'retcode': 1, 'err': u'需要 action 参数'})

    action = request.params['action']

    if action == 'list_lesson':
        return list_lesson(request)
    elif action == 'add_lesson':
        return add_lesson(request)
    elif action == 'delete_lesson':
        return delete_lesson(request)
    elif action == 'modify_lesson':
        return modify_lesson(request)
    else:
        return JsonResponse({'retcode': 1, 'err': u'action not supported'})



def list_lesson(request):
    # 获取 参数的值
    pagenum = int(request.params['pagenum'])
    pagesize = int(request.params['pagesize'])

    # 数据库表中，Lesson 对应的Course 只有其id，
    # 我们需要获取名字（根据接口文档）
    qs = Lesson.objects.all().select_related('course') \
        .annotate(course_name=F('course__name'))


    qs = qs.values('id','course_id','course_name','starttime','endtime',
                   'desc').order_by('-id')

    pgnt = Paginator(qs, pagesize)

    retObj = list(pgnt.page(pagenum))


    return JsonResponse({'retcode': 0, 'retlist': retObj, 'total': pgnt.count})




def add_lesson(request):
    data = json.loads(request.params['data'])

    try:
        Lesson.objects.create(course_id=data['course_id'],
                          desc=data['desc'],
                          starttime=data['starttime'],
                          endtime=data['endtime'])
    except Exception,e:
        return JsonResponse({'retcode':2, 'reason':str(e)})

    return JsonResponse({'retcode': 0})

def delete_lesson(request):
    rid = request.params['id']
    try:
        Lesson.objects.filter(id=rid).delete()
    except Exception,e:
        return JsonResponse({'retcode':2, 'reason':str(e)})

    return JsonResponse({'retcode': 0})

def modify_lesson(request):


    record = Lesson.objects.get(id=request.params['id'])

    # 由于是json编码，这里需要解码为对象
    newdata = json.loads(request.params['newdata'])
    record.course_id = newdata['course_id']

    record.starttime = newdata['starttime']
    record.endtime = newdata['endtime']
    record.desc = newdata['desc']

    record.save()


    return JsonResponse({'retcode': 0})

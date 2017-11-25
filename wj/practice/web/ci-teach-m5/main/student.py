# coding=utf8

from django.http import HttpResponse, JsonResponse, QueryDict

from models import Lesson,StudentCheckin
from django.db.models import F
from django.db import  IntegrityError
from django.core.paginator import Paginator, EmptyPage
import json
from django.utils.dateparse import parse_datetime
from django.utils import timezone

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
    if action == 'list_ci_lesson':
        return list_ci_lesson(request)
    elif action == 'checkin_lesson':
        return checkin_lesson(request)
    else:
        return JsonResponse({'retcode': 1, 'err': u'action not supported'})


from datetime import datetime,timedelta
def list_ci_lesson(request):
    pagenum = 1
    pagesize = 100

    # datetime  now 返回的是当前日期时间
    curTime = timezone.now()
    begin = curTime - timedelta(minutes=30)
    end = curTime + timedelta(minutes=10)


    qs = Lesson.objects.filter(starttime__gte=begin,
                               starttime__lte=end)\
        .select_related('course')\
        .annotate(course_name=F('course__name'))\
        .values('id','course_id','course_name','starttime','endtime',
                   'desc').order_by('-id')

    pgnt = Paginator(qs, pagesize)

    retObj = list(pgnt.page(pagenum))


    return JsonResponse({'retcode': 0, 'retlist': retObj, 'total': pgnt.count})




def checkin_lesson(request):
    lessonid = request.params['lessonid']

    try:
        StudentCheckin.objects.create(
            student_id=request.user.id,  # 用户id 在request.user.id
            lesson_id=lessonid
        )
    except IntegrityError:
        return JsonResponse({'retcode': 2, 'reason': u'该课已经签到过了'})


    return JsonResponse({'retcode': 0})

# coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import engines

tmplt = u'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>课程信息</title>
</head>
<body>

<form method='POST'>
  <fieldset>
    <legend>添加课程信息:</legend>
    课程名  :  <input type="text"   name="name" value=""><br><br>
    课程描述 :  <textarea    name="desc" value="" ></textarea><br><br>
    显示次序 :  <input type="number"  name="displayidx" value="1"><br><br>
    <input type="submit" value="提交">
  </fieldset>
</form>



<br>
<h2>现有课程</h2>
<table border="1">

<th>课程名</th>
<th>课程描述</th>
<th>显示次序</th>

{% for one in courseList %}
    <tr>
    <td>{{ one.name }}</td>
    <td>{{ one.desc }}</td>
    <td>{{ one.display_idx }}</td>
    </tr>
{% endfor %}


</table>
</body>
</html>
'''

django_engine = engines['django']
template = django_engine.from_string(tmplt)

from models import Course
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def showadd_course(request):

    # 添加课程信息
    # if 'name' in request.GET:
    #     name       = request.GET['name']
    #     desc       = request.GET['desc']
    #     displayidx = request.GET['displayidx']

    if 'name' in request.POST:
        name = request.POST['name']
        desc = request.POST['desc']
        displayidx = request.POST['displayidx']

        #
        # course = Course(name=name,desc=desc,display_idx=displayidx)
        # course.save()
        #
        c = Course.objects.create(name=name,desc=desc,display_idx=displayidx)
        print 'added2'

    courseList = Course.objects.filter(display_idx__gte=2)
    # courseList = Course.objects.all().filter(name__contains=u"语")
    print courseList

    ret = template.render({'courseList': courseList})
    return HttpResponse(ret)
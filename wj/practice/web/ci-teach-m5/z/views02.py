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

<form >
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


def showadd_course(request):
    studentList = []

    ret = template.render({'studentList': studentList})
    return HttpResponse(ret)
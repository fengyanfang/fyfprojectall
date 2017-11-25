# coding=utf8
from django.shortcuts import render


from django.http import HttpResponse

studentTable = {
    'zhangsan':{
        'loginname' : 'zhangsan',
        'name':u'张三3',
        'age': 16
    },
    'lisi':{
        'loginname' : 'lisi',
        'name':u'李四2',
        'age': 18
    },
    'wanger':{
        'loginname' : 'wanger',
        'name':u'王二',
        'age': 16
    },
    'xuda':{
        'loginname' : 'xuda',
        'name':u'许达',
        'age': 16
    },
}

def show_all_students(request):
    allName = [one['name'] for one in studentTable.values()]

    response = u'''
    <!DOCTYPE html>
    <html><head><meta charset="UTF-8"></head>
    <body>%s</body></html>
    ''' % u'  '.join(allName)

    return HttpResponse(response)




def show_all_students2(request):
    response2 = u'''
    <!DOCTYPE html>
    <html><head><meta charset="UTF-8"></head>
    <body>张三，李四</body></html>
    '''
    return HttpResponse(response2)


def check_exist(request):
    print request.GET
    loginname = request.GET['loginname']
    age  = int(request.GET['age'])
    if loginname not in studentTable:
        return HttpResponse(u'没有这个学生')

    student = studentTable[loginname]
    if student['age'] != age:
        return HttpResponse(u'没有这个学生')

    return HttpResponse(u'有这个学生')


tmplt = u'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>学生信息</title>
</head>
<body>

<form >
  <fieldset>
    <legend>添加学生信息:</legend>
    登录名  :  <input type="text"   name="loginname" value=""><br><br>
    真实姓名:  <input type="text"    name="name" value=""><br><br>
    年龄    :  <input type="number"  name="age" value="18"><br><br>
    <input type="submit" value="提交">
  </fieldset>
</form>



<br>
<h2>现有学生</h2>
<table border="1">

<th>学生登录名</th>
<th>真实姓名</th>
<th>年龄</th>

%s

</table>



</body>
</html>
'''
def showadd(request):

    if 'loginname' in request.GET:
        loginname = request.GET['loginname']
        name = request.GET['name']
        age = int(request.GET['age'])

        studentTable[loginname] = {
            'loginname':loginname,
            'name':name,
            'age':age,
        }


    onehtmlstu = u'<tr><td>{}</td><td>{}</td><td>{}</td></tr>'
    liststudents = [onehtmlstu.format(one['loginname'],
                                     one['name'],
                                     one['age']) \
                   for one in studentTable.values()]

    allhtmlstus = ''.join(liststudents)
    return HttpResponse(tmplt% allhtmlstus)



# tmplt2 = u'''
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>学生信息</title>
# </head>
# <body>
#
# <form >
#   <fieldset>
#     <legend>添加学生信息:</legend>
#     登录名  :  <input type="text"   name="loginname" value=""><br><br>
#     真实姓名:  <input type="text"    name="name" value=""><br><br>
#     年龄    :  <input type="number"  name="age" value="18"><br><br>
#     <input type="submit" value="提交">
#   </fieldset>
# </form>
#
#
#
# <br>
# <h2>现有学生555</h2>
# <table border="1">
#
# <th>学生登录名</th>
# <th>真实姓名</th>
# <th>年龄</th>
#
# {% for one in studentList %}
#     <tr>
#     <td>{{ one.loginname }}</td>
#     <td>{{ one.name }}</td>
#     <td>{{ one.age }}</td>
#     </tr>
#
# {% endfor %}
#
#
# </table>
#
#
#
# </body>
# </html>
# '''
#
# from django.template import engines
# django_engine = engines['django']
# template = django_engine.from_string(tmplt2)
#
# def showadd(request):
#     ret = template.render({'studentList':studentTable.values()})
#     return HttpResponse(ret)
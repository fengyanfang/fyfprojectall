# coding=utf8
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.


# 课程
class Course(models.Model):
    # 课程名
    name = models.CharField(max_length=100)
    # 课程描述
    desc = models.CharField(max_length=1000, null=True, blank=True)
    # 展示优先级
    display_idx = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "main_course"


# 课时表
class Lesson(models.Model):
    course = models.ForeignKey(Course, blank=False,on_delete=models.PROTECT)
    # 有哪些课
    starttime = models.DateTimeField()
    endtime   = models.DateTimeField()

    desc = models.CharField(max_length=1500, null=True, blank=True)

    class Meta:
        db_table = "main_lesson"






from datetime import  datetime
# 学生签到记录
class StudentCheckin(models.Model):
    student = models.ForeignKey(User, related_name='student_checkin')
    # 课时
    lesson = models.ForeignKey(Lesson,  related_name='checkin_students')
    # 签到时间,缺省值为当前时间
    checkintime = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "main_student_checkin"
        #
        unique_together = (("student", "lesson"),)









class City(models.Model):
    name = models.CharField(max_length=50)
    toursites = models.CharField(max_length=80)

    class Meta:
        db_table = "zzz_city"

class IdCard(models.Model):
    peoplename = models.CharField(max_length=50)
    idnumber = models.CharField(max_length=80)

    class Meta:
        db_table = "zzz_idcard"

class People(models.Model):
    name = models.CharField(max_length=80)
    borncity = models.ForeignKey(City, related_name='born_people')
    idcard = models.OneToOneField(IdCard, related_name='to_people')
    # ManyToManyField 会产生一张新表
    visitedcity = models.ManyToManyField(City,
                                         db_table='zzz_peoplevisitcity',
                                         related_name='visited_people')

    class Meta:
        db_table = "zzz_people"



# coding=utf8
from __future__ import unicode_literals

from django.db import models

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
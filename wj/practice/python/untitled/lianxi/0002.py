#coding:utf-8
import sys
def student():

    a=raw_input('please enter your name and age(for example:Mary,24): ')
    a= a.split(";")

    for one in a:
        # 防止有多余的符号影响
        if one.count(",") != 1:
            continue
        name, age = one.split(",")
        name = name.strip()
        age = age.strip()
        print '%-20s:%02s;' %(name,age)
        print sys.stdin.encoding



student()

with open('records/course.txt') as f :
    courses = f.read().decode('utf8').splitlines()[1:]

with open('records/teacher.txt') as f :
    teachers = f.read().decode('utf8').splitlines()[1:]

courseDict = {}

for course in courses:
    if not course.strip():
        continue

    parts = course.split(';')
    courseId = parts[0]
    courseName = parts[1]
    courseDict[courseId] = courseName

teacherDict = {}
for teacher in teachers:
    if not teacher.strip():
        continue

    parts = teacher.split(';')
    teacherId = parts[0]
    teacherName = parts[4]
    teacherDict[teacherId] = teacherName


with open('records/teacher_course.txt') as f :
    teacher_courses = f.read().splitlines()[1:]



with open('ret.txt','w') as f :
    for tc in teacher_courses:
        if not tc.strip():
            continue

        parts = tc.split(';')
        teacherId = parts[0]
        courseId = parts[1]

        if (teacherId not in teacherDict) or (courseId not in courseDict):
            print 'skip record {}'.format(tc)

        ret = u"{:10} : {}".format(teacherDict[teacherId],courseDict[courseId])

        print ret

        f.write(ret.encode('utf8')+'\n')



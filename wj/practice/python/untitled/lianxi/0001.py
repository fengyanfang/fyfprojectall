def gname(a):
    print a.split(',')[1].split(' ')[4]

c="A girl  come in, the name is Jack, level 955"
a="A old lady come in, the name is Mary, level 94454"
b="A pretty boy come in, the name is Patrick, level 194"

gname(b)


def getName(a):
    s = a.find('is')
    e = a.find('level')
    print a[s+3:e-2]

    a="A girl  come in, the name is Jack, level 955"
getName(a)

list=[2,6,8,3,5,34,23,56,17,19,24]

def num(list):
    newlist = []
    for i in range(len(list)):
        m = min(list)
        newlist.append(m)
        list.remove(m)

    print newlist

num(list)
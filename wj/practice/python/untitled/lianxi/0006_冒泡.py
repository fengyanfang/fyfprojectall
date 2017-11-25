a = [2,6,4,8,23,3,5,26,12,15]

def bubble(ilist):
    for j in range(len(ilist)-1,0,-1):
        for i in range(0,j):
            if ilist[i] > ilist[i+1]:
                ilist[i],ilist[i+1] = ilist[i+1],ilist[i]

    print ilist


bubble(a)
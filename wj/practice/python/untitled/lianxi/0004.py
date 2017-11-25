# coding = utf-8

def salary():
    with open("C:/classes/file1.txt","r+") as fp:
        f = fp.readlines()
        tax = []
        income = []
        name = []
        salary1 = []

        for i in f:
            i = i.strip('')
            i = i.split(';')
            salary1.append(i[1])
        for i in f:
            i = i.strip()
            i = i.split(';')
            name.append(i[0])

        name2 = []
        for n in name:
            n= n.strip()
            n = n.split(":")
            name2.append(n[1])

        salary2 = []
        for j in salary1:
            j = j.strip()
            j = j.split(':')
            salary2.append(int(j[1]))

        tax = [one*0.1 for one in salary2]
        incom = [one*0.9 for one in salary2]

        with open("C:/classes/a.txt","w+") as sp:
            for i in range(len(name)):
                sp.write( "%-5s:%10s; salary:%10s; tax:%10s; incom:%10s\n" %("name",name2[i],salary2[i],int(tax[i]),int(incom[i])))



salary()
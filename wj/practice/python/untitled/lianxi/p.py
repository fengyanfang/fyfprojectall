
def putInfoToDict(fileName):
    with open(fileName, "r+") as fp:
        f = fp.readlines()

        id_list = []
        lesson_id_list = []
        time_list = []
        info_list = []
        f_list = []

        for mess in f:

            mess = mess[2:-3]
            mess = mess.split(",")
            f_list.append(mess)
        print f_list

        for i in range(len(f_list)):
            if f_list.count(f_list[i][2]) > 1:
                print  f_list[i][2]



putInfoToDict("C:/classes/0005_1.txt")
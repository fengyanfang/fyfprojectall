# coding=utf-8
import xlrd,xlwt
#打开文件
workbook = xlrd.open_workbook('c:/classes/quhao.xls')
#通过索引获取工作表
table = workbook.sheets()[0]
# table = workbook.sheet_by_index(0)
nrows = table.nrows  #行数
ncols = table.ncols  #列数

# 获取整行和整列的值
row1 = table.row_values(0)
# for row in range(ncols):
#     print table.row_values(row)[1:19]

col1 = table.col_values(2)
# 获取单元格内容(第一行，第一列)
cell_value = table.cell_value(2,7)
# print row1[1]

#写入文件
wb = xlwt.Workbook()
infolist = []
for i in range(nrows):
   row =  table.row_values(i)
   infolist.append(row)
sheet7 = wb.add_sheet("sheet7",cell_overwrite_ok=True)
hebei = []
row2_12 = infolist[1:12]
for i in row2_12:
    i = i[:2]
    hebei.append(i)

row_count = len(hebei)
col_count = len(hebei[0])
for ro in range(0, row_count):
    col_cout = len(hebei[ro])
    for col in range(0, col_count):
        if ro == 0:
            sheet7.write(ro, col,hebei[ro][col])
        else:
            sheet7.write(ro, col,hebei[ro][col])
wb.save("c:/classes/fen.xls")






    # for col in range(12):
    #     if col%2 != 0:
    #         sheet.write(0,1,row1[col])
    #         workbook2.save("c:/classes/fen.xls")
    #     else:
    #         sheet.write(0,0,row1[col])
    #         workbook2.save("c:/classes/fen.xls")

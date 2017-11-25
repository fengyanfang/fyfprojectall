# coding=utf8

#打开中文的文件名一定要用unicode。
with open(u'cfiles/gbk编码.txt') as f1, open(u'cfiles/utf8编码.txt') as f2:
    # 根据不同的编码格式，对内容进行解码
    content1 = f1.read().decode('gbk')
    content2 = f2.read().decode('utf8')

    # 要合并内容，必须先都转化成unicode，再合并
    newContent = content1 + content2

    print newContent

print u'请输入新文件的名称:',
newFile = raw_input()

# 用户输入的内容的编码方式，和代码的运行环境有关， 如果是dos命令行执行 得到的是gbk编码
uNewFile = newFile.decode('utf8')

with open(uNewFile,'w') as f:
    f.write(newContent.encode('utf8'))



    

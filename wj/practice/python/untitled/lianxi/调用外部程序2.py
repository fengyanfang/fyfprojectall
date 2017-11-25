from subprocess import Popen,PIPE

# ret = subprocess.check_output('dir',shell=True)
# print ret.decode("gbk") #可以得到输出结果，只有被调用程序退出，才返回

# pooen方法不会阻塞程序,可以手动用来控制输入输出
process = Popen(
    args="mspaint",
    stdin=PIPE,
    stdout=PIPE,
    stderr=PIPE,
    shell=True
)
listi = [2,23,5,4]
output,err = process.communicate("\n".join(listi)) #communicate 程序把输入连接起来传进去，并把程序结束
print output

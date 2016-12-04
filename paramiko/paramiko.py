__author__ = 'Administrator'
#-*-coding:utf-8-*-
import sys,paramiko

host = sys.argv[1] #定义一个ip地址，例如：paramiko 192.168.1.254
#为什么是sys.argv[1]而不是sys.argv[0]呢？
#答：sys.argv[0]在shell中位置参数为第一位，表示程序本身，例如：执行./paramiko 192.168.1.254 ifconfig 其中，paramiko本身占用一个位置参数
user = 'user'
password = 'xiaofei'
cmd = sys.argv[2] #定义远程执行命令
s = paramiko.SSHClient() #绑定连接实例对象
s.load_system_host_keys() #加载本机HOST主机文件
s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #
s.connect(host,22,user,password,timeout=5)  #连接远程主机（目标ip地址、端口号、用户名、密码、超时时间）
stdin,stdout,stderr = s.exec_command(cmd) #执行命令,反馈一个元组（stdin输入信息，stdout输出信息，stderr错误信息）
cmd_result = stdout.read(),stderr.read() #读取命令结果

for line in cmd_result:
    print line #循环打印信息

s.close()
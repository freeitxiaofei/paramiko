__author__ = 'Administrator'
#通过SSH协议中的SFTP协议传输文件
import sys,paramiko
host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]

t = paramiko.Transport((host,22)) #创建传输实例对象
t.connect(username=user,password=password) #连接对象账户名和密码

#上面是账户名和密码认证，下面代码实现RSA认证
#pulic_key_file = '/home/root/.ssh/id.rsa'
#key = paramiko.RSAKey.from_private_key_file(public_key_file)
#t.connect(username=user,pkey=key)

sftp = paramiko.SFTPClient.from_transport(t) #创建SFTP客户端实例，连接信息来自‘t’实例对象
sftp.get('/tmp/file.py','file1.py') #上传功能
sftp.put('/tmp/file.py') #下载功能
t.close() #结束后取消连接
import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 允许连接不在know_hosts文件中的主机

private_key = paramiko.RSAKey.from_private_key_file("../.ssh/id_rsa")
ssh.connect("192.168.8.1",2222,"admin", pkey=private_key)

execmd = 'pwd' #需要输入的命令

stdin, stdout, stderr = ssh.exec_command (execmd)

print(stdout.read())

ssh.close()
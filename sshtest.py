import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 允许连接不在know_hosts文件中的主机

ssh.connect("127.0.0.1",22,"root", "stdx+2022")

execmd = 'ls -alh' #需要输入的命令

stdin, stdout, stderr = ssh.exec_command (execmd)

print(stdout.read())

ssh.close()
import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 允许连接不在know_hosts文件中的主机

ssh.connect("192.168.8.1",2222,"admin", "asuaadmin")

execmd = 'pwd' #需要输入的命令

stdin, stdout, stderr = ssh.exec_command (execmd)

print(stdout.read())

ssh.close()
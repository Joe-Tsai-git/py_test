from netmiko import ConnectHandler
from textfsm import TextFSM
from pprint import pprint

connection_info = {'device_type':'huawei',
      'ip':'10.0.2.32',
      'username':'admin',
      'password':'python123'}

with ConnectHandler(**connection_info) as conn:
    #output = conn.send_command("display interface brief", use_textfsm=True)
    output = conn.send_command("display bgp vpnv4 all routi 6.6.6.6", use_textfsm=True)

#print(output)
pprint(output)
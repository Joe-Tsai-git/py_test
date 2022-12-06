import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
group1 = nr.filter(F(groups__contains="huawei_group3"))
#results = nr.run(netmiko_send_command, command_string='disp ip int bri', use_textfsm=True)
#for result in results:
##    ipdb.set_trace()
#    for iface in results[result].result:
##        ipdb.set_trace()
#        if iface["status"]=='up':
#            print(f'{iface["intf"]} is up! IP address: {iface["ipaddr"]}')
out = group1.run(netmiko_send_command, command_string='disp ip int bri', use_genie=True)
for name, details in out.items():
    ipdb.set_trace()
    print(f"{name}")
    for iface in details.result:
        if iface["status"]=='up':
            print(f'{iface["intf"]} is up! IP address: {iface["ipaddr"]}')
#    print(f"- Status: {details.get('enabled', None)}")
#    print(f"- Physical address: {details.get('phys_address', None)}")
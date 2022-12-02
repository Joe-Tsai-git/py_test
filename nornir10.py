import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
results = nr.run(netmiko_send_command, command_string='sh ip int bri', use_textfsm=True)
for result in results:
#    ipdb.set_trace()
    for iface in results[result].result:
#        ipdb.set_trace()
        if iface["status"]=='up':
            print(f'{iface["intf"]} is up! IP address: {iface["ipaddr"]}')
#print_result(results)
import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
results = nr.run(netmiko_send_command, command_string='sh int switchport', use_textfsm=True)
print_result(results)
print(results['SW2'].result[3]['mode'])
#ipdb.set_trace()
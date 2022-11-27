from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
#sw4 = nr.filter(filter_func=lambda host: host.name=='SW4')
switches = ['SW1','SW2','SW3']
sw_multi = nr.filter(filter_func=lambda host: host.name in switches)
results = sw_multi.run(netmiko_send_command, command_string='sh ip arp')

print_result(results)
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result, print_title

nr = InitNornir(config_file="config.yaml")
#sw4 = nr.filter(filter_func=lambda host: host.name=='SW4')
def config(cisco): #here "cisco" is a context, can be taken place by "task" or "task_context"
    cisco.run(task=netmiko_send_config, config_file='commands.cfg')  #here the "task" mask be exect as "task", no task_context
    cisco.run(task=netmiko_send_command, command_string='show vlan bri')
print_title('Configuring vlan 999')
results=nr.run(task=config)

print_result(results)
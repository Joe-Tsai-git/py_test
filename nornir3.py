from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
group1=nr.filter(F(groups__contains="cisco_group1"))
group2=nr.filter(~F(groups__contains="cisco_group1"))
group3=nr.filter(F(groups__contains="huawei_group3"))
results = group3.run(netmiko_send_command, command_string='disp ip int brief')
#from nornir.core.filter import F_BASE
print_result(results)
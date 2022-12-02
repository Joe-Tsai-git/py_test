#import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
#ipdb.set_trace()
def host_parm(task):
    return(task.host.name,
        task.host.hostname,
        task.host.platform)
result = nr.run(task=host_parm)
print_result(result)
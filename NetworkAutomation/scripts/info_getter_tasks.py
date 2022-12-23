from netmiko import Netmiko
from nornir_netmiko.tasks import netmiko_send_command
from cmdb.models import Interface, Device

show_intf_cmd_maping = {
    'cisco_ios':'show interface',
    'cisco':'show interface',
}
def update_intfs_task(task, save=True):
    device_type = task.host.platform
    device_obj = Device.objects.get(ip=task.host.hostname)

    cmd = show_intf_cmd_maping.get(device_type)
    if not cmd:
        raise Exception('不支持的设备')

    intfs = task.run(netmiko_send_command, command_string=cmd, use_textfsm=True).result

    if save:
        for intf in intfs:
            try:
                obj, created = Interface.objects.update_or_create(
                    name=intf['interface'], device=device_obj,
                    defaults=dict(name=intf['interface'],
                    desc=intf['description'], device=device_obj)
                )
                print(obj, created)
            except Exception as e:
                print(e)

if __name__=='__main__':
    ...
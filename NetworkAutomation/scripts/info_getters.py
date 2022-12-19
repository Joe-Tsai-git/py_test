from netmiko import Netmiko

show_intf_cmd_maping = {
    'cisco_ios':'show interface',
    'cisco':'show interface',
}
def ssh_device_2_get_intf(device_type,host,username,password,secret='',port=22):
    dev_info = {
        'device_type':device_type,
        'host': host, 
        'username':username,
        'password':password,
        'port':port,
        'secret':secret,
    }

    cmd = show_intf_cmd_maping.get(device_type)
    if not cmd:
        raise Exception('不支持的设备')
    
    with Netmiko(**dev_info) as net_conn:
        output = net_conn.send_command(cmd, use_textfsm=True)
        return output
#        print(output)

if __name__=='__main__':
    dev_info = {
        'device_type':'cisco_ios',
        'host': '10.0.2.27', 
        'username':'python',
        'password':'123',
        'port':22,
        'secret':'123',
    } 
    ssh_device_2_get_intf(**dev_info)


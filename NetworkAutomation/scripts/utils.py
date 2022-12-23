from cmdb.models import Device
from nornir import InitNornir

def get_nornir_obj(queryset=None):
    if not queryset:
        devs = Device.objects.all()
    else:
        devs = queryset

    devs_data = []
    for dev in devs:
        devs_data.append(
            {
                'name':dev.name,
                'hostname': dev.ip, 
                'platform': dev.platform,
                'port': 22,
                'username':dev.username,
                'password':dev.password,
                'netmiko_secret':dev.secret,
            }
        )
    runner= {
        "plugin":"threaded",
        "options": {
            "num_workers": 100,
        },
    }
    inventory = {
        "plugin": "FlatDataInventory",
        "options": {
            "data":devs_data,
        },
    }

    nr = InitNornir(runner=runner, inventory=inventory)
    return nr

if __name__ == '__main__':
    ...

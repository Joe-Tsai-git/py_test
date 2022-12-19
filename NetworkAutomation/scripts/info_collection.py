import os
import sys
from pathlib import Path

bASE_DIR = Path(__file__).parent.parent.as_posix()
#print(bASE_DIR)
#print(sys.path)
#sys.path.append(Path(__file__).parent)

import django
#parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
#print(parentdir)
#sys.path.insert(0,parentdir)  
sys.path.insert(0, bASE_DIR)
#print(sys.path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NetworkAutomation.settings')
#print(os.environ)
django.setup()

from cmdb.models import Interface, Device
from scripts.info_getters import ssh_device_2_get_intf

def collect_intfs():
    devs = Device.objects.all()

    for dev in devs:
        print(dev)
        dev_info = {
            'device_type':dev.platform,
            'host': dev.ip, 
            'username':dev.username,
            'password':dev.password,
            'port':dev.port,
            'secret':dev.secret,
        }

        intfs = ssh_device_2_get_intf(**dev_info)
        for intf in intfs:
            try:
                obj, created = Interface.objects.update_or_create(
                    defaults=dict(name=intf['interface'], desc=intf['description'], device=dev),
                    device=dev, name=intf['interface']
                )
                print(obj, created)
            except Exception as e:
                print(e)

    
if __name__ == '__main__':
    collect_intfs()

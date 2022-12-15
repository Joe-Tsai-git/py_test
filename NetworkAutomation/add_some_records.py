import os
import sys
import django
from pathlib import Path

BASE_DIR = Path(__file__).parent
sys.path.append(BASE_DIR)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NetworkAutomation.settings')
django.setup()

if __name__ == '__main__':
    from cmdb.models import Device
#    #增加
#    dev = Device(
#        ip='192.168.1.3',
#        name='dev03',
#        sn='11111113',
#        vendor='huawei',
#        is_virtual=False,
#        group='0',
#    )
#    dev.save()
#    print(dev.name, dev.ip, dev.vendor)
    #查询所有行
    # devs = Device.objects.all()
    # for dev in devs:
    #     print(dev)
    #查询指定行
    devs = Device.objects.filter(name='dev01')
    for dev in devs:
        print(dev)
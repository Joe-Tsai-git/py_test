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
    # #增加
    # dev = Device(
    #     ip='10.0.2.21',
    #     name='SW1',
    #     vendor='cisco',
    #     platform='cisco_ios'
    # )
    # dev.save()
    # print(dev.name, dev.ip, dev.vendor)
    #查询所有行
    # devs = Device.objects.all()
    # for dev in devs:
    #     print(dev)
    #查询指定行
    devs = Device.objects.filter(name='SW1')
    for dev in devs:
        print(dev)
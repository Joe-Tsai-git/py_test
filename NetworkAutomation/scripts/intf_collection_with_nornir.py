# import os
# import sys
# from pathlib import Path

# bASE_DIR = Path(__file__).parent.parent.as_posix()

# import django
# sys.path.insert(0, bASE_DIR)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NetworkAutomation.settings')
# django.setup()

from cmdb.models import Device
from nornir import InitNornir

from scripts.info_getter_tasks import update_intfs_task
from nornir_utils.plugins.functions import print_result
from scripts.utils import get_nornir_obj

def collect_intfs(queryset=None):
    nr = get_nornir_obj(queryset)
    result = nr.run(update_intfs_task)
    print_result(result)

if __name__ == '__main__':
    collect_intfs()
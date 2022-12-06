from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result 
from nornir_utils.plugins.tasks.files import write_file
from datetime import date
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
#group1 = nr.filter(F(groups__contains="cisco_group1"))
group1 = nr.filter(F(groups__contains="huawei_group3"))
def backup_configurations(cisco): #here "cisco" is a context, can be taken place by "task" or "task_context"
    r=cisco.run(task=napalm_get, getters=["config"])
    cisco.run(task=write_file, content=r.result["config"]["running"], filename=str(cisco.host.name)+"-"+str(date.today())+".txt")

results=group1.run(name="Backing up SW's configuration", task=backup_configurations)

print_result(results)
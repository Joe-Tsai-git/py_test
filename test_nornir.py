from nornir import InitNornir
nr = InitNornir(
    config_file="nornir.yaml"
    )
# list hosts
print(nr.inventory.hosts)
{'dev01': Host: dev01, 'dev02': Host: dev02, 'dev03': Host: dev03}
import sys
import textfsm
from tabulate import tabulate

with open('templateM') as f, open('disp_bgp_vpnv4_all_routi_addr') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(tabulate(result, headers=header))
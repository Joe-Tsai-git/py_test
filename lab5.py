import sys
import textfsm
from tabulate import tabulate
import ipdb

with open('template') as f, open('output_from_cli.txt') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    
    print(tabulate(result, headers=header))
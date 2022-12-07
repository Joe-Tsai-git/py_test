import sys
import textfsm
from tabulate import tabulate

with open('templateM') as f, open('test_textfsm_output') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(result[0][1])    
#    print(tabulate(result, headers=header))
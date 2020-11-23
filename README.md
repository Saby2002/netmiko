In [4]: quit()
eve@Linux-Desktop:~/datastructure$ vim netmiko_arp.py 
eve@Linux-Desktop:~/datastructure$ ipython3 -i netmiko_arp.py 
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
[{'config_register': '0x0',
  'hardware': ['IOSv'],
  'hostname': 'R2',
  'mac': [],
  'reload_reason': 'Unknown reason',
  'rommon': 'Bootstrap',
  'running_image': '/vios-adventerprisek9-m',
  'serial': ['9HY92NK0VBG0BWORB5SBV'],
  'uptime': '3 days, 11 hours, 44 minutes',
  'version': '15.
In [2]: len(output)
Out[2]: 1

In [3]: for version in output:
   ...:     print('#'*80)
   ...:     print(version['hardware'])
   ...:     print(version['hostname'])
   ...:     break
   ...: 
################################################################################
['IOSv']
R2

In [4]: for version in output:
   ...:     print('#'*80)
   ...:     print(version['hardware'])
   ...:     print(version['hostname'])
   ...:     print('#'*80)
   ...:     break
   ...: 
   ...: 
################################################################################
['IOSv']
R2
#####

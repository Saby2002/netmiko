Why we need YAML or JSON?

 

When transfering our program from one computer to another, we need to convert these into bytes and this process is know as process of serilization.

Taking the things inside of the program serilzing them into a stream of bytes, either to be written into a file or written across the network.

 

This can be done in a standardize way. YAML and JSON are the two serilization protocol. The two well know protocol is YAML and JSON.

What would be the trade of between YAML and JSON.

JSON is generally good when doing compture to computer communication.

Its basically the payload of the API.

Lot of web application transfering JSON. As a payload for the data.

Its also good for the networking device.

Arita API passed JSON data. NXOS transfers JSON data.

JSON is good for computer to computer interaction.

YAML is a superset of JSON

Things like Ansible, Salt when using YAML to create Inventory

eve@Linux-Desktop:~/netmiko/YAML$ 
eve@Linux-Desktop:~/netmiko/YAML$ apt install yaml
E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
eve@Linux-Desktop:~/netmiko/YAML$ sudo apt install yaml
[sudo] password for eve: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package yaml
eve@Linux-Desktop:~/netmiko/YAML$ vim read_yaml.py
eve@Linux-Desktop:~/netmiko/YAML$ python3 read_yaml.py 
Enter Filename: test1.yaml
read_yaml.py:5: YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.
  yaml_out = yaml.load(f)
['router1', 'router2', 'router3', 'router4']
eve@Linux-Desktop:~/netmiko/YAML$ ipython3 -i read_yaml.py 
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
Enter Filename: test1.yaml
read_yaml.py:5: YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.
  yaml_out = yaml.load(f)
['router1', 'router2', 'router3', 'router4']

In [1]: dir()
Out[1]: 
['In',
 'Out',
 '_',
 '__',
 '___',
 '__builtin__',
 '__builtins__',
 '__doc__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_dh',
 '_i',
 '_i1',
 '_ih',
 '_ii',
 '_iii',
 '_oh',
 '_sh',
 'exit',
 'f',
 'filename',
 'get_ipython',
 'quit',
 'yaml',
 'yaml_out']

In [2]: yaml_out
Out[2]: ['router1', 'router2', 'router3', 'router4']

In [3]: yaml
Out[3]: <module 'yaml' from '/home/eve/.local/lib/python3.6/site-packages/yaml/__init__.py'>

In [4]: yaml_out[0]
Out[4]: 'router1'

In [5]: yaml_out[1]
Out[5]: 'router2'

Multiple lines chart use by having '|' charterter.
Also '>' can be used for multiple lines
YAML has a expanded format and a condensed format. 
 

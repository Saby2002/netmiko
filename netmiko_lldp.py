from netmiko import ConnectHandler
from datetime import datetime
from pprint import pprint


device1 = {
        "hosts": "172.29.129.1",
        "username": "saby",
        "password": "lab123",
        "device_type": "cisco_xr",
}

device2 = {
        "host": "172.29.129.2",
        "username": "lab",
        "password": "lab123",
        "device_type": "cisco_ios",
}

device3 = {
        "hosts": "172.29.129.5",
        "username": "lab",
        "password": "lab123",
        "device_type": "cisco_ios",
}



net_connect = ConnectHandler(**device2)
cmds = ["show lldp neighbors detail"]
for cmd in cmds:
    output = net_connect.send_command(cmd, use_textfsm=True)
    print(output)
   

print()


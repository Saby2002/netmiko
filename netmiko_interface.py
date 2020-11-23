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


vendors = [device2]

for device in vendors:
    net_connect = ConnectHandler(**device)
    cmds = ["show interfaces"]
    for cmd in cmds:
        output = net_connect.send_command(cmd, use_textfsm=True)
        
        
        
        pprint(output)
        
        
        print()

        if cmd == "show lldp neighbors":
            print("LLDP Date Structure Type : {}".format(type(output)))

print()


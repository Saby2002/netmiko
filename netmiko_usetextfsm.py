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
    pprint(device)
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    cmds = ["show arp", "show version", "show lldp neighbors detail"]
    for cmd in cmds:
        output = net_connect.send_command(cmd, use_textfsm=True)
        print('#' *80)
        print(cmd)
        print('#' *80)
        pprint(output)
        print('#' *80)
        
        print()

        if cmd == "show lldp neighbors":
            print("LLDP Date Structure Type : {}".format(type(output)))

print()


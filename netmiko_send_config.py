from netmiko import ConnectHandler

device1 = {
        "host": "172.29.129.2",
        "username": "lab",
        "password": "lab123",
        "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

cfg = [
    'int g0/3',
    'ip address 10.1.3.1 255.255.255.0',
    'no shut',
    'int g0/1',
    'ip address 10.1.2.1 255.255.255.0',
    'no shut',
    'int lo0',
    'ip address 2.2.2.2 255.255.255.255',
]

output = net_connect.send_config_set(cfg)
print(output)

output_interface = net_connect.send_command('show ip int br', use_textfsm=True)
print(output_interface)



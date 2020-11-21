from netmiko import ConnectHandler

device1 = {
        "host": "172.29.129.5",
        "username": "lab",
        "password": "lab123",
        "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_config_from_file(config_file='ios2.txt')
print(output)

output_interface = net_connect.send_command('show ip int br', use_textfsm=True)
print(output_interface)



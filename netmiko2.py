from netmiko import ConnectHandler

device1 = {
        "host": "172.29.129.1",
        "username": "saby",
        "password": "lab123",
        "device_type": "cisco_xr",
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show arp", expect_string=r'#')
print(output)


net_connect1 = ConnectHandler(**device1)
output_arp = net_connect1.send_command("show ip int br", expect_string=r'#')
print(output_arp)


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

save_config = net_connect.save_config()
print(save_config)



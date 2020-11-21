"""
In the lab environment use Netmiko to connect to one of the Cisco XR, device.  Simply print the router prompt back from this device to verify you are connecting to the device properly. 

Add second device SROS to your script. Make sure you are using dictionaries to represent the two IOS router devices. Additionally use a for loop to accomplish the Netmiko connection creation. Once again print the prompt back from the device that you connected to. 

For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrive 'show version'.
Save the output to  a file the current working directory. 
"""

from netmiko import ConnectHandler
from datetime import datetime

R1 = {
        "host": "172.29.129.1",
        "device_type": "cisco_xr",
        "username": "saby",
        "password": "lab123",
}

R2 = {
        "host": "172.29.129.2",
        "device_type": "cisco_ios",
        "username": "lab",
        "password": "lab123",
}

R5 = {
        "host": "172.29.129.5",
        "device_type": "cisco_ios",
        "username": "lab",
        "password": "lab123",
}

R6 = {
        "host": "172.29.129.6",
        "device_type": "nokia_sros",
        "username": "admin",
        "password": "admin",
}

all_device = [R1, R2, R5]

start_time = datetime.now()

for a_device in all_device:
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("show version")
    print(f"\n\n------ Device {a_device['device_type']}------")
    print(output)
    print("--------------END----------------")
    with open("show_version.txt", "w") as f:
        f.write(output)

end_time = datetime.now()
total_time = end_time - start_time




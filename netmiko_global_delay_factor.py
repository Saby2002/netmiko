"""
Create a Netmiko connection to cisco device using a global_delay_factor of 2.
Execute "show lldp neighbors" and print the returned output to standard output. Execute "show lldp neighbors details" second time using send_command() with a delay_factor of 8. 
Print the output of this command to standard output. 
Use the python datetime lib to record the execution time of both these commands. Print these times to a standard output. 
"""

from netmiko import ConnectHandler
from datetime import datetime

device = {
        "device_type": "cisco_ios",
        "host" : "172.29.129.2",
        "username": "lab",
        "password": "lab123",
       # "global_delay_factor": 2,
}

net_connect = ConnectHandler(**device)

cmd = "show lldp neigh detail"
start_time = datetime.now()

output = net_connect.send_command(cmd, delay_factor=8)
end_time = datetime.now()
print('#' *80)
print(output)
print('#' *80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()




"""
Use the extended 'ping' command and Netmiko on the 'cisco4' router. This should prompt you for additional information as follows :

cisco4# ping
protocol[ip]:
Target IP address : 172.29.129.151
Repeat Count [5] :
Datagram Size[100]:
Timeout in seconds [2]:
Extended commands [n]:
Sweep range of sizes [n]:
Sending 5, 100-bytes ICMP Echos to 172.29.129.151, timeout is 2 seconds:
!!!!!
Success rate is 100 percent(5/5), round-trip min/avg/max = 1/1/4 ms

b) Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'

"""
from netmiko import ConnectHandler

device = {
        "device_type": "cisco_ios",
        "host": "172.29.129.2",
        "username": "lab",
        "password": "lab123",
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command(
        "ping vrf MGMT", expect_string=r"Protocol", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Target IP", strip_prompt=False, strip_command=False)
output += net_connect.send_command("172.29.129.151", expect_string=r"Repeat count", strip_prompt=False, strip_command=False)
#output += net_connect.send_command("\n", expect_string=r"Repeat count", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Datagram size", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Timeout in seconds", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Extended commands", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Sweep range of sizes", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"#", strip_prompt=False, strip_command=False)



print(output)


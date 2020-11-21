from netmiko import ConnectHandler

cisco_xr =ConnectHandler(
        device_type= 'cisco_xr',
        host= '172.29.129.1',
        username= 'saby',
        password= 'lab123',
        session_log='XR_Session.txt',
)

print(cisco_xr.find_prompt())








import yaml

my_data = {
        'device_name': 'rtr1',
        'ip_addr': '172.29.129.2',
        'username': 'lab',
        'password': 'lab123'
}

some_list = list(range(10))
my_data['some_list'] = some_list
my_data['null_value'] = None
my_data['a_bool'] = False

filename = 'outputfile.yaml'
with open(filename, "wt") as f:
    yaml.dump(my_data, f, default_flow_style=True)

filename = 'outputfile1_expanded.yaml'
with open(filename, "wt") as f:
    yaml.dump(my_data, f, default_flow_style=False)


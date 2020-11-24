import json

my_data = {
        'device_name': 'R2',
        'ip_addr': '172.29.129.2',
        'username': 'lab',
        'password': 'lab123'
}

some_list = list(range(10))
my_data['some_list'] = some_list
my_data['null_value'] = None
my_data['a_bool'] = False

filename = 'outfile.json'
with open(filename, "wt") as f:
    json.dump(my_data, f, indent=4)

print("Python")
print('#'*10)
print(my_data)
print()
print('JSON')
print('#'*10)
print(json.dumps(my_data))



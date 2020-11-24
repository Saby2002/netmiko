* Cisco in writing.                                                      *
**************************************************************************^C
banner login ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
!
line con 0
line aux 0
line vty 0 4
 login local
 transport input all
!
no scheduler allocate
!
end
eve@Linux-Desktop:~/netmiko/cisco_conf_parser$ vi ios1_showrun.txt 
eve@Linux-Desktop:~/netmiko/cisco_conf_parser$ clear

eve@Linux-Desktop:~/netmiko/cisco_conf_parser$ ipython3
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: from CiscoConfparse import CiscoConfparse
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-1-b95d9416d992> in <module>()
----> 1 from CiscoConfparse import CiscoConfparse

ModuleNotFoundError: No module named 'CiscoConfparse'

In [2]: from ciscoconfparse import CiscoConfparse
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-2-abaab3a79553> in <module>()
----> 1 from ciscoconfparse import CiscoConfparse

ImportError: cannot import name 'CiscoConfparse'

In [3]: quit()
eve@Linux-Desktop:~/netmiko/cisco_conf_parser$ sudo apt install CiscoConfparse
[sudo] password for eve: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package CiscoConfparse
eve@Linux-Desktop:~/netmiko/cisco_conf_parser$ 
eve@Linux-Desktop:~/netmiko/cisco_conf_parser$ 
eve@Linux-Desktop:~/netmiko/cisco_conf_parser$ ipython3
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: from ciscoconfparse import CiscoConfparse
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-1-abaab3a79553> in <module>()
----> 1 from ciscoconfparse import CiscoConfparse

ImportError: cannot import name 'CiscoConfparse'

In [2]: from ciscoconfparse import CiscoConfParse

In [3]: CiscoConfParse('ios1_showrun.txt')
Out[3]: <CiscoConfParse: 148 lines / syntax: ios / comment delimiter: '!' / factory: False>

In [4]: cisco_obj = CiscoConfParse('ios1_showrun.txt')

In [5]: cisco_obj
Out[5]: <CiscoConfParse: 148 lines / syntax: ios / comment delimiter: '!' / factory: False>

In [6]: dir(cisco_obj)
Out[6]: 
['ConfigObjs',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_build_space_tolerant_regex',
 '_find_all_child_OBJ',
 '_find_line_OBJ',
 '_find_sibling_OBJ',
 '_objects_to_uncfg',
 '_sequence_nonparent_lines',
 '_sequence_parent_lines',
 '_unique_OBJ',
 'append_line',
 'atomic',
 'comment_delimiter',
 'commit',
 'convert_braces_to_ios',
 'debug',
 'delete_lines',
 'factory',
 'find_all_children',
 'find_blocks',
 'find_children',
 'find_children_w_parents',
 'find_interface_objects',
 'find_lineage',
 'find_lines',
 'find_object_branches',
 'find_objects',
 'find_objects_dna',
 'find_objects_w_all_children',
 'find_objects_w_child',
 'find_objects_w_missing_children',
 'find_objects_w_parents',
 'find_objects_wo_child',
 'find_parents_w_child',
 'find_parents_wo_child',
 'has_line_with',
 'insert_after',
 'insert_after_child',
 'insert_before',
 'ioscfg',
 'objs',
 'openargs',
 'prepend_line',
 're_match_iter_typed',
 're_search_children',
 'replace_all_children',
 'replace_children',
 'replace_lines',
 'req_cfgspec_all_diff',
 'req_cfgspec_excl_diff',
 'save_as',
 'sync_diff',
 'syntax']

In [7]: 

In [7]: help(cisco_obj.find_objects)

[1]+  Stopped                 ipython3
eve@Linux-Desktop:~/netmiko/cisco_conf_parser$ ipython3
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: cisco_obj
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-2251e5d93a33> in <module>()
----> 1 cisco_obj

NameError: name 'cisco_obj' is not defined

In [2]: cisco_obj = CiscoConfParse('ios1_showrun.txt')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-342637d091a4> in <module>()
----> 1 cisco_obj = CiscoConfParse('ios1_showrun.txt')

NameError: name 'CiscoConfParse' is not defined

In [3]: from ciscoconfparse import CiscoConfParse

In [4]: cisco_obj = CiscoConfParse('ios1_showrun.txt')

In [5]: cisco_obj.find_objects(r"^Interface")
Out[5]: []

In [6]: cisco_obj.find_objects(r"^interface")
Out[6]: 
[<IOSCfgLine # 70 'interface Loopback0'>,
 <IOSCfgLine # 73 'interface GigabitEthernet0/0'>,
 <IOSCfgLine # 80 'interface GigabitEthernet0/1'>,
 <IOSCfgLine # 86 'interface GigabitEthernet0/2'>,
 <IOSCfgLine # 92 'interface GigabitEthernet0/3'>]

In [7]: intf = cisco_obj.find_objects(r"^interface")

In [8]: intf
Out[8]: 
[<IOSCfgLine # 70 'interface Loopback0'>,
 <IOSCfgLine # 73 'interface GigabitEthernet0/0'>,
 <IOSCfgLine # 80 'interface GigabitEthernet0/1'>,
 <IOSCfgLine # 86 'interface GigabitEthernet0/2'>,
 <IOSCfgLine # 92 'interface GigabitEthernet0/3'>]

In [9]: intf[0]
Out[9]: <IOSCfgLine # 70 'interface Loopback0'>

In [10]: intf[0].text
Out[10]: 'interface Loopback0'

In [11]: dir(intf[0])
Out[11]: 
['_VIRTUAL_INTF_REGEX',
 '_VIRTUAL_INTF_REGEX_STR',
 '__abstractmethods__',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_abc_cache',
 '_abc_negative_cache',
 '_abc_negative_cache_version',
 '_abc_registry',
 '_list_reassign_linenums',
 'add_child',
 'add_parent',
 'add_uncfgtext',
 'all_children',
 'all_parents',
 'append_to_family',
 'build_reset_string',
 'child_indent',
 'children',
 'classname',
 'comment_delimiter',
 'confobj',
 'delete',
 'delete_children_matching',
 'dna',
 'family_endpoint',
 'feature',
 'feature_param1',
 'feature_param2',
 'geneology',
 'geneology_text',
 'has_child_with',
 'has_children',
 'hash_children',
 'indent',
 'insert_after',
 'insert_before',
 'intf_in_portchannel',
 'ioscfg',
 'is_child',
 'is_comment',
 'is_config_line',
 'is_ethernet_intf',
 'is_intf',
 'is_loopback_intf',
 'is_object_for',
 'is_parent',
 'is_portchannel_intf',
 'is_subintf',
 'is_virtual_intf',
 'lineage',
 'linenum',
 'oldest_ancestor',
 'parent',
 'portchannel_number',
 're_match',
 're_match_iter_typed',
 're_match_typed',
 're_search',
 're_search_children',
 're_sub',
 'replace',
 'reset',
 'set_comment_bool',
 'siblings',
 'text',
 'verbose']

In [12]: intf[0].children
Out[12]: [<IOSCfgLine # 71 ' ip address 2.2.2.2 255.255.255.255' (parent is # 70)>]

In [13]: intf[1].children
Out[13]: 
[<IOSCfgLine # 74 ' vrf forwarding MGMT' (parent is # 73)>,
 <IOSCfgLine # 75 ' ip address 172.29.129.2 255.255.255.0' (parent is # 73)>,
 <IOSCfgLine # 76 ' duplex auto' (parent is # 73)>,
 <IOSCfgLine # 77 ' speed auto' (parent is # 73)>,
 <IOSCfgLine # 78 ' media-type rj45' (parent is # 73)>]

In [14]: for child in intf[1].children:
    ...:     print(child.text)
    ...:     
 vrf forwarding MGMT
 ip address 172.29.129.2 255.255.255.0
 duplex auto
 speed auto
 media-type rj45

In [15]: intf[1]
Out[15]: <IOSCfgLine # 73 'interface GigabitEthernet0/0'>

In [16]: intf[1].text
Out[16]: 'interface GigabitEthernet0/0'

In [17]: 

In [17]: dir(cisco_obj)
Out[17]: 
['ConfigObjs',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_build_space_tolerant_regex',
 '_find_all_child_OBJ',
 '_find_line_OBJ',
 '_find_sibling_OBJ',
 '_objects_to_uncfg',
 '_sequence_nonparent_lines',
 '_sequence_parent_lines',
 '_unique_OBJ',
 'append_line',
 'atomic',
 'comment_delimiter',
 'commit',
 'convert_braces_to_ios',
 'debug',
 'delete_lines',
 'factory',
 'find_all_children',
 'find_blocks',
 'find_children',
 'find_children_w_parents',
 'find_interface_objects',
 'find_lineage',
 'find_lines',
 'find_object_branches',
 'find_objects',
 'find_objects_dna',
 'find_objects_w_all_children',
 'find_objects_w_child',
 'find_objects_w_missing_children',
 'find_objects_w_parents',
 'find_objects_wo_child',
 'find_parents_w_child',
 'find_parents_wo_child',
 'has_line_with',
 'insert_after',
 'insert_after_child',
 'insert_before',
 'ioscfg',
 'objs',
 'openargs',
 'prepend_line',
 're_match_iter_typed',
 're_search_children',
 'replace_all_children',
 'replace_children',
 'replace_lines',
 'req_cfgspec_all_diff',
 'req_cfgspec_excl_diff',
 'save_as',
 'sync_diff',
 'syntax']

In [18]: cisco_obj.find_parents_w_child
Out[18]: <bound method CiscoConfParse.find_parents_w_child of <CiscoConfParse: 148 lines / syntax: ios / comment delimiter: '!' / factory: False>>

In [19]: cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec= r"^/
    ...: sinterface)
  File "<ipython-input-19-795bc85a7ab0>", line 1
    cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec= r"^/sinterface)
                                                                          ^
SyntaxError: invalid syntax


In [20]: cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=(r"^/
    ...: sinterface)
  File "<ipython-input-20-e50a6f233f81>", line 1
    cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=(r"^/sinterface)
                                                                          ^
SyntaxError: invalid syntax


In [21]: cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=(r"^i
    ...: nterface")
  File "<ipython-input-21-2ebceb26f3bd>", line 1
    cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=(r"^interface")
                                                                                     ^
SyntaxError: EOL while scanning string literal


In [22]: cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=r"^in
    ...: terface")
  File "<ipython-input-22-d31b4e6b15cd>", line 1
    cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=r"^interface")
                                                                                    ^
SyntaxError: EOL while scanning string literal


In [23]: cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=(r"^i
    ...: nterface")
  File "<ipython-input-23-2ebceb26f3bd>", line 1
    cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=(r"^interface")
                                                                                     ^
SyntaxError: EOL while scanning string literal


In [24]: 

In [24]: 

In [24]: cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=r"^/s
    ...: ip address"))
  File "<ipython-input-24-1e2e010cf30f>", line 1
    cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=r"^/sip address"))
                                                                         ^
SyntaxError: invalid syntax


In [25]: cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=r"^/s
    ...: ip address")
  File "<ipython-input-25-9a7ea577800e>", line 1
    cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=r"^/sip address")
                                                                         ^
SyntaxError: invalid syntax


In [26]: cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=r"ip 
    ...: address")
  File "<ipython-input-26-9733749547db>", line 1
    cisco_obj.find_parents_w_child(parentspec=r"^interface, childspec=r"ip address")
                                                                         ^
SyntaxError: invalid syntax


In [27]: 

In [27]: 

In [27]: cisco_obj.find_parents_w_child(parentspec=r"^interface", childspec=r"^/
    ...: sip address")
Out[27]: []

In [28]: cisco_obj.find_parents_w_child(parentspec=r"^interface", childspec=r"^\
    ...: sip address")
Out[28]: 
['interface Loopback0',
 'interface GigabitEthernet0/0',
 'interface GigabitEthernet0/1',
 'interface GigabitEthernet0/3']

In [29]: cisco_obj.find_parents_w_child(parentspec=r"^interface", childspec=r"^\
    ...: s+ip address")
Out[29]: 
['interface Loopback0',
 'interface GigabitEthernet0/0',
 'interface GigabitEthernet0/1',
 'interface GigabitEthernet0/3']

In [30]: match = cisco_obj.find_parents_w_child(parentspec=r"^interface", childs
    ...: pec=r"^\sip address")

In [31]: match
Out[31]: 
['interface Loopback0',
 'interface GigabitEthernet0/0',
 'interface GigabitEthernet0/1',
 'interface GigabitEthernet0/3']

In [32]: match.text
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-32-00dc34927d7e> in <module>()
----> 1 match.text

AttributeError: 'list' object has no attribute 'text'

In [33]: match[0].text
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-33-09767bf0cc25> in <module>()
----> 1 match[0].text

AttributeError: 'str' object has no attribute 'text'

In [34]: match.children
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-34-1eec00f52209> in <module>()
----> 1 match.children

Attribu:wq!


#!/usr/bin/env python3
from sys import argv

interface = argv[1]
vlan = argv[2]
argv3 = argv[3]

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('Interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))
print('Argv3 is: {}'.format(argv3))



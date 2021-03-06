# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.


user_input = input("Enter VLAN number: ")
results = []
with open("CAM_table.txt") as f:
    for line in f:
        line = line.split()
        template = '{:15} {:15} {:15}'
        if line and line[0].isdigit():
            vlan,mac,_,port = line
            line = vlan,mac,port
            results.append([int(vlan),mac,port])

for vlan, mac,port in sorted(results):
	if int(user_input) == vlan:
		print(f"{vlan:<9}{mac:20}{port}")
		"""
user_vlan = input("Enter VLAN number: ")

with open("CAM_table.txt", "r") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit() and words[0] == user_vlan:
            vlan, mac, _, intf = words
            print(f"{vlan:9}{mac:20}{intf}")
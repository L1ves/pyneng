# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0
O        10.0.28.0/24 [110/31] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.37.0/24 [110/11] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.41.0/24 [110/51] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.78.0/24 [110/21] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.79.0/24 [110/20] via 10.0.19.9, 4d02h, FastEthernet0/2


"""
output = "\n{:25} {}" * 5

with open('ospf.txt') as x:
	for y in x:
		y = y.replace(',','').replace('[','').replace(']','')
		y = y.split()
		print(output.format(
			"Prefix", y[1],
			"AD/Metric", y[2],
			"Next-Hop", y[4],
			"Last update", y[5],
			"Outbound Interface", y[6]))

"""
prefix = y[1]
ad_metric = y[2]
next_hop = y[4]
last_update = y[5]
outbond_interface = y[6]
print(f"Prefix {prefix:>30}\n AD/Metric {ad_metric:>20}\n Next-Hop {next_hop:>24}\n Last update {last_update:>17}\n Outbound Interface {outbond_interface:>20}")
"""
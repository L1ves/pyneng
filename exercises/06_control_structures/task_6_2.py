# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

uni = "unicast"
multi = "multicast"
bro = "local broadcast"
unassigned = "unassigned"
unused = "unused"

#1)провести проверку длинны равную 4
user_input = input("Input ip adress like format 10.10.10.1\n")
first_byte = list(user_input.split("."))
if len(first_byte) == 4:
    #2)выделить первый байт
    remix_num = int(first_byte[0])
    if remix_num >= 1 and remix_num <= 223:
        print(f'{uni}')
    elif remix_num >= 224 and remix_num <= 239:
        print(f'{multi}')
    elif user_input == '0.0.0.0':
        print(f'{unassigned}')
    elif user_input == "255.255.255.255":    #остановились на проверке broadcast и unassigned
        print(f'{bro}')
    else:
        print(f'{unused}')
else:
    print(f'{unused}')

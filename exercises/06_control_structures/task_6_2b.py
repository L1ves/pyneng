# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
uni = "unicast"
multi = "multicast"
bro = "local broadcast"
unassigned = "unassigned"
unused = "unused"

correct_address = True

while correct_address:
	user_input = input("Input ip adress like format 10.10.10.1\n")
	q = list(user_input.replace(",", ".").split("."))
	if len(q)==4 and q[0].isdigit() and q[1].isdigit() and q[2].isdigit() and q[3].isdigit() and 0<=int(q[0])<=255 \
	        and 0<=int(q[1])<=255 and 0<=int(q[2])<=255 and 0<=int(q[3])<=255:
	            #2)выделить первый байт
	        correct_address = False
	        remix_num = int(q[0])
	        if remix_num >= 1 and remix_num <= 223:
	            print(f'{uni}')
	        elif remix_num >= 224 and remix_num <= 239:
	            print(f'{multi}')
	        elif user_input == '0.0.0.0':
	            print(f'{unassigned}')
	        elif user_input == "255.255.255.255": 
	            print(f'{bro}')
	        else:
	            print(f'{unused}')

	else:
	    print("Неправильный IP-адрес")

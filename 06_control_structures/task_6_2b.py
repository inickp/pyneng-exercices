# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

valid = 0
while valid != 1:
  ip_input = raw_input ('IP: ')
  for oct in ip_input.split('.'):
    if (len(ip_input.split('.')) != 4) or not (oct.isdigit()) or (int(oct) < 0) or (int(oct) > 255):
      print('wrong IP')
      break
    else:
      valid = 1 

if ip_input == '255.255.255.255':
  print('local broadcast')
elif ip_input == '0.0.0.0':
  print ('unassigned')
elif int(ip_input.split('.')[0])  <= 223 and int(ip_input.split('.')[0]) >= 1:
  print ('unicast')
elif int(ip_input.split('.')[0]) >= 224 and  int(ip_input.split('.')[0]) <=239:
  print ('multicast')
else:
  print ('unused')


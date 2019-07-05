# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip_input = raw_input ('IP: ')
for oct in ip_input.split('.'):
  if (len(ip_input.split('.')) != 4) or not (oct.isdigit()) or (int(oct) < 0) or (int(oct) > 255):
#    print (octs)
#    print (oct.isdigit())
#    print (int(oct))
    print('wrong IP')
    exit()

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


# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def get_int_vlan_map(config_filename):
  intf_access_list=[]
  vlan_access_list=[]
  intf_trunk_list=[]
  vlan_trunk_list=[]
  f=open(config_filename)
  for config_piece in f.read().split('!'):
    if config_piece.strip().startswith('interface Fast'):
      if config_piece.find(' switchport mode access'):
        append_interface_vlan_lists(config_piece, intf_access_list, vlan_access_list, type='access')
      if config_piece.find(' switchport mode trunk'):
        append_interface_vlan_lists(config_piece, intf_trunk_list, vlan_trunk_list, type='trunk')

#  create dict_access
  access_dict = {key: None for key in intf_access_list}
  i=0
  for key in access_dict.keys():
    access_dict[key] = vlan_access_list[i]
    i = i+1
#  create dict_trunk
  trunk_dict = {key: None for key in intf_trunk_list}
  i=0
  for key in trunk_dict.keys():
    trunk_dict[key] = vlan_trunk_list[i]
    i = i+1
  
#  create tuple
  tuple = (access_dict, trunk_dict)
  print(tuple)
  return tuple

def append_interface_vlan_lists(interface_conf_str, intf_list, vlan_list, type):
#  print(interface_conf_str)
  access_vlan_explicit = False
  interface = ''

  for str in interface_conf_str.split('\n'):
    if str.strip().startswith('interface Fast'):
      interface = str.strip().strip('interface ')
    if str.strip().startswith('switchport access vlan ') and type=='access':
      access_vlan_explicit = True
      vlan_list.append(str.strip().strip('switchport access vlan '))
      intf_list.append(interface)
    if str.strip().startswith('switchport trunk allowed vlan ') and type=='trunk':
      vlan_list.append(str.strip().strip('switchport trunk allowed vlan ').split(','))
      intf_list.append(interface)
  if type=='access' and access_vlan_explicit == False:
    vlan_list.append('1')
    intf_list.append(interface)

get_int_vlan_map('config_sw2.txt')

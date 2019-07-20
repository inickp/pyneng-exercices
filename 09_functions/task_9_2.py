# -*- coding: utf-8 -*-
'''
Задание 9.2

Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.

У функции должны быть такие параметры:

- intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)

Функция должна возвращать список команд с конфигурацией
на основе указанных портов и шаблона trunk_mode_template.
В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_config.

Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


def trunk_config_generate(intf_vlans,config_template):
  result=[]
  for key, value in intf_vlans.items():
    result.append('interface {}'.format(key))
    result.append(config_template[0])
    result.append(config_template[1])
    allowed_vlans=config_template[2]
    for vlan in value:
      allowed_vlans=allowed_vlans + ' ' + str(vlan) + ','
    result.append(allowed_vlans.strip(','))
  return result

print(trunk_config_generate(trunk_config,trunk_mode_template))

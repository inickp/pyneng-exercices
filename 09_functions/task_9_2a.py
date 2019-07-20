# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

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
  intf_list = list(intf_vlans.keys())
  intf_commands_dict = {key: None for key in intf_list}
  for key, value in intf_vlans.items():
    intf_commands_list=[]
    intf_commands_list.append(config_template[0])
    intf_commands_list.append(config_template[1])
    allowed_vlans=config_template[2]
    for vlan in value:
      allowed_vlans=allowed_vlans + ' ' + str(vlan) + ','
    intf_commands_list.append(allowed_vlans.strip(','))
    intf_commands_dict[key] = intf_commands_list
  return intf_commands_dict

print(trunk_config_generate(trunk_config,trunk_mode_template))


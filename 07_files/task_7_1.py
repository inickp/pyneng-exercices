# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
f=open('ospf.txt')
strList=f.read().split('\n')
ospfTemplate = '''
Protocol:              {0}
Prefix:                {1}
AD/Metric:             {2}
Next-Hop:              {3}
Last Update:           {4}
Outbound Interface:    {5}
'''


for str in strList:
  list=str.split(' ')
  if str=='':
    break
  if list[0] == 'O':
    proto='OSPF'
  prefix=list[8]
  adMetr=list[10].strip('[]')
  nH=list[11].strip(',')
  lastUpd=list[12].strip(',')
  outbInt=list[13]
  print ospfTemplate.format(proto,prefix,adMetr,nH,lastUpd,outbInt)

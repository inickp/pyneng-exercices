# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv

f=open(argv[1])
strList=f.read().split('\n')
f.close()
fw=open('config_sw1_cleared.txt','w')
for str in strList:
  counter=0
  for i in ignore:
    if i not in str:
      counter=counter+1
    if counter==len(ignore):
      fw.write(str + '\n')
fw.close()


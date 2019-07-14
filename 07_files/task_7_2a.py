# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv

f=open(argv[1])
strList=f.read().split('\n')
for str in strList:
  if not str.startswith('!'):
    counter=0
    for i in ignore:
      if i not in str:
        counter=counter+1
      if counter==len(ignore):
        print(str)

# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv

f=open(argv[1])
strList=f.read().split('\n')
f.close()
fw=open(argv[2],'w')
for str in strList:
  counter=0
  for i in ignore:
    if i not in str:
      counter=counter+1
    if counter==len(ignore):
      fw.write(str + '\n')
fw.close()


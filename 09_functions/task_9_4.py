# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration', '!']



def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в ignore_commandкоманде содержится слово из списка ignore
    * False - если нет
    '''


    return any(word in command for word in ignore)





def list_glob_commands(commands_list):
  glob_commands_list = []
  for str in commands_list:
    if not str.startswith(' ') and not ignore_command(str, ignore) and not len(str)==0:
      glob_commands_list.append(str)
  return glob_commands_list


def list_subcommands(glob_command, commands_list):
  i = commands_list.index(glob_command) + 1
  subcommands_list = []
  while commands_list[i].startswith(' '):
    subcommands_list.append(commands_list[i])
    i = i+1
  return subcommands_list




file = open('config_sw1.txt')
list = file.read().split('\n')
glob_commands = list_glob_commands(list)
config_dict = {key: list_subcommands(key, list) for key in glob_commands}
print(config_dict)




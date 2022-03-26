### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками 
на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть 
[здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-03-yaml/README.md). 
Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать 
форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. 
Вместо логов можно вставить скриншоты по желани.

# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"

## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```json
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

1. Отсутствие запятой при перечислении элементов списка словарей в ключе "elements"
2. Неверное значение ключа "ip" - не является IP-адресом
```json
{ "name" : "first",
  "type" : "server",
  "ip" : 7175 
}
```
3. Отсутствие закрывающей кавычки ключа "ip", значение ключа "ip" не заключено в кавычки
```json
{ "name" : "second",
  "type" : "proxy",
  "ip : 71.78.22.43
}
```

Верный ответ должен быть таким
```json
{
    "info": "Sample JSON output from our service\t",
    "elements": [
        {
            "name": "first",
            "type": "server",
            "ip": "71.75.0.2"
        },
        {
            "name": "second",
            "type": "proxy",
            "ip": "71.78.22.43"
        }
    ]
}
```


## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному 
функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по 
одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в 
момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
#!/usr/bin/env python3

import dns.resolver
import json
import requests
import os
import signal
import time
import yaml

os.system("clear")

etl_dict = {}
# etl_dict = {'drive.google.com': {'64.233.162.194'},
#             'mail.google.com': {'64.233.165.18', '64.233.165.17', '64.233.165.19', '64.233.165.83'},
#             'google.com': {'64.233.162.139', '64.233.162.113', '64.233.162.102', '64.233.162.101',
#                            '64.233.162.138', '64.233.162.100'}}

services_list: list[str] = ['drive.google.com', 'mail.google.com', 'google.com']
query_type: str = 'A'
check_interval = 10
save_format: str = 'JSON'  # 'YAML' or 'JSON'


def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)


def url_ok(url):
    r = requests.head(url)
    return str(r.status_code) in ("200", "301", "302",)


def dns_resolve(fqdn):
    r = dns.resolver.resolve(fqdn, query_type, raise_on_no_answer=False)
    return r


def save_results(dict_to_save, save_fmt):
    with open(f'data.{save_fmt.lower()}', 'w') as f:
        if save_fmt == "JSON":
            json.dump(dict_to_save, f, indent=2)
        elif save_fmt == "YAML":
            yaml.dump(dict_to_save, f, indent=2)


signal.signal(signal.SIGINT, handler)

while 1:
    service_dict = {}
    for service in services_list:
        ip_list: list[str] = []
        answer = dns_resolve(service)
        for val in answer:
            ip = val.to_text()
            ip_list.append(ip)
            if service in etl_dict:
                if ip not in etl_dict[service]:
                    print(f'[ERROR] {service} IP mismatch: new IP {ip} not in the IP list {etl_dict[service]}')

        service_dict.update([(service, ip_list)])

        if url_ok(f'https://{service}'):
            service_status = 'Connection OK'
        else:
            service_status = 'Connection Failed'

        print(f'{service} - {service_dict[service]} - status {service_status}')

    etl_dict = service_dict

    save_results(etl_dict, save_format)

    time.sleep(check_interval)
    
    # если нужно очищать терминал перед выводом результатов текущей проверки, раскомментировать
    # os.system("clear")
```

### Вывод скрипта при запуске при тестировании:
```
drive.google.com - ['142.251.1.194'] - status Connection OK
mail.google.com - ['108.177.14.83', '108.177.14.19', '108.177.14.18', '108.177.14.17'] - status Connection OK
google.com - ['74.125.131.102', '74.125.131.101', '74.125.131.139', '74.125.131.138', '74.125.131.100', '74.125.131.113'] - status Connection OK
[ERROR] drive.google.com IP mismatch: new IP 74.125.131.194 not in the IP list ['142.251.1.194']
drive.google.com - ['74.125.131.194'] - status Connection OK
mail.google.com - ['108.177.14.83', '108.177.14.19', '108.177.14.18', '108.177.14.17'] - status Connection OK
google.com - ['74.125.131.102', '74.125.131.101', '74.125.131.139', '74.125.131.138', '74.125.131.100', '74.125.131.113'] - status Connection OK
Ctrl-c was pressed. Do you really want to exit? y/n y
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
{
  "drive.google.com": [
    "74.125.131.194"
  ],
  "mail.google.com": [
    "108.177.14.83",
    "108.177.14.19",
    "108.177.14.18",
    "108.177.14.17"
  ],
  "google.com": [
    "74.125.131.102",
    "74.125.131.101",
    "74.125.131.139",
    "74.125.131.138",
    "74.125.131.100",
    "74.125.131.113"
  ]
}
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
drive.google.com:
- 142.251.1.194
google.com:
- 74.125.131.102
- 74.125.131.101
- 74.125.131.139
- 74.125.131.138
- 74.125.131.100
- 74.125.131.113
mail.google.com:
- 108.177.14.83
- 108.177.14.19
- 108.177.14.18
- 108.177.14.17
```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: 
JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

### Ваш скрипт:
```python
???
```

### Пример работы скрипта:
???

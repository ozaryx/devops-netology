### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-02-py/README.md). Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. Вместо логов можно вставить скриншоты по желани.

# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательная задача 1

Есть скрипт:
```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```

### Вопросы:
| Вопрос  | Ответ                  |
| ------------- |------------------------|
| Какое значение будет присвоено переменной `c`?  | никакое, будет ошибка TypeError: unsupported operand type(s) for +: 'int' and 'str' |
| Как получить для переменной `c` значение 12?  | c = str(a) + str(b)    |
| Как получить для переменной `c` значение 3?  | c = int(a) + int(b)    |

```shell
>>> a=1
>>> b='2'
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> c = str(a) + b
>>> print(c)
12
>>> c = a + int(b)
>>> print(c)
3
```

## Обязательная задача 2
Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие 
файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что 
в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно 
доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```

### Ваш скрипт:
```python
#!/usr/bin/env python3

import os

curr_dir = os.getcwd()
repo_path = os.path.normpath(curr_dir)
bash_command = ["cd " + repo_path, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        file_path = os.path.normpath(repo_path+'/'+prepare_result)
        print(file_path)
```

### Вывод скрипта при запуске при тестировании:
```shell
kmankov$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   test.py
	new file:   test1.sh

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   test1.sh
```
```shell
kmankov$ pwd
/Users/kmankov/PycharmProjects/sysadm-homeworks-test

kmankov$ ~/show_diff.py 
~/PycharmProjects/sysadm-homeworks-test/test.py
~/PycharmProjects/sysadm-homeworks-test/test1.sh
```

## Обязательная задача 3
Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел 
воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и 
будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ваш скрипт:
```python
#!/usr/bin/env python3

import os
import sys

curr_dir = os.getcwd()

if len(sys.argv) > 1:
    curr_dir = os.path.normpath(sys.argv[1])

repo_path = os.path.normpath(curr_dir)

if os.path.isdir(repo_path+'/.git'):
    bash_command = ["cd " + repo_path, "git status"]
    result_os = os.popen(' && '.join(bash_command)).read()

    for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            file_path = os.path.normpath(repo_path+'/'+prepare_result)
            print(file_path)
else:
    print(f'{repo_path} is not Git repository')
```

### Вывод скрипта при запуске при тестировании:
```shell 
kmankov$ pwd
/Users/kmankov/PycharmProjects/sysadm-homeworks-test

kmankov$ ~/show_diff.py 
/Users/kmankov/PycharmProjects/sysadm-homeworks-test/test.py
/Users/kmankov/PycharmProjects/sysadm-homeworks-test/test1.sh

kmankov$ ~/show_diff.py ~/PycharmProjects/devops-netology/
/Users/kmankov/PycharmProjects/devops-netology/.DS_Store
/Users/kmankov/PycharmProjects/devops-netology/04-script-02-py/README.md

kmankov$ ~/show_diff.py ~/vagrant/
/Users/kmankov/vagrant is not Git repository
```

## Обязательная задача 4
Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой 
балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, 
занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом 
сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в 
такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает 
веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть 
реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - 
оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем 
считать, что наша разработка реализовала сервисы: `drive.google.com`, `mail.google.com`, `google.com`.

### Ваш скрипт:
```python
#!/usr/bin/env python3

import dns.resolver
import requests
import os
import signal
import time

os.system("clear")

etl_dict = {}
# etl_dict = {'drive.google.com': {'64.233.162.194'},
#             'mail.google.com': {'64.233.165.18', '64.233.165.17', '64.233.165.19', '64.233.165.83'},
#             'google.com': {'64.233.162.139', '64.233.162.113', '64.233.162.102', '64.233.162.101',
#                            '64.233.162.138', '64.233.162.100'}}

services_list: list[str] = ['drive.google.com', 'mail.google.com', 'google.com']
query_type: str = 'A'
check_interval = 10


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


signal.signal(signal.SIGINT, handler)

while 1:
    service_dict = {}
    for service in services_list:
        ip_list = set()
        answer = dns_resolve(service)
        for val in answer:
            ip = val.to_text()
            ip_list.add(ip)
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

    time.sleep(check_interval)
    
    # если нужно очищать терминал перед выводом результатов текущей проверки, раскомментировать
    # os.system("clear")
```

### Вывод скрипта при запуске при тестировании:
```
drive.google.com - {'142.251.1.194'} - status Connection OK
mail.google.com - {'142.251.1.18', '142.251.1.19', '142.251.1.83', '142.251.1.17'} - status Connection OK
google.com - {'209.85.233.102', '209.85.233.100', '209.85.233.113', '209.85.233.101', '209.85.233.138', '209.85.233.139'} - status Connection OK
drive.google.com - {'142.251.1.194'} - status Connection OK
mail.google.com - {'142.251.1.18', '142.251.1.19', '142.251.1.83', '142.251.1.17'} - status Connection OK
google.com - {'209.85.233.102', '209.85.233.100', '209.85.233.113', '209.85.233.101', '209.85.233.138', '209.85.233.139'} - status Connection OK
[ERROR] drive.google.com IP mismatch: new IP 108.177.14.194 not in the IP list {'142.251.1.194'}
drive.google.com - {'108.177.14.194'} - status Connection OK
mail.google.com - {'142.251.1.18', '142.251.1.19', '142.251.1.83', '142.251.1.17'} - status Connection OK
google.com - {'209.85.233.102', '209.85.233.100', '209.85.233.113', '209.85.233.101', '209.85.233.138', '209.85.233.139'} - status Connection OK
drive.google.com - {'108.177.14.194'} - status Connection OK
mail.google.com - {'142.251.1.18', '142.251.1.19', '142.251.1.83', '142.251.1.17'} - status Connection OK
google.com - {'209.85.233.102', '209.85.233.100', '209.85.233.113', '209.85.233.101', '209.85.233.138', '209.85.233.139'} - status Connection OK
drive.google.com - {'108.177.14.194'} - status Connection OK
^CCtrl-c was pressed. Do you really want to exit? y/n y
```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению
Так получилось, что мы очень часто вносим правки в конфигурацию своей системы прямо на сервере. Но так как вся наша 
команда разработки держит файлы конфигурации в github и пользуется gitflow, то нам приходится каждый раз переносить 
архив с нашими изменениями с сервера на наш локальный компьютер, формировать новую ветку, коммитить в неё изменения, 
создавать pull request (PR) и только после выполнения Merge мы наконец можем официально подтвердить, что новая 
конфигурация применена. Мы хотим максимально автоматизировать всю цепочку действий. Для этого нам нужно написать скрипт, 
который будет в директории с локальным репозиторием обращаться по API к github, создавать PR для вливания текущей 
выбранной ветки в master с сообщением, которое мы вписываем в первый параметр при обращении к py-файлу (сообщение не 
может быть пустым). При желании, можно добавить к указанному функционалу создание новой ветки, commit и push в неё 
изменений конфигурации. С директорией локального репозитория можно делать всё что угодно. Также, принимаем во внимание, 
что Merge Conflict у нас отсутствуют и их точно не будет при push, как в свою ветку, так и при слиянии в master. Важно 
получить конечный результат с созданным PR, в котором применяются наши изменения. 

### Ваш скрипт:
```python
???
```

### Вывод скрипта при запуске при тестировании:
```
???
```

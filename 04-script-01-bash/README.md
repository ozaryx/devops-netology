### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-01-bash/README.md). Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. Вместо логов можно вставить скриншоты по желани.

---


# Домашнее задание к занятию "4.1. Командная оболочка Bash: Практические навыки"

## Обязательная задача 1

Есть скрипт:
```bash
a=1
b=2
c=a+b
d=$a+$b
e=$(($a+$b))
```

Какие значения переменным c,d,e будут присвоены? Почему?

| Переменная  | Значение | Обоснование                                                              |
| ------------- |----------|--------------------------------------------------------------------------|
| `c`  | a+b      | Выполняется присвоение строкового значения                               |
| `d`  | 1+2      | Выполняется присвоение строкового значения переменных a и b и знака +    |
| `e`  | 3        | Выполняется арифметичская операция сложения числовых значений перменных a и b |

При этом в выражении `(($a+$b))` не надо использовать знак $ для обозначения переменных.
```shell
a=1
b=2
e=$((a+b))
echo $e
3
```

## Обязательная задача 2
На нашем локальном сервере упал сервис и мы написали скрипт, который постоянно проверяет его доступность, 
записывая дату проверок до тех пор, пока сервис не станет доступным (после чего скрипт должен завершиться). 
В скрипте допущена ошибка, из-за которой выполнение не может завершиться, при этом место на Жёстком Диске 
постоянно уменьшается. Что необходимо сделать, чтобы его исправить:

```bash
while ((1==1)
do
	curl https://localhost:4757
	if (($? != 0))
	then
		date >> curl.log
	fi
done
```

Этот код вообще работать не будет. Синтаксическая ошибка в коде - строка 1 - в '((1==1)' не хватает ')'
```shell
vagrant@vagrant:~$ sh ./test_web.sh 
./test_web.sh: 4: Syntax error: "do" unexpected (expecting ")")
```

Условие ((1==1)) будет выполняться бесконечно.

### Ваш скрипт:
```bash
while ! curl https://localhost:4757; do
  date >> curl.log
done
```

## Обязательная задача 3
Необходимо написать скрипт, который проверяет доступность трёх IP: `192.168.0.1`, `173.194.222.113`, `87.250.250.242` 
по `80` порту и записывает результат в файл `log`. Проверять доступность необходимо пять раз для каждого узла.

### Ваш скрипт:
./check_web.sh 
```bash
#!/usr/bin/env bash

declare -a HOSTS
HOSTS=(192.168.0.1 173.194.222.113 87.250.250.242)

for host in "${HOSTS[@]}"; do
  for (( i=1; i<=5; i++ )); do
    URL="http://$host"
    c=0
    if curl -m 5 "$URL" > /dev/null 2>&1; then
      echo "$(date) - $host - Connection OK" | tee -a log
    else
      echo "$(date) - $host - Unreachable" | tee -a log
    fi
  done
done

```
```shell
vagrant@vagrant:~$ cat log 
Sat Mar  5 05:34:56 UTC 2022 - 192.168.0.1 - Unreachable
Sat Mar  5 05:35:01 UTC 2022 - 192.168.0.1 - Unreachable
Sat Mar  5 05:35:06 UTC 2022 - 192.168.0.1 - Unreachable
Sat Mar  5 05:35:11 UTC 2022 - 192.168.0.1 - Unreachable
Sat Mar  5 05:35:16 UTC 2022 - 192.168.0.1 - Unreachable
Sat Mar  5 05:35:16 UTC 2022 - 173.194.222.113 - Connection OK
Sat Mar  5 05:35:16 UTC 2022 - 173.194.222.113 - Connection OK
Sat Mar  5 05:35:16 UTC 2022 - 173.194.222.113 - Connection OK
Sat Mar  5 05:35:17 UTC 2022 - 173.194.222.113 - Connection OK
Sat Mar  5 05:35:17 UTC 2022 - 173.194.222.113 - Connection OK
Sat Mar  5 05:35:17 UTC 2022 - 87.250.250.242 - Connection OK
Sat Mar  5 05:35:17 UTC 2022 - 87.250.250.242 - Connection OK
Sat Mar  5 05:35:18 UTC 2022 - 87.250.250.242 - Connection OK
Sat Mar  5 05:35:18 UTC 2022 - 87.250.250.242 - Connection OK
Sat Mar  5 05:35:18 UTC 2022 - 87.250.250.242 - Connection OK
```


## Обязательная задача 4
Необходимо дописать скрипт из предыдущего задания так, чтобы он выполнялся до тех пор, пока один из узлов не окажется 
недоступным. Если любой из узлов недоступен - IP этого узла пишется в файл error, скрипт прерывается.

### Ваш скрипт:
check_web2.sh
```shell
#!/usr/bin/env bash

declare -a HOSTS
HOSTS=(173.194.222.113 87.250.250.242 192.168.0.1)

for host in "${HOSTS[@]}"; do
  c=0
  for (( i=1; i<=5; i++ )); do
    URL="http://$host"
    if curl -m 5 "$URL" > /dev/null 2>&1; then
      echo "$(date) - $host - Connection OK" | tee -a log
    else
      echo "$(date) - $host - Unreachable" | tee -a log
      c=$((++c))
    fi
  done

  if (( c == 5 )); then
    echo "$(date) - $host - Totally Unreachable" | tee -a log
    exit 1
  fi
  
done
```
```shell
vagrant@vagrant:~$ cat log 
Sat Mar  5 06:03:30 UTC 2022 - 173.194.222.113 - Connection OK
Sat Mar  5 06:03:30 UTC 2022 - 173.194.222.113 - Connection OK
Sat Mar  5 06:03:30 UTC 2022 - 173.194.222.113 - Connection OK
Sat Mar  5 06:03:31 UTC 2022 - 173.194.222.113 - Connection OK
Sat Mar  5 06:03:31 UTC 2022 - 173.194.222.113 - Connection OK
Sat Mar  5 06:03:31 UTC 2022 - 87.250.250.242 - Connection OK
Sat Mar  5 06:03:31 UTC 2022 - 87.250.250.242 - Connection OK
Sat Mar  5 06:03:32 UTC 2022 - 87.250.250.242 - Connection OK
Sat Mar  5 06:03:32 UTC 2022 - 87.250.250.242 - Connection OK
Sat Mar  5 06:03:32 UTC 2022 - 87.250.250.242 - Connection OK
Sat Mar  5 06:03:37 UTC 2022 - 192.168.0.1 - Unreachable
Sat Mar  5 06:03:42 UTC 2022 - 192.168.0.1 - Unreachable
Sat Mar  5 06:03:47 UTC 2022 - 192.168.0.1 - Unreachable
Sat Mar  5 06:03:52 UTC 2022 - 192.168.0.1 - Unreachable
Sat Mar  5 06:03:57 UTC 2022 - 192.168.0.1 - Unreachable
Sat Mar  5 06:03:57 UTC 2022 - 192.168.0.1 - Totally Unreachable
```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Мы хотим, чтобы у нас были красивые сообщения для коммитов в репозиторий. Для этого нужно написать локальный хук для 
git, который будет проверять, что сообщение в коммите содержит код текущего задания в квадратных скобках и количество 
символов в сообщении не превышает 30. Пример сообщения: \[04-script-01-bash\] сломал хук.

### Ваш скрипт:
используется хук commit-msg

```bash
#!/bin/sh

if ! grep '\[04-script-01-bash\]' "$1" > /dev/null 2>&1; then
  echo "Commit doesn't start with [04-script-01-bash]"
  exit 1
fi

read -r message <<< "$(cat "$1")"
if [ ${#message} -gt 30 ]; then
  echo "Commit message more than 30 characters"
  exit 1
fi

```

```shell
$ git commit -m "add line"
Commit doesn't start with [04-script-01-bash]

$ git commit -m "[04-script-01-bash] delete line from file1.sh long commit message"
Commit message more than 30 characters

$ git commit -m "[04-script-01-bash] delete lin"
[master e7f413c] [04-script-01-bash] delete lin
 1 file changed, 2 deletions(-)

```

## Задание 1

Конфигурация сервиса node exporter

    $ cat /opt/node_exporter/node_exporter.service
    [Unit]
    Description=Node exporter
    
    [Service]
    Restart=always
    User=vagrant
    EnvironmentFile=/opt/node_exporter/node_exporter.conf
    ExecStart=/usr/bin/node_exporter $ARGS
    ExecReload=/bin/kill -HUP $MAINPID
    ExecStop=/bin/kill -TERM $MAINPID
    TimeoutStopSec=20s
    SendSIGKILL=no
    
    [Install]
    WantedBy=multi-user.target

Файл конфигурации node exporter

    $ cat /opt/node_exporter/node_exporter.conf
    ARGS="--log.level=warn"

Установка node exporter в systemd

    $ sudo systemctl link /opt/node_exporter/node_exporter.service
    Created symlink /etc/systemd/system/node_exporter.service → /opt/node_exporter/node_exporter.service.

Включение node exporter

    $ sudo systemctl enable node_exporter.service
    Created symlink /etc/systemd/system/multi-user.target.wants/node_exporter.service → /opt/node_exporter/node_exporter.service.

Проверка статуса

    $ sudo systemctl status node_exporter.service
    ● node_exporter.service - Node exporter
         Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
         Active: inactive (dead)

Запуск

    $ sudo systemctl start node_exporter.service
    $ sudo systemctl status node_exporter.service
    ● node_exporter.service - Node exporter
         Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
         Active: active (running) since Wed 2022-01-26 14:33:55 UTC; 10s ago
       Main PID: 11442 (node_exporter)
          Tasks: 5 (limit: 1659)
         Memory: 2.8M
         CGroup: /system.slice/node_exporter.service
                 └─11442 /opt/node_exporter/node_exporter
    
    Jan 26 14:33:55 vagrant node_exporter[11442]: ts=2022-01-26T14:33:55.462Z caller=node_exporter.go:115 level=info collector=thermal_zone
    Jan 26 14:33:55 vagrant node_exporter[11442]: ts=2022-01-26T14:33:55.462Z caller=node_exporter.go:115 level=info collector=time
    Jan 26 14:33:55 vagrant node_exporter[11442]: ts=2022-01-26T14:33:55.462Z caller=node_exporter.go:115 level=info collector=timex
    Jan 26 14:33:55 vagrant node_exporter[11442]: ts=2022-01-26T14:33:55.462Z caller=node_exporter.go:115 level=info collector=udp_queues
    Jan 26 14:33:55 vagrant node_exporter[11442]: ts=2022-01-26T14:33:55.462Z caller=node_exporter.go:115 level=info collector=uname
    Jan 26 14:33:55 vagrant node_exporter[11442]: ts=2022-01-26T14:33:55.462Z caller=node_exporter.go:115 level=info collector=vmstat
    Jan 26 14:33:55 vagrant node_exporter[11442]: ts=2022-01-26T14:33:55.462Z caller=node_exporter.go:115 level=info collector=xfs
    Jan 26 14:33:55 vagrant node_exporter[11442]: ts=2022-01-26T14:33:55.463Z caller=node_exporter.go:115 level=info collector=zfs
    Jan 26 14:33:55 vagrant node_exporter[11442]: ts=2022-01-26T14:33:55.463Z caller=node_exporter.go:199 level=info msg="Listening on" address=:9100
    Jan 26 14:33:55 vagrant node_exporter[11442]: ts=2022-01-26T14:33:55.463Z caller=tls_config.go:195 level=info msg="TLS is disabled." http2=false

    $ ps -ef|grep node
    vagrant    11537       1  0 14:33 ?        00:00:00 /opt/node_exporter/node_exporter --log.level=warn

Остановка

    $ sudo systemctl stop node_exporter.service
    $ sudo systemctl status node_exporter.service
    ● node_exporter.service - Node exporter
         Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
         Active: inactive (dead) since Wed 2022-01-26 14:37:01 UTC; 2s ago
        Process: 11490 ExecStart=/opt/node_exporter/node_exporter $ARGS (code=killed, signal=TERM)
        Process: 11512 ExecStop=/bin/kill -TERM $MAINPID (code=exited, status=0/SUCCESS)
       Main PID: 11490 (code=killed, signal=TERM)
    
    Jan 26 14:36:41 vagrant systemd[1]: Started Node exporter.
    Jan 26 14:37:01 vagrant systemd[1]: Stopping Node exporter...
    Jan 26 14:37:01 vagrant systemd[1]: node_exporter.service: Succeeded.
    Jan 26 14:37:01 vagrant systemd[1]: Stopped Node exporter.

Перезагрузка ВМ

    $ sudo reboot
    Connection to 127.0.0.1 closed by remote host.
    Connection to 127.0.0.1 closed.
    macbook0P0LYWK:ubunta kmankov$ vagrant ssh
    Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)
      System information as of Wed 26 Jan 2022 02:41:23 PM UTC

      System load:  0.57               Processes:             144
      Usage of /:   12.7% of 30.88GB   Users logged in:       0
      Memory usage: 16%                IPv4 address for eth0: 10.0.2.15
      Swap usage:   0%

    Last login: Sun Jan 23 07:58:26 2022 from 10.0.2.2

    $ ps -ef|grep node
    vagrant      654       1  0 14:41 ?        00:00:00 /opt/node_exporter/node_exporter --log.level=warn
    vagrant     1340    1319  0 14:41 pts/0    00:00:00 grep --color=auto node

    $ sudo systemctl status node_exporter.service
    ● node_exporter.service - Node exporter
         Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
         Active: active (running) since Sun 2022-01-23 18:23:02 UTC; 2 days ago
       Main PID: 654 (node_exporter)
          Tasks: 5 (limit: 1659)
         Memory: 13.9M
         CGroup: /system.slice/node_exporter.service
                 └─654 /opt/node_exporter/node_exporter --log.level=warn
    
    Jan 23 18:23:02 vagrant systemd[1]: Started Node exporter.

## Задание 2

Включенных по умолчанию коллекторов довольно много, они охватывают практически все статистики ОС. 
Отключены по умолчанию те коллекторы, которые довольно тяжелы для повседневного использования.

для базового мониторинга хоста по CPU, памяти, диску и сети:

    --collector.cpu           Exposes CPU statistics
    --collector.meminfo       Exposes memory statistics.
    --collector.diskstats     Exposes disk I/O statistics.
    --collector.netstat       Exposes network statistics from /proc/net/netstat

    $ cat node_exporter.conf
    ARGS="
    --collector.disable-defaults
    --collector.cpu
    --collector.diskstats
    --collector.netstat
    --collector.meminfo
    --log.level=warn
    "

## Задание 3

## Задание 4

## Задание 

## Задание 

## Задание 


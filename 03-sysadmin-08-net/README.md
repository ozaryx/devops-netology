# Домашнее задание к занятию "3.8. Компьютерные сети, лекция 3"

## Задание 1.
Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP

```
telnet route-views.routeviews.org
Username: rviews
show ip route x.x.x.x/32
show bgp x.x.x.x/32
```

```shell
route-views>show ip route 188.162.1.56  
Routing entry for 188.162.1.0/24
  Known via "bgp 6447", distance 20, metric 0
  Tag 6939, type external
  Last update from 64.71.137.241 1w0d ago
  Routing Descriptor Blocks:
  * 64.71.137.241, from 64.71.137.241, 1w0d ago
      Route metric is 0, traffic share count is 1
      AS Hops 3
      Route tag 6939
      MPLS label: none
```

```shell
route-views>show bgp 188.162.1.56        
BGP routing table entry for 188.162.1.0/24, version 306464498
Paths: (22 available, best #22, table default)
...
  Refresh Epoch 1
  20130 6939 31133 31205, (aggregated by 65426 10.104.236.33)
    140.192.8.16 from 140.192.8.16 (140.192.8.16)
      Origin IGP, localpref 100, valid, external
      path 7FE03D990BF8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1351 6939 31133 31205, (aggregated by 65426 10.104.236.33)
    132.198.255.253 from 132.198.255.253 (132.198.255.253)
      Origin IGP, localpref 100, valid, external
      path 7FE184C733A8 RPKI State valid
      rx pathid: 0, tx pathid: 0
...
  Refresh Epoch 1
  6939 31133 31205, (aggregated by 65426 10.104.236.33)
    64.71.137.241 from 64.71.137.241 (216.218.252.164)
      Origin IGP, localpref 100, valid, external, best
      path 7FE0354F0830 RPKI State valid
      rx pathid: 0, tx pathid: 0x0

```

## Задание 2. 
Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.

```shell
vagrant@vagrant:~$ sudo su
root@vagrant:/home/vagrant# ip link add dev dum0 type dummy

root@vagrant:/home/vagrant# ip link show dum0
3: dum0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 22:13:45:15:1b:29 brd ff:ff:ff:ff:ff:ff

root@vagrant:/home/vagrant# ip address add 192.168.99.9/30 dev dum0

root@vagrant:/home/vagrant# ip address show dum0
3: dum0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 22:13:45:15:1b:29 brd ff:ff:ff:ff:ff:ff
    inet 192.168.99.9/30 scope global dum0
       valid_lft forever preferred_lft forever
```

Для поднятия интерфейса после перезагрузки надо создать конфигурацию интерфейса через systemd-networkd
```shell
root@vagrant:/home/vagrant# cat <<EOF > /etc/systemd/network/dum0.netdev
> [NetDev]
> Name=dum0
> Kind=dummy
> EOF

root@vagrant:/home/vagrant# cat <<EOF > /etc/systemd/network/dum0.network
> [Match]
> Name=dum0
>  
> [Network]
> Address=192.168.98.9/32
> EOF

root@vagrant:/home/vagrant# ip l
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:b1:28:5d brd ff:ff:ff:ff:ff:ff

root@vagrant:/home/vagrant# systemctl restart systemd-networkd.service

root@vagrant:/home/vagrant# ip l
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:b1:28:5d brd ff:ff:ff:ff:ff:ff
3: dum0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/ether 96:a9:55:aa:08:91 brd ff:ff:ff:ff:ff:ff

root@vagrant:/home/vagrant# ip a s dum0
3: dum0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default qlen 1000
    link/ether 96:a9:55:aa:08:91 brd ff:ff:ff:ff:ff:ff
    inet 192.168.98.9/32 scope global dum0
       valid_lft forever preferred_lft forever
    inet6 fe80::94a9:55ff:feaa:891/64 scope link 
       valid_lft forever preferred_lft forever
```
```shell
root@vagrant:/home/vagrant# ip route 
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100 
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15 
10.0.2.2 dev eth0 proto dhcp scope link src 10.0.2.15 metric 100 
```
```shell
root@vagrant:/home/vagrant# ip route add 192.168.200.0/24 via 192.168.98.9
root@vagrant:/home/vagrant# ip route add 192.168.0.0/24 via 10.0.2.2
```

```shell
root@vagrant:/home/vagrant# ip route
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100 
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15 
10.0.2.2 dev eth0 proto dhcp scope link src 10.0.2.15 metric 100 
192.168.0.0/24 via 10.0.2.2 dev eth0 
192.168.200.0/24 via 192.168.98.9 dev dum0 
```

## Задание 4.
Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров.

```shell
vagrant@vagrant:~$ ss -tnap
Netid       State        Recv-Q       Send-Q              Local Address:Port              Peer Address:Port        Process                                       
tcp         LISTEN       0            4096                      0.0.0.0:19999                  0.0.0.0:*                                                         
tcp         LISTEN       0            4096                127.0.0.53%lo:53                     0.0.0.0:*                                                         
tcp         LISTEN       0            128                       0.0.0.0:22                     0.0.0.0:*                                                         
tcp         LISTEN       0            4096                    127.0.0.1:8125                   0.0.0.0:*                                                         
tcp         ESTAB        0            0                       10.0.2.15:22                    10.0.2.2:56957                                                     
tcp         LISTEN       0            4096                            *:9100                         *:*            users:(("node_exporter",pid=654,fd=3))       
tcp         LISTEN       0            128                          [::]:22                        [::]:*                                                         
```
127.0.0.53%lo:53 - ДНС  
0.0.0.0:22 - SSH  
*:9100 - node_exporter  

## Задание 5.
Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?
```shell
vagrant@vagrant:~$ ss -unap
State              Recv-Q             Send-Q                          Local Address:Port                         Peer Address:Port            Process            
UNCONN             0                  0                                   127.0.0.1:8125                              0.0.0.0:*                                  
UNCONN             0                  0                               127.0.0.53%lo:53                                0.0.0.0:*                                  
UNCONN             0                  0                              10.0.2.15%eth0:68                                0.0.0.0:*                                  
```

## Задание 6.
Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали. 

Файл [VideoNetDiagram.drawio](https://github.com/ozaryx/devops-netology/blob/main/03-sysadmin-08-net/VideoNetDiagram.drawio)

 ---
## Задание для самостоятельной отработки (необязательно к выполнению)

6*. Установите Nginx, настройте в режиме балансировщика TCP или UDP.

7*. Установите bird2, настройте динамический протокол маршрутизации RIP.

8*. Установите Netbox, создайте несколько IP префиксов, используя curl проверьте работу API.

 ---

## Как сдавать задания

Обязательными к выполнению являются задачи без указания звездочки. Их выполнение необходимо для получения зачета и диплома о профессиональной переподготовке.

Задачи со звездочкой (*) являются дополнительными задачами и/или задачами повышенной сложности. Они не являются обязательными к выполнению, но помогут вам глубже понять тему.

Домашнее задание выполните в файле readme.md в github репозитории. В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории.

Также вы можете выполнить задание в [Google Docs](https://docs.google.com/document/u/0/?tgif=d) и отправить в личном кабинете на проверку ссылку на ваш документ.
Название файла Google Docs должно содержать номер лекции и фамилию студента. Пример названия: "1.1. Введение в DevOps — Сусанна Алиева".

Если необходимо прикрепить дополнительные ссылки, просто добавьте их в свой Google Docs.

Перед тем как выслать ссылку, убедитесь, что ее содержимое не является приватным (открыто на комментирование всем, у кого есть ссылка), иначе преподаватель не сможет проверить работу. Чтобы это проверить, откройте ссылку в браузере в режиме инкогнито.

[Как предоставить доступ к файлам и папкам на Google Диске](https://support.google.com/docs/answer/2494822?hl=ru&co=GENIE.Platform%3DDesktop)

[Как запустить chrome в режиме инкогнито ](https://support.google.com/chrome/answer/95464?co=GENIE.Platform%3DDesktop&hl=ru)

[Как запустить  Safari в режиме инкогнито ](https://support.apple.com/ru-ru/guide/safari/ibrw1069/mac)

Любые вопросы по решению задач задавайте в чате учебной группы.

---


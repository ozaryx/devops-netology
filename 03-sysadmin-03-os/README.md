## Задание 1 
chdir("/tmp")

## Задание 2 
Бинарный файл "/usr/share/misc/magic.mgc" является базой данных паттернов различных типов файлов.  
Системный вызов к файлу "/usr/share/misc/magic.mgc"  

    openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3  

Описание файла "/usr/share/misc/magic.mgc" можно посмотреть в документации

    man magic

## Задание 3 
Запустил редактор и перевел его в фон  

    vagrant@vagrant:~$ vi test.txt
    Ctrl-z
    [1]+  Stopped                 vi test.txt

Нашел какой файл открыт редактором

    vagrant@vagrant:~$ ps aux |grep "vi test.txt"
    vagrant     1606  0.0  0.6  23644  9816 pts/0    T    08:20   0:00 vi test.txt

    vagrant@vagrant:~$ lsof | grep test.txt
    vi        1606                        vagrant    4u      REG              253,0     4096    1048613 /home/vagrant/.test.txt.swp
    vagrant@vagrant:~$ ls -l /proc/1606/fd/4
    total 0
    lrwx------ 1 vagrant vagrant 64 Jan 23 08:20 4 -> /home/vagrant/.test.txt.swp

Удалил файл

    vagrant@vagrant:~$ rm -f /home/vagrant/.test.txt.swp

    vagrant@vagrant:~$ ls -l /proc/1606/fd/4
    total 0
    lrwx------ 1 vagrant vagrant 64 Jan 23 08:20 4 -> '/home/vagrant/.test.txt.swp (deleted)'
    vagrant@vagrant:~$ lsof | grep test.txt
    vi        1606                        vagrant    4u      REG              253,0     4096    1048613 /home/vagrant/.test.txt.swp (deleted)

Файл удален, доступа к нему нет

    vagrant@vagrant:~$ ls -l /home/vagrant/.test.txt.swp
    ls: cannot access '/home/vagrant/.test.txt.swp': No such file or directory

Но можно работать с дескриптором файла

    vagrant@vagrant:~$ cat /dev/null >/proc/1606/fd/4

## Задание 4 
По определению процесс-зомби не занимает никаких ресурсов. (Процесс при завершении (как нормальном, так и в результате не обрабатываемого сигнала) освобождает все свои ресурсы и становится «зомби» — пустой записью в таблице процессов, хранящей статус завершения, предназначенный для чтения родительским процессом.)

## Задание 5 
opensnoop  traces  the open() syscall, showing which processes are attempting to open which files. This can be useful for determining the
       location of config and log files, or for troubleshooting applications that are failing, specially on startup.

vagrant@vagrant:~$ sudo opensnoop-bpfcc
    PID    COMM               FD ERR PATH
    863    vminfo              5   0 /var/run/utmp
    644    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
    644    dbus-daemon        19   0 /usr/share/dbus-1/system-services
    644    dbus-daemon        -1   2 /lib/dbus-1/system-services
    644    dbus-daemon        19   0 /var/lib/snapd/dbus-1/system-services/
    396    systemd-udevd      14   0 /sys/fs/cgroup/unified/system.slice/systemd-udevd.service/cgroup.procs
    396    systemd-udevd      14   0 /sys/fs/cgroup/unified/system.slice/systemd-udevd.service/cgroup.threads
    651    irqbalance          6   0 /proc/interrupts
    651    irqbalance          6   0 /proc/stat

## Задание 6 
 uname -a использует системный вызов  uname()  

    Part of the utsname information is also accessible via  
       /proc/sys/kernel/{ostype, hostname, osrelease, version,  
       domainname}.

## Задание 7 
Команды разделенные ; выполняются последовательно друг за другом.  
Команда следующая после && выполнится только в том случае, если команда перед && завершилась без ошибок, 
т.е. с кодом завершения 0.

set -e останавливает выполнение скрипта при завершении выполнения команды с ненулевым кодом. 
Следовательно, выполнение связки команд через && будет работать без изменений. Но можно и просто заменить && на ; - 
логика выполнения не изменится.

## Задание 8 
set 

-e - останавливает выполнение скрипта/сеанса при ошибке любой команды
-u - останавливает выполнение скрипта/сеанса, если встречается использование переменной, которая раньше нигде не объявлялась
-x - выводит значения переменных
-o pipefail - выводит код завершения всего пайплайна кодом завершения команды с ошибкой, а не кодом завершения последней команды.

Это сочетание может быть полезно при отладке скриптов для выявления всех неявных ошибок.

## Задание 9 

    vagrant@vagrant:~$ ps --no-headers -eo stat | sort | uniq -c
      9 I
     40 I<
      1 R+
     29 S
      2 S+
      7 S<
      1 S<s
      1 SLsl
      2 SN
      1 Sl
     13 Ss
      1 Ss+
      8 Ssl

Большинство процессов находится в состоянии S (interruptible sleep (waiting for an event to complete)) -

PROCESS STATE CODES
       Here are the different values that the s, stat and state output specifiers (header "STAT" or "S") will display to describe the state of a
       process:
               D    uninterruptible sleep (usually IO)
               I    Idle kernel thread
               R    running or runnable (on run queue)
               S    interruptible sleep (waiting for an event to complete)
               T    stopped by job control signal
               t    stopped by debugger during the tracing
               W    paging (not valid since the 2.6.xx kernel)
               X    dead (should never be seen)
               Z    defunct ("zombie") process, terminated but not reaped by its parent

       For BSD formats and when the stat keyword is used, additional characters may be displayed:
               <    high-priority (not nice to other users)
               N    low-priority (nice to other users)
               L    has pages locked into memory (for real-time and custom IO)
               s    is a session leader
               l    is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
               +    is in the foreground process group

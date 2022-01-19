## Задание 1 
cd  это встроенная команда  bash

    $ type cd
    cd is a shell builtin

## Задание 2

    grep <some_string> <some_file> | wc -l  =>  grep -c <some_string> <some_file>

## Задание 3

    vagrant@vagrant:~$ ps p 1
        PID TTY      STAT   TIME COMMAND
        1 ?        Ss     0:06 /sbin/init

## Задание 4
### Session 2

    vagrant@vagrant:~$ lsof -p $$
    COMMAND   PID    USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
    ...
    bash    14613 vagrant    0u   CHR  136,1      0t0       4 /dev/pts/1
    bash    14613 vagrant    1u   CHR  136,1      0t0       4 /dev/pts/1
    bash    14613 vagrant    2u   CHR  136,1      0t0       4 /dev/pts/1
    bash    14613 vagrant  255u   CHR  136,1      0t0       4 /dev/pts/1

    vagrant@vagrant:~$ ps -p $$
        PID TTY          TIME CMD
      14512 pts/1    00:00:00 bash
    
    vagrant@vagrant:~$ ls -l /proc/$$/fd
    total 0
    lrwx------ 1 vagrant vagrant 64 Jan 17 14:38 0 -> /dev/pts/1
    lrwx------ 1 vagrant vagrant 64 Jan 17 14:38 1 -> /dev/pts/1
    lrwx------ 1 vagrant vagrant 64 Jan 17 14:38 2 -> /dev/pts/1
    lrwx------ 1 vagrant vagrant 64 Jan 17 14:39 255 -> /dev/pts/1

### Session 1

    vagrant@vagrant:~$ ls /abc 2>/dev/pts/1

### Session 2

    vagrant@vagrant:~$ ls: cannot access '/abc': No such file or directory

## Задание 5
Получится

    vagrant@vagrant:~$ cat list.txt | grep testcase > grep.txt

## Задание 6



## Задание 7
## Задание 8
## Задание 9
## Задание 10
## Задание 11
## Задание 12
## Задание 13
## Задание 14

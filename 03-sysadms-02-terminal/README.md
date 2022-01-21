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

    vagrant@vagrant:~$ grep testcase < list.txt > grep.txt

## Задание 6
Если у пользователя PTY есть права писать в устройство эмулятора TTY, то можно выводить данные из PTY в TTY. 

## Задание 7
bash 5>&1 - Создаст новый сеанс bash и дополнительный файловый дескриптор 5 с перенаправлением в ФД 1.

    vagrant@vagrant:~$ bash 5>&1
    vagrant@vagrant:~$ ls -l /proc/$$/fd
    total 0
    lrwx------ 1 vagrant vagrant 64 Jan 20 14:46 0 -> /dev/pts/0
    lrwx------ 1 vagrant vagrant 64 Jan 20 14:46 1 -> /dev/pts/0
    lrwx------ 1 vagrant vagrant 64 Jan 20 14:46 2 -> /dev/pts/0
    lrwx------ 1 vagrant vagrant 64 Jan 20 14:46 255 -> /dev/pts/0
    lrwx------ 1 vagrant vagrant 64 Jan 20 14:46 5 -> /dev/pts/0

echo netology > /proc/$$/fd/5 - Выведет в stdout "netology" поскольку ФД 5 переведен в ФД 1.
 
## Задание 8
Можно использовать переключение потоков ввода вывода 3>&1 1>&2 2>&3

    vagrant@vagrant:~$ ls /proc/$$/fd 3>&1 1>&2 2>&3 | cat > test_stdout.txt
    0  1  2  255
    vagrant@vagrant:~$ cat test_stdout.txt

    vagrant@vagrant:~$ ls /abc 3>&1 1>&2 2>&3 | cat > test_err.txt 
    vagrant@vagrant:~$ cat test_err.txt 
    ls: cannot access '/abc': No such file or directory

## Задание 9
cat /proc/$$/environ - выведет переменные окружения текущего сеанса bash  
команда env также выведет этот список  

## Задание 10
    /proc/<PID>/cmdline - полная строка команды запуска процесса  
    /proc/<PID>/exe - символическая ссылка на исполняемый файл команды  

## Задание 11
sse4_2

    cat /proc/cpuinfo | grep sse
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single pti fsgsbase avx2 invpcid rdseed clflushopt md_clear flush_l1d

## Задание 12
ssh  по умолчанию не запускает псевдо-терминал для выполнения переданной команды.
чтобы запустить псевдо-терминал нужно указать параметр -t

    vagrant@vagrant:~$ ssh -t localhost 'tty'
    vagrant@localhost's password: 
    /dev/pts/1

## Задание 13
Запустить новый сеанс screen или подключиться к существующему.
Выполнить переключение нужного процесса командой reptyr PID

## Задание 14
echo выводит строки текста в stdout  
tee  читает stdin и выводит в stdout или файл  

 команда tee запущенная с правами root примет на stdin stdout команды echo и запишет в файл в домашнем каталоге пользователя root

## Задание 4. 

    macbook0P0LYWK:ubunta kmankov$ pwd
    /Users/kmankov/ubunta

    macbook0P0LYWK:ubunta kmankov$ ls -l
    total 8
    -rw-r--r--  1 kmankov  staff  3024 Dec 14 23:08 Vagrantfile

    macbook0P0LYWK:ubunta kmankov$ grep -Ev '^#.*$|^ *#.*$|^ *$' Vagrantfile 
    Vagrant.configure("2") do |config|
      config.vm.box = "bento/ubuntu-20.04"
    end

    macbook0P0LYWK:ubunta kmankov$ vagrant up
    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Checking if box 'bento/ubuntu-20.04' version '202107.28.0' is up to date...
    ==> default: A newer version of the box 'bento/ubuntu-20.04' for provider 'virtualbox' is
    ==> default: available! You currently have version '202107.28.0'. The latest is version
    ==> default: '202112.19.0'. Run `vagrant box update` to update.
    ==> default: Resuming suspended VM...
    ==> default: Booting VM...
    ==> default: Waiting for machine to boot. This may take a few minutes...
        default: SSH address: 127.0.0.1:2222
        default: SSH username: vagrant
        default: SSH auth method: private key
    ==> default: Machine booted and ready!
    ==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
    ==> default: flag to force provisioning. Provisioners marked to run always will still run.

    macbook0P0LYWK:ubunta kmankov$ vagrant suspend
    ==> default: Saving VM state and suspending execution...

    macbook0P0LYWK:ubunta kmankov$ vagrant up
    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Checking if box 'bento/ubuntu-20.04' version '202107.28.0' is up to date...
    ==> default: Resuming suspended VM...
    ==> default: Booting VM...
    ==> default: Waiting for machine to boot. This may take a few minutes...
        default: SSH address: 127.0.0.1:2222
        default: SSH username: vagrant
        default: SSH auth method: private key
    ==> default: Machine booted and ready!
    ==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
    ==> default: flag to force provisioning. Provisioners marked to run always will still run.

## Задание 5.

![](img/VirtBoxVM.png)

Выделено 1Гб оперативной памяти и 2 процессора. 
Создан виртуальный диск 64Гб с авторасширением.
Настроен сетевой адаптер.

Все параметры ВМ настроены по умолчанию, так как при создании ВМ не было указано никаких параметров.

## Задание 6.

Нужно добавить в Vagrantfile параметры выделения памяти и процессоров

    Vagrant.configure("2") do |config|
      config.vm.box = "bento/ubuntu-20.04"
      config.vm.provider "virtualbox" do |v|
        v.memory = 1524
        v.cpus = 3
      end
    end

## Задание 7.

    macbook0P0LYWK:ubunta kmankov$ vagrant ssh
    Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)
        Documentation:  https://help.ubuntu.com
        Management:     https://landscape.canonical.com
        Support:        https://ubuntu.com/advantage
    System information as of Wed 05 Jan 2022 06:58:41 AM UTC
        System load:  1.12               Processes:             132
        Usage of /:   11.6% of 30.88GB   Users logged in:       0
        Memory usage: 14%                IPv4 address for eth0: 10.0.2.15
        Swap usage:   0%

    This system is built by the Bento project by Chef Software
    More information can be found at https://github.com/chef/bento


    vagrant@vagrant:~$ pwd
    /home/vagrant

    vagrant@vagrant:~$ ls -l
    total 0
    vagrant@vagrant:~$ pwd
    /home/vagrant
    vagrant@vagrant:~$ touch test.txt
    vagrant@vagrant:~$ ls -l
    total 0
    -rw-rw-r-- 1 vagrant vagrant 0 Jan  5 06:59 test.txt
    vagrant@vagrant:~$ vi test.txt 
    vagrant@vagrant:~$ ls -l
    total 4
    -rw-rw-r-- 1 vagrant vagrant 82 Jan  5 06:59 test.txt

    vagrant@vagrant:~$ cat test.txt 
    test
    
    #test
     test
    test
    test
    test

    vagrant@vagrant:~$ alias
    alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
    alias egrep='egrep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias grep='grep --color=auto'
    alias l='ls -CF'
    alias la='ls -A'
    alias ll='ls -alF'
    alias ls='ls --color=auto'

    vagrant@vagrant:~$ lt
    -bash: lt: command not found
    vagrant@vagrant:~$ alias lt='ls -lt'
    vagrant@vagrant:~$ lt
    total 4
    -rw-rw-r-- 1 vagrant vagrant 33 Jan  5 07:30 test.txt

    vagrant@vagrant:~$ alias lt='ll -t'
    vagrant@vagrant:~$ lt
    total 48
    drwxr-xr-x 4 vagrant vagrant 4096 Jan  5 07:30 ./
    -rw------- 1 vagrant vagrant 1535 Jan  5 07:30 .viminfo
    -rw-rw-r-- 1 vagrant vagrant   33 Jan  5 07:30 test.txt
    -rw------- 1 vagrant vagrant   37 Jan  5 07:18 .lesshst
    drwx------ 2 vagrant root    4096 Jan  5 06:56 .ssh/
    drwxr-xr-x 3 root    root    4096 Dec 19 19:42 ../
    -rw-r--r-- 1 vagrant vagrant  220 Feb 25  2020 .bash_logout
    -rw-r--r-- 1 vagrant vagrant 3771 Feb 25  2020 .bashrc
    -rw-r--r-- 1 vagrant vagrant  807 Feb 25  2020 .profile

    vagrant@vagrant:~$ type type
    type is a shell builtin
    vagrant@vagrant:~$ type -a pwd
    pwd is a shell builtin
    pwd is /usr/bin/pwd
    pwd is /bin/pwd
    vagrant@vagrant:~$ type {
    { is a shell keyword

    vagrant@vagrant:~$ env pwd
    /home/vagrant
    vagrant@vagrant:~$ cp test.txt test0.txt
    vagrant@vagrant:~$ vi test.txt
    vagrant@vagrant:~$ diff test.txt test0.txt
    7,9c7
    < testtesttest
    < 
    < 
    ---
    > test

    vagrant@vagrant:~$ mv test.txt test1.txt
    vagrant@vagrant:~$ ls -lt
    total 8
    -rw-rw-r-- 1 vagrant vagrant 43 Jan  5 07:44 test1.txt
    -rw-rw-r-- 1 vagrant vagrant 33 Jan  5 07:43 test0.txt
    vagrant@vagrant:~$ rm test*.txt
    vagrant@vagrant:~$ ls -lt
    total 0

## Задание 8.

* строка 710 HISTFILESIZE - The maximum number of lines contained in the history file. The shell sets the default value to the value of HISTSIZE after reading any startup files.
* строка 722 HISTSIZE - The number of commands to remember in the command history.

* HISTCONTROL - A  colon-separated  list  of  values controlling how commands are saved on the history list. A value of ignoreboth is shorthand for ignorespace and ignoredups.
  Убирает дубликаты команд  и команды начинающиеся с пробелов.

## Задание 9.

{ } - зарезервированные слова bash. Позволяют группировать команды в группу. Служат для описания функций.
    Также служат для создания расширений.
    Например, команда 

    vagrant@vagrant:~$ touch {one,two}.txt

Создаст два файла

    vagrant@vagrant:~$ ls
    one.txt
    two.txt 

## Задание 10.

    vagrant@vagrant:~$ touch brace{000001..100000}.txt
    -bash: /usr/bin/touch: Argument list too long

Создать одной командой не получится, слишком много аргументов для команды.

## Задание 11.

[[ expression ]] служит для проверки истинности выражения
[[ -d /tmp ]] - проверяет существование каталога /tmp, если каталог существует, результат будет 0, иначе 1.

## Задание 12.

    vagrant@vagrant:~$ type -a bash
    bash is /usr/local/bin/bash
    bash is /bin/bash

    vagrant@vagrant:~$ env|grep PATH
    PATH=/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

    vagrant@vagrant:~$ mkdir /tmp/new_path_directory
    vagrant@vagrant:~$ ln -s /bin/bash /tmp/new_path_directory/bash
    vagrant@vagrant:~$ export PATH=/Library/Frameworks/Python.framework/Versions/3.9/bin:/tmp/new_path_directory:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
    vagrant@vagrant:~$ type -a bash
    bash is /tmp/new_path_directory/bash
    bash is /usr/local/bin/bash
    bash is /bin/bash

## Задание 13.

at - выполняет команду в назначенное время
batch - выполняет команду если средняя загрузка системы меньше определенного уровня

## Задание 14.

    macbook0P0LYWK:ubunta kmankov$ vagrant halt
    ==> default: Attempting graceful shutdown of VM...

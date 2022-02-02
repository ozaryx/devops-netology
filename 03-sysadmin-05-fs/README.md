## Задание 1
Разрежённый файл (англ. sparse file) — файл, в котором последовательности нулевых байтов[1] заменены на информацию об этих последовательностях (список дыр).

Дыра (англ. hole) — последовательность нулевых байт внутри файла, не записанная на диск. Информация о дырах (смещение от начала файла в байтах и количество байт) хранится в метаданных ФС.

## Задание 2
Не могут, потому что права и владелец назначаются файлу. Имя файла это жесткая ссылка на индексный дескриптор файла. 
Не важно сколько жестких ссылок будет ссылаться на файл, все они указывают на один и тот же индексный дескриптор.

Пример,

    root@vagrant:~# touch test1
    root@vagrant:~# stat test1
      File: test1
      Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
    Device: fd00h/64768d	Inode: 1703948     Links: 1
    Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
    Access: 2022-02-02 14:57:07.590326988 +0000
    Modify: 2022-02-02 14:57:07.590326988 +0000
    Change: 2022-02-02 14:57:07.590326988 +0000
     Birth: -

    root@vagrant:~# ln test1 test2

    root@vagrant:~# stat test2
      File: test2
      Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
    Device: fd00h/64768d	Inode: 1703948     Links: 2
    Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
    Access: 2022-02-02 14:57:07.590326988 +0000
    Modify: 2022-02-02 14:57:07.590326988 +0000
    Change: 2022-02-02 14:57:25.027040927 +0000
     Birth: -

    root@vagrant:~# ls -l test[12]
    -rw-r--r-- 2 root root 0 Feb  2 14:57 test1
    -rw-r--r-- 2 root root 0 Feb  2 14:57 test2

    root@vagrant:~# chmod u+x test1

    root@vagrant:~# ls -l test[12]
    -rwxr--r-- 2 root root 0 Feb  2 14:57 test1
    -rwxr--r-- 2 root root 0 Feb  2 14:57 test2

    root@vagrant:~# stat test[12]
      File: test1
      Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
    Device: fd00h/64768d	Inode: 1703948     Links: 2
    Access: (0744/-rwxr--r--)  Uid: (    0/    root)   Gid: (    0/    root)
    Access: 2022-02-02 14:57:07.590326988 +0000
    Modify: 2022-02-02 14:57:07.590326988 +0000
    Change: 2022-02-02 14:58:08.536784757 +0000
     Birth: -
      File: test2
      Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
    Device: fd00h/64768d	Inode: 1703948     Links: 2
    Access: (0744/-rwxr--r--)  Uid: (    0/    root)   Gid: (    0/    root)
    Access: 2022-02-02 14:57:07.590326988 +0000
    Modify: 2022-02-02 14:57:07.590326988 +0000
    Change: 2022-02-02 14:58:08.536784757 +0000
     Birth: -

    root@vagrant:~# chown root:staff test1

    root@vagrant:~# ls -l test[12]
    -rwxr--r-- 2 root staff 0 Feb  2 14:57 test1
    -rwxr--r-- 2 root staff 0 Feb  2 14:57 test2

    root@vagrant:~# stat test[12]
      File: test1
      Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
    Device: fd00h/64768d	Inode: 1703948     Links: 2
    Access: (0744/-rwxr--r--)  Uid: (    0/    root)   Gid: (   50/   staff)
    Access: 2022-02-02 14:57:07.590326988 +0000
    Modify: 2022-02-02 14:57:07.590326988 +0000
    Change: 2022-02-02 14:58:44.894954623 +0000
     Birth: -
      File: test2
      Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
    Device: fd00h/64768d	Inode: 1703948     Links: 2
    Access: (0744/-rwxr--r--)  Uid: (    0/    root)   Gid: (   50/   staff)
    Access: 2022-02-02 14:57:07.590326988 +0000
    Modify: 2022-02-02 14:57:07.590326988 +0000
    Change: 2022-02-02 14:58:44.894954623 +0000
     Birth: -


## Задание 3

    macbook0P0LYWK:~ kmankov$ mkdir sysadmin-05
    macbook0P0LYWK:~ kmankov$ cd !$
    cd sysadmin-05
    macbook0P0LYWK:sysadmin-05 kmankov$ vagrant init
    macbook0P0LYWK:sysadmin-05 kmankov$ vi Vagrantfile
    macbook0P0LYWK:sysadmin-05 kmankov$ vagrant up
    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Importing base box 'bento/ubuntu-20.04'...
    ==> default: Matching MAC address for NAT networking...
    ==> default: Checking if box 'bento/ubuntu-20.04' version '202112.19.0' is up to date...
    ==> default: Setting the name of the VM: sysadmin-05_default_1643643921334_8386
    ==> default: Clearing any previously set network interfaces...
    ==> default: Preparing network interfaces based on configuration...
        default: Adapter 1: nat

    
    vagrant@vagrant:~$ ls -l /dev/sd*
    brw-rw---- 1 root disk 8,  0 Jan 31 15:46 /dev/sda
    brw-rw---- 1 root disk 8,  1 Jan 31 15:46 /dev/sda1
    brw-rw---- 1 root disk 8,  2 Jan 31 15:46 /dev/sda2
    brw-rw---- 1 root disk 8,  3 Jan 31 15:46 /dev/sda3
    brw-rw---- 1 root disk 8, 16 Jan 31 15:46 /dev/sdb
    brw-rw---- 1 root disk 8, 32 Jan 31 15:46 /dev/sdc

## Задание 4

    vagrant@vagrant:~$ sudo -i
    root@vagrant:~# fdisk -l /dev/sdb
    Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
    Disk model: VBOX HARDDISK
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes

    
    root@vagrant:~# fdisk /dev/sdb

    Welcome to fdisk (util-linux 2.34).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.
    
    Device does not contain a recognized partition table.
    Created a new DOS disklabel with disk identifier 0xa1a4cfac.
    
    Command (m for help): n
    Partition type
       p   primary (0 primary, 0 extended, 4 free)
       e   extended (container for logical partitions)
    Select (default p): p
    Partition number (1-4, default 1):
    First sector (2048-5242879, default 2048):
    Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-5242879, default 5242879): +2G

    Created a new partition 1 of type 'Linux' and of size 2 GiB.

    Command (m for help): n
    Partition type
       p   primary (1 primary, 0 extended, 3 free)
       e   extended (container for logical partitions)
    Select (default p): p
    Partition number (2-4, default 2):
    First sector (4196352-5242879, default 4196352):
    Last sector, +/-sectors or +/-size{K,M,G,T,P} (4196352-5242879, default 5242879):
    
    Created a new partition 2 of type 'Linux' and of size 511 MiB.
 
    Command (m for help): p
    Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
    Disk model: VBOX HARDDISK
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0xa1a4cfac
    
    Device     Boot   Start     End Sectors  Size Id Type
    /dev/sdb1          2048 4196351 4194304    2G 83 Linux
    /dev/sdb2       4196352 5242879 1046528  511M 83 Linux

    Command (m for help): w
    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.
    
    root@vagrant:~# fdisk -l /dev/sdb
    Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
    Disk model: VBOX HARDDISK
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0xa1a4cfac
    
    Device     Boot   Start     End Sectors  Size Id Type
    /dev/sdb1          2048 4196351 4194304    2G 83 Linux
    /dev/sdb2       4196352 5242879 1046528  511M 83 Linux

    root@vagrant:~# lsblk
    NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    loop0                       7:0    0 70.3M  1 loop /snap/lxd/21029
    loop1                       7:1    0 32.3M  1 loop /snap/snapd/12704
    loop2                       7:2    0 55.4M  1 loop /snap/core18/2128
    loop3                       7:3    0 55.5M  1 loop /snap/core18/2284
    loop4                       7:4    0 43.4M  1 loop /snap/snapd/14549
    loop5                       7:5    0 61.9M  1 loop /snap/core20/1328
    loop6                       7:6    0 67.2M  1 loop /snap/lxd/21835
    sda                         8:0    0   64G  0 disk
    ├─sda1                      8:1    0    1M  0 part
    ├─sda2                      8:2    0    1G  0 part /boot
    └─sda3                      8:3    0   63G  0 part
      └─ubuntu--vg-ubuntu--lv 253:0    0 31.5G  0 lvm  /
    sdb                         8:16   0  2.5G  0 disk
    ├─sdb1                      8:17   0    2G  0 part
    └─sdb2                      8:18   0  511M  0 part
    sdc                         8:32   0  2.5G  0 disk
    

## Задание 5
    
    root@vagrant:~# man sfdisk

    root@vagrant:~# sfdisk --dump /dev/sdb | sfdisk /dev/sdc

    Checking that no-one is using this disk right now ... OK
    
    Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors
    Disk model: VBOX HARDDISK
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    
    >>> Script header accepted.
    >>> Script header accepted.
    >>> Script header accepted.
    >>> Script header accepted.
    >>> Created a new DOS disklabel with disk identifier 0xa1a4cfac.
    /dev/sdc1: Created a new partition 1 of type 'Linux' and of size 2 GiB.
    /dev/sdc2: Created a new partition 2 of type 'Linux' and of size 511 MiB.
    /dev/sdc3: Done.
    
    New situation:
    Disklabel type: dos
    Disk identifier: 0xa1a4cfac
    
    Device     Boot   Start     End Sectors  Size Id Type
    /dev/sdc1          2048 4196351 4194304    2G 83 Linux
    /dev/sdc2       4196352 5242879 1046528  511M 83 Linux
    
    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.


    root@vagrant:~# fdisk -l /dev/sdc
    Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors
    Disk model: VBOX HARDDISK
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0xa1a4cfac
    
    Device     Boot   Start     End Sectors  Size Id Type
    /dev/sdc1          2048 4196351 4194304    2G 83 Linux
    /dev/sdc2       4196352 5242879 1046528  511M 83 Linux

    root@vagrant:~# lsblk
    NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    loop0                       7:0    0 70.3M  1 loop /snap/lxd/21029
    loop1                       7:1    0 32.3M  1 loop /snap/snapd/12704
    loop2                       7:2    0 55.4M  1 loop /snap/core18/2128
    loop3                       7:3    0 55.5M  1 loop /snap/core18/2284
    loop4                       7:4    0 43.4M  1 loop /snap/snapd/14549
    loop5                       7:5    0 61.9M  1 loop /snap/core20/1328
    loop6                       7:6    0 67.2M  1 loop /snap/lxd/21835
    sda                         8:0    0   64G  0 disk
    ├─sda1                      8:1    0    1M  0 part
    ├─sda2                      8:2    0    1G  0 part /boot
    └─sda3                      8:3    0   63G  0 part
      └─ubuntu--vg-ubuntu--lv 253:0    0 31.5G  0 lvm  /
    sdb                         8:16   0  2.5G  0 disk
    ├─sdb1                      8:17   0    2G  0 part
    └─sdb2                      8:18   0  511M  0 part
    sdc                         8:32   0  2.5G  0 disk
    ├─sdc1                      8:33   0    2G  0 part
    └─sdc2                      8:34   0  511M  0 part


## Задание 6

    mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sd[bc]1

    root@vagrant:~# ls -l /dev/sd[bc]1
    brw-rw---- 1 root disk 8, 17 Jan 31 16:00 /dev/sdb1
    brw-rw---- 1 root disk 8, 33 Jan 31 16:13 /dev/sdc1
    root@vagrant:~# mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sd[bc]1
    mdadm: Note: this array has metadata at the start and
        may not be suitable as a boot device.  If you plan to
        store '/boot' on this device please ensure that
        your boot-loader understands md/v1.x metadata, or use
        --metadata=0.90
    Continue creating array? y
    mdadm: Defaulting to version 1.2 metadata
    mdadm: array /dev/md0 started.

    root@vagrant:~# ls -l /dev/md0
    brw-rw---- 1 root disk 9, 0 Jan 31 16:21 /dev/md0

    root@vagrant:~# lsblk
    NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
    loop0                       7:0    0 70.3M  1 loop  /snap/lxd/21029
    loop1                       7:1    0 32.3M  1 loop  /snap/snapd/12704
    loop2                       7:2    0 55.4M  1 loop  /snap/core18/2128
    loop3                       7:3    0 55.5M  1 loop  /snap/core18/2284
    loop4                       7:4    0 43.4M  1 loop  /snap/snapd/14549
    loop5                       7:5    0 61.9M  1 loop  /snap/core20/1328
    loop6                       7:6    0 67.2M  1 loop  /snap/lxd/21835
    sda                         8:0    0   64G  0 disk
    ├─sda1                      8:1    0    1M  0 part
    ├─sda2                      8:2    0    1G  0 part  /boot
    └─sda3                      8:3    0   63G  0 part
      └─ubuntu--vg-ubuntu--lv 253:0    0 31.5G  0 lvm   /
    sdb                         8:16   0  2.5G  0 disk
    ├─sdb1                      8:17   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    └─sdb2                      8:18   0  511M  0 part
    sdc                         8:32   0  2.5G  0 disk
    ├─sdc1                      8:33   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    └─sdc2                      8:34   0  511M  0 part


## Задание 7

    mdadm --create /dev/md1 --level=0 --raid-devices=2 /dev/sd[bc]2

    root@vagrant:~# mdadm --create /dev/md1 --level=0 --raid-devices=2 /dev/sd[bc]2
    mdadm: Defaulting to version 1.2 metadata
    mdadm: array /dev/md1 started.

    root@vagrant:~# ls -l /dev/md1
    brw-rw---- 1 root disk 9, 1 Jan 31 16:24 /dev/md1

    root@vagrant:~# lsblk
    NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
    loop0                       7:0    0 70.3M  1 loop  /snap/lxd/21029
    loop1                       7:1    0 32.3M  1 loop  /snap/snapd/12704
    loop2                       7:2    0 55.4M  1 loop  /snap/core18/2128
    loop3                       7:3    0 55.5M  1 loop  /snap/core18/2284
    loop4                       7:4    0 43.4M  1 loop  /snap/snapd/14549
    loop5                       7:5    0 61.9M  1 loop  /snap/core20/1328
    loop6                       7:6    0 67.2M  1 loop  /snap/lxd/21835
    sda                         8:0    0   64G  0 disk
    ├─sda1                      8:1    0    1M  0 part
    ├─sda2                      8:2    0    1G  0 part  /boot
    └─sda3                      8:3    0   63G  0 part
      └─ubuntu--vg-ubuntu--lv 253:0    0 31.5G  0 lvm   /
    sdb                         8:16   0  2.5G  0 disk
    ├─sdb1                      8:17   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    └─sdb2                      8:18   0  511M  0 part
      └─md1                     9:1    0 1018M  0 raid0
    sdc                         8:32   0  2.5G  0 disk
    ├─sdc1                      8:33   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    └─sdc2                      8:34   0  511M  0 part
      └─md1                     9:1    0 1018M  0 raid0


## Задание 8

    root@vagrant:~# pvs
      PV         VG        Fmt  Attr PSize   PFree
      /dev/sda3  ubuntu-vg lvm2 a--  <63.00g <31.50g


    root@vagrant:~# man pvcreate
    root@vagrant:~# pvcreate /dev/md0
      Physical volume "/dev/md0" successfully created.
    root@vagrant:~# pvs
      PV         VG        Fmt  Attr PSize   PFree
      /dev/md0             lvm2 ---   <2.00g  <2.00g
      /dev/sda3  ubuntu-vg lvm2 a--  <63.00g <31.50g

    root@vagrant:~# pvcreate /dev/md1
      Physical volume "/dev/md1" successfully created.
    root@vagrant:~# pvs
      PV         VG        Fmt  Attr PSize    PFree
      /dev/md0             lvm2 ---    <2.00g   <2.00g
      /dev/md1             lvm2 ---  1018.00m 1018.00m
      /dev/sda3  ubuntu-vg lvm2 a--   <63.00g  <31.50g

## Задание 9

    root@vagrant:~# man vgcreate
    root@vagrant:~# vgcreate md_vg /dev/md[01]
      Volume group "md_vg" successfully created
 
    root@vagrant:~# vgs
      VG        #PV #LV #SN Attr   VSize   VFree
      md_vg       2   0   0 wz--n-  <2.99g  <2.99g
      ubuntu-vg   1   1   0 wz--n- <63.00g <31.50g

    root@vagrant:~# pvs
      PV         VG        Fmt  Attr PSize    PFree
      /dev/md0   md_vg     lvm2 a--    <2.00g   <2.00g
      /dev/md1   md_vg     lvm2 a--  1016.00m 1016.00m
      /dev/sda3  ubuntu-vg lvm2 a--   <63.00g  <31.50g

## Задание 10
    root@vagrant:~# lvs
      LV        VG        Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
      ubuntu-lv ubuntu-vg -wi-ao---- 31.50g

    root@vagrant:~# lvcreate -L 100m -n r0_lv md_vg /dev/md1
      Logical volume "r0_lv" created.

    root@vagrant:~# lvs
      LV        VG        Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
      r0_lv     md_vg     -wi-a----- 100.00m
      ubuntu-lv ubuntu-vg -wi-ao----  31.50g

    root@vagrant:~# lsblk
    NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
    loop0                       7:0    0 70.3M  1 loop  /snap/lxd/21029
    loop1                       7:1    0 32.3M  1 loop  /snap/snapd/12704
    loop2                       7:2    0 55.4M  1 loop  /snap/core18/2128
    loop3                       7:3    0 55.5M  1 loop  /snap/core18/2284
    loop4                       7:4    0 43.4M  1 loop  /snap/snapd/14549
    loop5                       7:5    0 61.9M  1 loop  /snap/core20/1328
    loop6                       7:6    0 67.2M  1 loop  /snap/lxd/21835
    sda                         8:0    0   64G  0 disk
    ├─sda1                      8:1    0    1M  0 part
    ├─sda2                      8:2    0    1G  0 part  /boot
    └─sda3                      8:3    0   63G  0 part
      └─ubuntu--vg-ubuntu--lv 253:0    0 31.5G  0 lvm   /
    sdb                         8:16   0  2.5G  0 disk
    ├─sdb1                      8:17   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    └─sdb2                      8:18   0  511M  0 part
      └─md1                     9:1    0 1018M  0 raid0
        └─md_vg-r0_lv         253:1    0  100M  0 lvm
    sdc                         8:32   0  2.5G  0 disk
    ├─sdc1                      8:33   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    └─sdc2                      8:34   0  511M  0 part
      └─md1                     9:1    0 1018M  0 raid0
        └─md_vg-r0_lv         253:1    0  100M  0 lvm


## Задание 11

    root@vagrant:~# lvdisplay md_vg/r0_lv
      --- Logical volume ---
      LV Path                /dev/md_vg/r0_lv
      LV Name                r0_lv
      VG Name                md_vg
      LV UUID                gBsvcZ-NddY-FxOq-3JSG-i8Ta-jUwo-nJNUpt
      LV Write Access        read/write
      LV Creation host, time vagrant, 2022-01-31 16:56:16 +0000
      LV Status              available
      # open                 0
      LV Size                100.00 MiB
      Current LE             25
      Segments               1
      Allocation             inherit
      Read ahead sectors     auto
      - currently set to     4096
      Block device           253:1

    root@vagrant:~# ls -l /dev/md_vg/r0_lv
    lrwxrwxrwx 1 root root 7 Jan 31 17:00 /dev/md_vg/r0_lv -> ../dm-1
    
    root@vagrant:~# mkfs.ext4 /dev/dm-1
    mke2fs 1.45.5 (07-Jan-2020)
    Creating filesystem with 25600 4k blocks and 25600 inodes
    
    Allocating group tables: done
    Writing inode tables: done
    Creating journal (1024 blocks): done
    Writing superblocks and filesystem accounting information: done

## Задание 12

    root@vagrant:~# mkdir /tmp/new
    root@vagrant:~# mount /dev/md_vg/r0_lv /tmp/new
    
    root@vagrant:~# mount | grep /tmp/new
    /dev/mapper/md_vg-r0_lv on /tmp/new type ext4 (rw,relatime,stripe=256)

    root@vagrant:~# lsblk
    NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
    loop0                       7:0    0 70.3M  1 loop  /snap/lxd/21029
    loop1                       7:1    0 32.3M  1 loop  /snap/snapd/12704
    loop2                       7:2    0 55.4M  1 loop  /snap/core18/2128
    loop3                       7:3    0 55.5M  1 loop  /snap/core18/2284
    loop4                       7:4    0 43.4M  1 loop  /snap/snapd/14549
    loop5                       7:5    0 61.9M  1 loop  /snap/core20/1328
    loop6                       7:6    0 67.2M  1 loop  /snap/lxd/21835
    sda                         8:0    0   64G  0 disk
    ├─sda1                      8:1    0    1M  0 part
    ├─sda2                      8:2    0    1G  0 part  /boot
    └─sda3                      8:3    0   63G  0 part
      └─ubuntu--vg-ubuntu--lv 253:0    0 31.5G  0 lvm   /
    sdb                         8:16   0  2.5G  0 disk
    ├─sdb1                      8:17   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    └─sdb2                      8:18   0  511M  0 part
      └─md1                     9:1    0 1018M  0 raid0
        └─md_vg-r0_lv         253:1    0  100M  0 lvm   /tmp/new
    sdc                         8:32   0  2.5G  0 disk
    ├─sdc1                      8:33   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    └─sdc2                      8:34   0  511M  0 part
      └─md1                     9:1    0 1018M  0 raid0
        └─md_vg-r0_lv         253:1    0  100M  0 lvm   /tmp/new


## Задание 13

    root@vagrant:~# wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz
    --2022-01-31 17:07:22--  https://mirror.yandex.ru/ubuntu/ls-lR.gz
    Resolving mirror.yandex.ru (mirror.yandex.ru)... 213.180.204.183, 2a02:6b8::183
    Connecting to mirror.yandex.ru (mirror.yandex.ru)|213.180.204.183|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 22018280 (21M) [application/octet-stream]
    Saving to: ‘/tmp/new/test.gz’
    
    /tmp/new/test.gz                100%[=====================================================>]  21.00M  7.29MB/s    in 2.9s
    
    2022-01-31 17:07:26 (7.29 MB/s) - ‘/tmp/new/test.gz’ saved [22018280/22018280]

    root@vagrant:~# ls -l /tmp/new/test.gz
    -rw-r--r-- 1 root root 22018280 Jan 31 14:17 /tmp/new/test.gz


## Задание 14

    root@vagrant:~# lsblk
    NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
    loop0                       7:0    0 32.3M  1 loop  /snap/snapd/12704
    loop1                       7:1    0 55.4M  1 loop  /snap/core18/2128
    loop2                       7:2    0 70.3M  1 loop  /snap/lxd/21029
    loop3                       7:3    0 55.5M  1 loop  /snap/core18/2284
    loop4                       7:4    0 43.4M  1 loop  /snap/snapd/14549
    loop5                       7:5    0 61.9M  1 loop  /snap/core20/1328
    loop6                       7:6    0 67.2M  1 loop  /snap/lxd/21835
    sda                         8:0    0   64G  0 disk
    ├─sda1                      8:1    0    1M  0 part
    ├─sda2                      8:2    0    1G  0 part  /boot
    └─sda3                      8:3    0   63G  0 part
      └─ubuntu--vg-ubuntu--lv 253:0    0 31.5G  0 lvm   /
    sdb                         8:16   0  2.5G  0 disk
    ├─sdb1                      8:17   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    └─sdb2                      8:18   0  511M  0 part
      └─md1                     9:1    0 1018M  0 raid0
        └─md_vg-r0_lv         253:1    0  100M  0 lvm   /tmp/new
    sdc                         8:32   0  2.5G  0 disk
    ├─sdc1                      8:33   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    └─sdc2                      8:34   0  511M  0 part
      └─md1                     9:1    0 1018M  0 raid0
        └─md_vg-r0_lv         253:1    0  100M  0 lvm   /tmp/new

## Задание 15

    root@vagrant:~# gzip -t /tmp/new/test.gz; echo $?
    0


## Задание 16

    root@vagrant:~# pvmove /dev/md1
      /dev/md1: Moved: 20.00%
      /dev/md1: Moved: 100.00%

    root@vagrant:~# lsblk
    NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
    loop0                       7:0    0 70.3M  1 loop  /snap/lxd/21029
    loop1                       7:1    0 32.3M  1 loop  /snap/snapd/12704
    loop2                       7:2    0 55.4M  1 loop  /snap/core18/2128
    loop3                       7:3    0 55.5M  1 loop  /snap/core18/2284
    loop4                       7:4    0 43.4M  1 loop  /snap/snapd/14549
    loop5                       7:5    0 61.9M  1 loop  /snap/core20/1328
    loop6                       7:6    0 67.2M  1 loop  /snap/lxd/21835
    sda                         8:0    0   64G  0 disk
    ├─sda1                      8:1    0    1M  0 part
    ├─sda2                      8:2    0    1G  0 part  /boot
    └─sda3                      8:3    0   63G  0 part
      └─ubuntu--vg-ubuntu--lv 253:0    0 31.5G  0 lvm   /
    sdb                         8:16   0  2.5G  0 disk
    ├─sdb1                      8:17   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    │   └─md_vg-r0_lv         253:1    0  100M  0 lvm   /tmp/new
    └─sdb2                      8:18   0  511M  0 part
      └─md1                     9:1    0 1018M  0 raid0
    sdc                         8:32   0  2.5G  0 disk
    ├─sdc1                      8:33   0    2G  0 part
    │ └─md0                     9:0    0    2G  0 raid1
    │   └─md_vg-r0_lv         253:1    0  100M  0 lvm   /tmp/new
    └─sdc2                      8:34   0  511M  0 part
      └─md1                     9:1    0 1018M  0 raid0


## Задание 17

    root@vagrant:~# gzip -t /tmp/new/test.gz; echo $?
    0
    root@vagrant:~# mdadm --fail /dev/md0 /dev/sdb1
    mdadm: set /dev/sdb1 faulty in /dev/md0

    root@vagrant:~# cat /proc/mdstat
    Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10]
    md1 : active raid0 sdc2[1] sdb2[0]
          1042432 blocks super 1.2 512k chunks
    
    md0 : active raid1 sdc1[1] sdb1[0](F)
          2094080 blocks super 1.2 [2/1] [_U]
    
    unused devices: <none>


## Задание 18

    root@vagrant:~# dmesg | grep md0
    [  921.900288] md/raid1:md0: not clean -- starting background reconstruction
    [  921.900291] md/raid1:md0: active with 2 out of 2 mirrors
    [  921.900322] md0: detected capacity change from 0 to 2144337920
    [  921.902355] md: resync of RAID array md0
    [  932.321853] md: md0: resync done.
    [ 1563.781033] md/raid1:md0: Disk failure on sdb1, disabling device.
                   md/raid1:md0: Operation continuing on 1 devices.

## Задание 19

    root@vagrant:~# gzip -t /tmp/new/test.gz; echo $?
    0

## Задание 20

    macbook0P0LYWK:sysadmin-05 kmankov$ vagrant destroy
        default: Are you sure you want to destroy the 'default' VM? [y/N] y
    ==> default: Forcing shutdown of VM...
    ==> default: Destroying VM and associated drives...

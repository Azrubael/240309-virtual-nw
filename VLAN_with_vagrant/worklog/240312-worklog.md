# 2024-03-12    10:03
=====================

План работы
1) Создать новую ветку 'DevOps7-traceroute2', выходящую от 'main'.
2) Отредактировать схему в соответствии с образцом.
3) Отедактировать скрипты в соответствии со схемой.
4) Сделать коммит.
5) Запустить тестирование: сначала скрипт пайтон, потом пинг, потом traceroute.

    $ vagrant up
    $ python3 scripts/pretty_config_collect_time.py
$ python3 scripts/pretty_config_collect_time.py
Data written to a file: reports/summary_table_024702792.txt

Created: 2024-03-12 14:37
Diagnostic information about the data of a virtual computer network running on the Virtualbox platform:

+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Device   | Hostname   | Operating System   | Default Gateway            | Interface   | IP Address       | MAC Adderess      |
+==========+============+====================+============================+=============+==================+===================+
| Server_1 | server1    | Ubuntu 18.04.6 LTS | via 192.168.1.1 dev enp0s8 | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | enp0s3      | 10.0.2.15/24     | 02:3b:7b:b7:3b:2d |
|          |            |                    |                            | enp0s8      | 192.168.1.105/24 | 08:00:27:5d:d3:ee |
|          |            |                    |                            | enp0s9      | 10.0.1.2/24      | 08:00:27:94:90:f4 |
|          |            |                    |                            | enp0s10     | 10.0.3.2/24      | 08:00:27:7f:c2:2f |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Client_1 | client1    | CentOS Linux 8     | via 10.0.2.2 dev eth0      | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | eth0        | 10.0.2.15/24     | 08:00:27:b7:f6:78 |
|          |            |                    |                            | eth1        | 10.0.1.10/24     | 08:00:27:36:a0:2d |
|          |            |                    |                            | eth2        | 10.0.5.10/24     | 08:00:27:e9:fd:75 |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Client_2 | client2    | Ubuntu 20.04.3 LTS | via 10.0.3.1 dev enp0s8    | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | enp0s3      | 10.0.2.15/24     | 08:00:27:62:67:d4 |
|          |            |                    |                            | enp0s8      | 10.0.3.10/24     | 08:00:27:d4:78:22 |
|          |            |                    |                            | enp0s9      | 10.0.5.11/24     | 08:00:27:3e:77:d5 |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+

    $ vagrant ssh Server_1
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 4.15.0-212-generic x86_64)
  System information as of Tue Mar 12 11:42:17 UTC 2024

  System load:  0.01              Users logged in:        0
  Usage of /:   3.4% of 38.70GB   IP address for enp0s3:  10.0.2.15
  Memory usage: 24%               IP address for enp0s8:  192.168.1.105
  Swap usage:   0%                IP address for enp0s9:  10.0.1.2
  Processes:    88                IP address for enp0s10: 10.0.3.2

Last login: Tue Mar 12 11:41:20 2024 from 10.0.2.2
vagrant@server1:~$ ping 10.0.1.10
PING 10.0.1.10 (10.0.1.10) 56(84) bytes of data.
64 bytes from 10.0.1.10: icmp_seq=1 ttl=64 time=1.81 ms
64 bytes from 10.0.1.10: icmp_seq=2 ttl=64 time=1.22 ms
^C
--- 10.0.1.10 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 1.221/1.519/1.817/0.298 ms
vagrant@server1:~$ ping 10.0.3.10
PING 10.0.3.10 (10.0.3.10) 56(84) bytes of data.
64 bytes from 10.0.3.10: icmp_seq=1 ttl=64 time=1.57 ms
64 bytes from 10.0.3.10: icmp_seq=2 ttl=64 time=0.997 ms
^C
--- 10.0.3.10 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 0.997/1.287/1.578/0.292 ms
vagrant@server1:~$ ping google.com
PING google.com (142.251.208.142) 56(84) bytes of data.
64 bytes from bud02s42-in-f14.1e100.net (142.251.208.142): icmp_seq=1 ttl=117 time=76.5 ms
64 bytes from bud02s42-in-f14.1e100.net (142.251.208.142): icmp_seq=2 ttl=117 time=24.5 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 24.552/50.532/76.513/25.981 ms

vagrant@server1:~$ traceroute 10.0.1.10
traceroute to 10.0.1.10 (10.0.1.10), 30 hops max, 60 byte packets
 1  client1 (10.0.1.10)  0.792 ms !X  0.809 ms !X  0.762 ms !X
vagrant@server1:~$ traceroute 10.0.3.10
traceroute to 10.0.3.10 (10.0.3.10), 30 hops max, 60 byte packets
 1  client2 (10.0.3.10)  0.873 ms  0.682 ms  0.832 ms

 vagrant@server1:~$ logout


 $ vagrant ssh Client_1
[vagrant@client1 ~]$ traceroute 10.0.5.11
traceroute to 10.0.5.11 (10.0.5.11), 30 hops max, 60 byte packets
 1  client2 (10.0.5.11)  4.047 ms  4.044 ms  3.758 ms
[vagrant@client1 ~]$ traceroute 10.0.1.2
traceroute to 10.0.1.2 (10.0.1.2), 30 hops max, 60 byte packets
 1  server1 (10.0.1.2)  3.906 ms  3.879 ms  3.522 ms
[vagrant@client1 ~]$ ip route
default via 10.0.2.2 dev eth0 proto dhcp metric 100 
10.0.1.0/24 dev eth1 proto kernel scope link src 10.0.1.10 metric 101 
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15 metric 100 
10.0.5.0/24 dev eth2 proto kernel scope link src 10.0.5.10 metric 102 
[vagrant@client1 ~]$ logout


$ vagrant ssh Client_2
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-42-generic x86_64)
Last login: Tue Mar 12 11:41:35 2024 from 10.0.2.2

vagrant@client2:~$ sudo -i
root@client2:~# ip route
default via 10.0.3.1 dev enp0s8 proto static 
default via 10.0.2.2 dev enp0s3 proto dhcp src 10.0.2.15 metric 100 
10.0.2.0/24 dev enp0s3 proto kernel scope link src 10.0.2.15 
10.0.2.2 dev enp0s3 proto dhcp scope link src 10.0.2.15 metric 100 
10.0.3.0/24 dev enp0s8 proto kernel scope link src 10.0.3.10 
10.0.5.0/24 dev enp0s9 proto kernel scope link src 10.0.5.11 

root@client2:~# traceroute 10.0.5.10
traceroute to 10.0.5.10 (10.0.5.10), 30 hops max, 60 byte packets
 1  client1 (10.0.5.10)  0.817 ms !X  0.735 ms !X  0.889 ms !X
root@client2:~# traceroute 10.0.3.2
traceroute to 10.0.3.2 (10.0.3.2), 30 hops max, 60 byte packets
 1  server1 (10.0.3.2)  0.812 ms  0.726 ms  0.687 ms


[root@client1 ~]# traceroute 10.0.1.2
traceroute to 10.0.1.2 (10.0.1.2), 30 hops max, 60 byte packets
 1  server1 (10.0.1.2)  3.895 ms  3.843 ms  3.417 ms
[root@client1 ~]# traceroute 10.0.5.11
traceroute to 10.0.5.11 (10.0.5.11), 30 hops max, 60 byte packets
 1  client2 (10.0.5.11)  4.399 ms  4.279 ms  3.938 ms
[root@client1 ~]# traceroute 10.0.3.2
traceroute to 10.0.3.2 (10.0.3.2), 30 hops max, 60 byte packets
 1  _gateway (10.0.2.2)  3.969 ms  3.653 ms  3.328 ms
 2  _gateway (192.168.1.1)  3.180 ms  2.722 ms  2.633 ms
...
[root@client1 ~]# traceroute 192.168.1.1
traceroute to 192.168.1.1 (192.168.1.1), 30 hops max, 60 byte packets
 1  _gateway (10.0.2.2)  3.386 ms  3.274 ms  2.857 ms
 2  _gateway (192.168.1.1)  30.153 ms  29.825 ms  29.937 ms
[root@client1 ~]# 


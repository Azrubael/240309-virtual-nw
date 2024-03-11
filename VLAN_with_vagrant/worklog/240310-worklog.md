# 2024-03-10  18:25
===================

    $ vagrant up
    $ source azenv/bin/activate
    $ python3 scripts/pretty_config_collect.py

Diagnostic information about the data of a virtual computer network running on the Virtualbox platform:

+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Device   | Hostname   | Operating System   | Default Gateway            | Interface   | IP Address       | MAC Adderess      |
+==========+============+====================+============================+=============+==================+===================+
| Server_1 | server1    | Ubuntu 18.04.6 LTS | via 192.168.1.1 dev enp0s3 | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | enp0s3      | 192.168.1.105/24 | 02:3b:7b:b7:3b:2d |
|          |            |                    |                            | enp0s8      | 192.168.1.105/24 | 08:00:27:23:6f:03 |
|          |            |                    |                            | enp0s9      | 10.0.1.11/24     | 08:00:27:35:55:41 |
|          |            |                    |                            | enp0s10     | 10.0.3.11/24     | 08:00:27:d0:1f:fb |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Client_1 | client1    | CentOS Linux 8     | via 10.0.2.2 dev eth0      | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | eth0        | 10.0.2.15/24     | 08:00:27:b7:f6:78 |
|          |            |                    |                            | eth1        | 10.0.1.12/24     | 08:00:27:1a:ec:b1 |
|          |            |                    |                            | eth2        | 10.0.5.2/24      | 08:00:27:24:fe:d1 |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Client_2 | client2    | Ubuntu 20.04.3 LTS | via 10.0.2.2 dev enp0s3    | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | enp0s3      | 10.0.2.15/24     | 08:00:27:62:67:d4 |
|          |            |                    |                            | enp0s8      | 10.0.3.13/24     | 08:00:27:7b:b5:74 |
|          |            |                    |                            | enp0s9      | 10.0.5.3/24      | 08:00:27:e4:09:e1 |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
Data written to a file: reports/virtual_machines_009216351.json
Data written to a file: reports/virtual_network_009216351.json
Data written to a file: reports/summary_table_009216351.txt

vagrant ssh Server_1 -c "traceroute 10.0.1.12"
vagrant ssh Server_1 -c "traceroute 10.0.3.13"
vagrant ssh Client_1 -c "traceroute 10.0.1.11"
vagrant ssh Client_1 -c "traceroute 10.0.5.3"
vagrant ssh Client_2 -c "traceroute 10.0.3.11"
vagrant ssh Client_2 -c "traceroute 10.0.5.2"


    $ vagrant ssh Server_1 -c "traceroute 10.0.1.12"
traceroute to 10.0.1.12 (10.0.1.12), 30 hops max, 60 byte packets
# 1  client1 (10.0.1.12)  1.157 ms !X  0.742 ms !X  0.568 ms !X

    $ vagrant ssh Server_1 -c "traceroute 10.0.3.13"
traceroute to 10.0.3.13 (10.0.3.13), 30 hops max, 60 byte packets
 1  client2 (10.0.3.13)  0.777 ms  0.226 ms  0.218 ms

    $ varant ssh Client_1 -c "traceroute 10.0.1.11"
traceroute to 10.0.1.11 (10.0.1.11), 30 hops max, 60 byte packets
 1  server1 (10.0.1.11)  1.507 ms  1.424 ms  1.377 ms

    $ vagrant ssh Client_1 -c "traceroute 10.0.5.3"
traceroute to 10.0.5.3 (10.0.5.3), 30 hops max, 60 byte packets
 1  client2 (10.0.5.3)  1.479 ms  1.572 ms  1.551 ms

    $ vagrant ssh Client_2 -c "traceroute 10.0.3.11"
traceroute to 10.0.3.11 (10.0.3.11), 30 hops max, 60 byte packets
 1  server1 (10.0.3.11)  0.415 ms  0.373 ms  0.452 ms

    $ vagrant ssh Client_2 -c "traceroute 10.0.5.2"
traceroute to 10.0.5.2 (10.0.5.2), 30 hops max, 60 byte packets
 1  client1 (10.0.5.2)  0.481 ms !X  0.567 ms !X  0.488 ms !X

    $ vagrant ssh Server_1

vagrant@server1:~$ route -n
Kernel IP routing table
Destination     Gateway        Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1    0.0.0.0         UG    0      0        0 enp0s3
0.0.0.0         10.0.2.2       0.0.0.0         UG    100    0        0 enp0s3
10.0.1.0        0.0.0.0        255.255.255.0   U     0      0        0 enp0s9
10.0.2.0        0.0.0.0        255.255.255.0   U     0      0        0 enp0s3
10.0.2.2        0.0.0.0        255.255.255.255 UH    100    0        0 enp0s3
10.0.3.0        0.0.0.0        255.255.255.0   U     0      0        0 enp0s10
192.168.1.0     0.0.0.0        255.255.255.0   U     0      0        0 enp0s8
192.168.1.0     0.0.0.0        255.255.255.0   U     0      0        0 enp0s3





# 2024-03-10    20:56
=====================

Diagnostic information about the data of a virtual computer network running on the Virtualbox platform:

+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Device   | Hostname   | Operating System   | Default Gateway            | Interface   | IP Address       | MAC Adderess      |
+==========+============+====================+============================+=============+==================+===================+
| Server_1 | server1    | Ubuntu 18.04.6 LTS | via 192.168.1.1 dev enp0s3 | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | enp0s3      | 192.168.1.105/24 | 02:3b:7b:b7:3b:2d |
|          |            |                    |                            | enp0s8      | 192.168.1.105/24 | 08:00:27:cc:18:c8 |
|          |            |                    |                            | enp0s9      | 10.0.1.11/24     | 08:00:27:60:ef:89 |
|          |            |                    |                            | enp0s10     | 10.0.3.11/24     | 08:00:27:66:aa:0a |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Client_1 | client1    | CentOS Linux 8     | via 10.0.2.2 dev eth0      | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | eth0        | 10.0.2.15/24     | 08:00:27:b7:f6:78 |
|          |            |                    |                            | eth1        | 10.0.1.12/24     | 08:00:27:1f:6f:06 |
|          |            |                    |                            | eth2        | 10.0.5.2/24      | 08:00:27:39:23:3c |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Client_2 | client2    | Ubuntu 20.04.3 LTS | via 10.0.2.2 dev enp0s3    | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | enp0s3      | 10.0.2.15/24     | 08:00:27:62:67:d4 |
|          |            |                    |                            | enp0s8      | 10.0.3.13/24     | 08:00:27:c9:51:61 |
|          |            |                    |                            | enp0s9      | 10.0.5.3/24      | 08:00:27:c3:d1:89 |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
Data written to a file: reports/virtual_machines_009686387.json
Data written to a file: reports/virtual_network_009686387.json
Data written to a file: reports/summary_table_009686387.txt

    $ vagrant ssh Server_1 -c "traceroute 10.0.1.12"
traceroute to 10.0.1.12 (10.0.1.12), 30 hops max, 60 byte packets
# 1  client1 (10.0.1.12)  0.979 ms !X  0.728 ms !X  0.831 ms !X

    $ vagrant ssh Server_1 -c "traceroute 10.0.3.13"
traceroute to 10.0.3.13 (10.0.3.13), 30 hops max, 60 byte packets
 1  client2 (10.0.3.13)  0.873 ms  0.975 ms  0.992 ms

    $ vagrant ssh Client_1 -c "traceroute 10.0.1.11"
traceroute to 10.0.1.11 (10.0.1.11), 30 hops max, 60 byte packets
 1  server1 (10.0.1.11)  1.093 ms  1.009 ms  0.867 ms

    $ vagrant ssh Client_1 -c "traceroute 10.0.5.3"
traceroute to 10.0.5.3 (10.0.5.3), 30 hops max, 60 byte packets
 1  client2 (10.0.5.3)  1.651 ms  1.756 ms  1.419 ms

    $ vagrant ssh Client_2 -c "traceroute 10.0.3.11"
traceroute to 10.0.3.11 (10.0.3.11), 30 hops max, 60 byte packets
 1  server1 (10.0.3.11)  0.499 ms  0.454 ms  0.431 ms

    $ vagrant ssh Client_2 -c "traceroute 10.0.5.2"
traceroute to 10.0.5.2 (10.0.5.2), 30 hops max, 60 byte packets
# 1  client1 (10.0.5.2)  0.463 ms !X  0.540 ms !X  0.524 ms !X
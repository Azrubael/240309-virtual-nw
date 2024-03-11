# 2024-03-10    17:38
=====================


# Deploying a project from IaC:
#   1. Configure static addresses on all interfaces on Server_1.
#   2. Configure the DHCP service on Server_1, which will configure the Int1
# addresses of Client_1 and Client_2
#   3.a On the virtual interface lo Client_1:
#       - assign two IP addresses IPaddr1 and IPaddr2.
#   3.b Configure routing so that traffic from Client_2 to IPaddr1 goes
# through Server_1, and to IPaddr2 through Net4. To check, use traceroute.



    $ vagrant up

    $ source azenv/bin/activate
(azenv)$ pip freeze > python_dependencies
    $ cat python_dependencies
tabulate==0.9.0

    $ python3 scripts/pretty_config_collect.py

Diagnostic information about the data of a virtual computer network running on the Virtualbox platform:

+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Device   | Hostname   | Operating System   | Default Gateway            | Interface   | IP Address       | MAC Adderess      |
+==========+============+====================+============================+=============+==================+===================+
| Server_1 | server1    | Ubuntu 18.04.6 LTS | via 192.168.1.1 dev enp0s3 | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | enp0s3      | 192.168.1.204/24 | 02:3b:7b:b7:3b:2d |
|          |            |                    |                            | enp0s8      | 192.168.1.204/24 | 08:00:27:8d:ec:94 |
|          |            |                    |                            | enp0s9      | 10.8.0.11/24     | 08:00:27:07:21:d3 |
|          |            |                    |                            | enp0s10     | 10.9.0.11/24     | 08:00:27:ca:90:e8 |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Client_1 | client1    | CentOS Linux 8     | via 10.0.2.2 dev eth0      | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | eth0        | 10.0.2.15/24     | 08:00:27:b7:f6:78 |
|          |            |                    |                            | eth1        | 10.8.0.12/24     | 08:00:27:69:06:44 |
|          |            |                    |                            | eth2        | 10.7.0.12/24     | 08:00:27:22:71:35 |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Client_2 | client2    | Ubuntu 20.04.3 LTS | via 10.0.2.2 dev enp0s3    | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | enp0s3      | 10.0.2.15/24     | 08:00:27:62:67:d4 |
|          |            |                    |                            | enp0s8      | 10.9.0.13/24     | 08:00:27:0f:2a:63 |
|          |            |                    |                            | enp0s9      | 10.7.0.13/24     | 08:00:27:ea:b0:a2 |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
Data written to a file: reports/virtual_machines_008491433.json
Data written to a file: reports/virtual_network_008491433.json
Data written to a file: reports/summary_table_008491433.txt



# 4. Configure the SSH service so that Client_1 and Client_2
# can connect to Server_1 and each other.

    $ vagrant ssh Client_1 -c "traceroute 10.8.0.11"
traceroute to 10.8.0.11 (10.8.0.11), 30 hops max, 60 byte packets
 1  server1 (10.8.0.11)  1.505 ms  1.508 ms  1.483 ms
    $ vagrant ssh Client_1 -c "traceroute 10.7.0.13"
traceroute to 10.7.0.13 (10.7.0.13), 30 hops max, 60 byte packets
 1  10.7.0.13 (10.7.0.13)  1.555 ms  1.448 ms  1.769 ms

    $ vagrant ssh Client_2 -c "traceroute 10.9.0.11"
traceroute to 10.9.0.11 (10.9.0.11), 30 hops max, 60 byte packets
 1  server1 (10.9.0.11)  0.823 ms  0.770 ms  0.754 ms
    $ vagrant ssh Client_2 -c "traceroute 10.7.0.12"
traceroute to 10.7.0.12 (10.7.0.12), 30 hops max, 60 byte packets
 1  10.7.0.12 (10.7.0.12)  0.468 ms !X  0.416 ms !X  0.396 ms !X
# !X stands for "communication administratively prohibited," which means that a packet was received with the "communication administratively prohibited" error.
    $ vagrant ssh Client_2 -c "ping 10.7.0.12"
PING 10.7.0.12 (10.7.0.12) 56(84) bytes of data.
64 bytes from 10.7.0.12: icmp_seq=1 ttl=64 time=0.498 ms
64 bytes from 10.7.0.12: icmp_seq=2 ttl=64 time=0.511 ms
64 bytes from 10.7.0.12: icmp_seq=3 ttl=64 time=0.502 ms
^C
--- 10.7.0.12 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2035ms
rtt min/avg/max/mdev = 0.498/0.503/0.511/0.005 ms


    $ vagrant halt
    $ vagrant destroy
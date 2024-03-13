# 2024-03-13    09:47
=====================

Tables overview
---------------
The *filter table* is used to make decisions about whether to let a packet continue to its intended destination or to deny its request.
The *NAT table* is used to implement network address translation rules. As packets enter the network stack, rules in this table will determine whether and how to modify the packet’s source or destination addresses in order to impact the way that the packet and any response traffic are routed.
The *mangle table* is used to alter the IP headers of the packet in various ways. For instance, you can adjust the TTL (Time to Live) value of a packet, either lengthening or shortening the number of valid network hops the packet can sustain.
The *raw table* has a very narrowly defined function. Its only purpose is to provide a mechanism for marking packets in order to opt-out of connection tracking. The iptables firewall is stateful, meaning that packets are evaluated in regards to their relation to previous packets.


Today's task:
-------------
Configure the firewall on Server_1 as follows:
    1) Allowed to connect via SSH from `Client_1` and forbidden from `Client_2`
    2) `Client_2` may ping IPaddr1, but may not ping IPaddr2

1) Allow to connect `Server_1` via SSH from `Client_1` and forbidden from `Client_2`

    $ vagrant up
    $ python3 scripts/pretty_config_collect_time.py
Data written to a file: reports/virtual_machines_031756483.json
Data written to a file: reports/virtual_network_031756483.json
Data written to a file: reports/summary_table_031756483.txt

Created: 2024-03-13 10:12
Diagnostic information about the data of a virtual computer network running on the Virtualbox platform:

+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Device   | Hostname   | Operating System   | Default Gateway            | Interface   | IP Address       | MAC Adderess      |
+==========+============+====================+============================+=============+==================+===================+
| Server_1 | server1    | Ubuntu 18.04.6 LTS | via 192.168.1.1 dev enp0s8 | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | enp0s3      | 10.0.2.15/24     | 02:3b:7b:b7:3b:2d |
|          |            |                    |                            | enp0s8      | 192.168.1.105/24 | 08:00:27:bf:f1:7b |
|          |            |                    |                            | enp0s9      | 10.0.1.2/24      | 08:00:27:18:f1:69 |
|          |            |                    |                            | enp0s10     | 10.0.3.2/24      | 08:00:27:07:90:db |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Client_1 | client1    | CentOS Linux 8     | via 10.0.2.2 dev eth0      | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | eth0        | 10.0.2.15/24     | 08:00:27:b7:f6:78 |
|          |            |                    |                            | eth1        | 10.0.1.10/24     | 08:00:27:0c:4f:20 |
|          |            |                    |                            | eth2        | 10.0.5.10/24     | 08:00:27:44:55:be |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+
| Client_2 | client2    | Ubuntu 20.04.3 LTS | via 10.0.2.2 dev enp0s3    | lo          | 127.0.0.1/8      | 00:00:00:00:00:00 |
|          |            |                    |                            | enp0s3      | 10.0.2.15/24     | 08:00:27:62:67:d4 |
|          |            |                    |                            | enp0s8      | 10.0.3.10/24     | 08:00:27:96:d9:c5 |
|          |            |                    |                            | enp0s9      | 10.0.5.11/24     | 08:00:27:20:d5:e3 |
+----------+------------+--------------------+----------------------------+-------------+------------------+-------------------+

# Login to Server_1
    $ vagrant ssh Server_1
    $ sudo iptables -L
...

    $ sudo iptables -t filter -L
...

vagrant@server1:~$ ping client1
PING client1 (10.0.1.10) 56(84) bytes of data.
64 bytes from client1 (10.0.1.10): icmp_seq=1 ttl=64 time=2.20 ms
64 bytes from client1 (10.0.1.10): icmp_seq=2 ttl=64 time=1.22 ms
^C
--- client1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 1.228/1.714/2.200/0.486 ms

vagrant@server1:~$ ping client2
PING client2 (10.0.3.10) 56(84) bytes of data.
64 bytes from client2 (10.0.3.10): icmp_seq=1 ttl=64 time=1.49 ms
64 bytes from client2 (10.0.3.10): icmp_seq=2 ttl=64 time=1.05 ms
^C
--- client2 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 1.054/1.275/1.496/0.221 ms


# Check out all ports are used on hosts for SSH
    $ sudo lsof -i -P -n | grep LISTEN | grep ssh
sshd       821            root    3u  IPv4  17286      0t0  TCP *:22 (LISTEN)
sshd       821            root    4u  IPv6  17306      0t0  TCP *:22 (LISTEN)
    $ sudo vim /etc/ssh/sshd_config
    $ nmap -p 1-3000 -sV -sS -T4 10.0.1.0-10.0.5.50

# https://www.opennet.ru/docs/RUS/iptables/
# Blocking traffic
    $ sudo iptables -A INPUT -p tcp --dport 22 -s 10.0.3.10 -j DROP 
    $ sudo iptables -A INPUT -p tcp --dport 2222 -s 10.0.3.10 -j DROP 
    $ sudo iptables -A INPUT -p tcp --dport 2022 -s 10.0.3.10 -j DROP 
    $ sudo iptables -A INPUT -p tcp --dport 22 -s 10.0.1.10 -j ACCEPT 
    $ sudo iptables -A INPUT -p tcp --dport 2222 -s 10.0.1.10 -j ACCEPT 
    $ sudo iptables -A INPUT -p tcp --dport 2022 -s 10.0.1.10 -j ACCEPT
# OR
vagrant@server1:~$ sudo iptables -A INPUT -p tcp -s 10.0.3.10 -m multiport --dports 22,2222,2022 -j DROP
vagrant@server1:~$ sudo iptables -A INPUT -p tcp -s 10.0.1.10 -m multiport --dports 22,2222,2022 -j ACCEPT


vagrant@server1:~$ sudo iptables -t filter -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     tcp  --  client1              anywhere             multiport dports ssh,2222,2022
DROP       tcp  --  client2              anywhere             multiport dports ssh,2222,2022

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination   



#    2) `Client_2` may ping IPaddr1, but may not ping IPaddr2
    $ vagrant ssh Client_1
Last login: Wed Mar 13 08:12:37 2024 from 10.0.2.2
[vagrant@client1 ~]$ sudo iptables -A INPUT -s 10.0.5.11 -p icmp --icmp-type echo-request -j DROP
[vagrant@client1 ~]$ sudo iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
DROP       icmp --  client2              anywhere             icmp echo-request

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination 


# To block all incoming traffic on the localhost
    $ sudo iptables -A INPUT -j DROP


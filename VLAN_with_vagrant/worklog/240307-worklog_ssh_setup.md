# 2024-03-06    17:56
=====================

    $ vagrant up
    $ vagrant ssh Server_1

vagrant@server1:~$ ip route sh
default via 10.0.2.2 dev enp0s3 proto dhcp src 10.0.2.15 metric 100 
10.0.2.0/24 dev enp0s3 proto kernel scope link src 10.0.2.15 
10.0.2.2 dev enp0s3 proto dhcp scope link src 10.0.2.15 metric 100 
10.8.0.0/24 dev enp0s9 proto kernel scope link src 10.8.0.11 
10.9.0.0/24 dev enp0s10 proto kernel scope link src 10.9.0.11 
192.168.1.0/24 dev enp0s8 proto kernel scope link src 192.168.1.204 

vagrant@server1:~$ traceroute client1
traceroute to client1 (10.8.0.12), 30 hops max, 60 byte packets
 1  client1 (10.8.0.12)  1.357 ms  1.070 ms  1.029 ms

vagrant@server1:~$ traceroute client2
traceroute to client2 (10.9.0.13), 30 hops max, 60 byte packets
 1  client2 (10.9.0.13)  1.547 ms  1.355 ms  1.841 ms


vagrant@server1:~$ ssh-keygen -t rsa -b 4096 -f ~/.ssh/c1_key -N ""
vagrant@server1:~$ ssh-keygen -t rsa -b 4096 -f ~/.ssh/c2_key -N ""

# sudo systemctl restart sshd - to restart SSH after changing '/etc/ssh/sshd_config' on Centos
vagrant@server1:~$ ssh-copy-id -i ~/.ssh/c1_key.pub vagrant@client1
vagrant@server1:~$ ssh -i ~/.ssh/c1_key vagrant@client1
[vagrant@client1 ~]$ traceroute 10.8.0.11
traceroute to 10.8.0.11 (10.8.0.11), 30 hops max, 60 byte packets
 1  server1 (10.8.0.11)  0.692 ms  0.596 ms  0.532 ms
[vagrant@client1 ~]$ exit
logout
Connection to client1 closed.


# sudo systemctl restart ssh - to restart SSH after changing '/etc/ssh/sshd_config' on Ubuntu
vagrant@server1:~$ ssh-copy-id -i ~/.ssh/c2_key.pub vagrant@client2
vagrant@server1:~$ ssh -i ~/.ssh/c2_key vagrant@client2
vagrant@client2:~$ ping client1
PING client1 (10.10.0.12) 56(84) bytes of data.
64 bytes from client1 (10.10.0.12): icmp_seq=1 ttl=64 time=0.456 ms
64 bytes from client1 (10.10.0.12): icmp_seq=2 ttl=64 time=0.394 ms
^C
--- client1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.394/0.425/0.456/0.031 ms
vagrant@client2:~$ exit
logout
Connection to client2 closed.
vagrant@server1:~$ ^D


    $ vagrant ssh Server_1 -c "ip -j addr"
    $ vagrant halt

#!/bin/bash

sudo yum makecache
sudo yum install vim bind-utils -y
sudo yum install traceroute -y
sudo yum install mc -y
sudo yum install net-tools -y
sudo dnf install network-scripts -y

sudo cp /tmp/route-eth2 /etc/sysconfig/network-scripts/route-eth2
sudo cp /tmp/route-eth1 /etc/sysconfig/network-scripts/route-eth1


if [[ -z "$(grep '^export EDITOR=vim' /home/vagrant/.bashrc)" ]]; then
    echo "export EDITOR=vim" >> /home/vagrant/.bashrc
    echo "vim set as the default text editor."
else echo "Note: vim is already the default text editor."
fi

if [[ -z "$(grep '10.0.1.2  server1' /etc/hosts)" ]] && \
   [[ -z "$(grep '10.0.5.11  client2' /etc/hosts)" ]]; then
sudo echo "## vagrant-hostmanager-start
10.0.1.2  server1
10.0.5.11  client2
## vagrant-hostmanager-end" >> /etc/hosts
fi


# if [[ -z "$(grep '^GATEWAY=10.0.1.2' /etc/sysconfig/network-scripts/ifcfg-eth1)" ]]; then
#     echo "GATEWAY=10.0.1.2" >> /etc/sysconfig/network-scripts/ifcfg-eth1
#     echo "For Client_1 CentOS 8 the default gateway set as 10.0.1.2 via eth1."
# else echo "Note: For Client_1 CentOS 8 the default gateway is OK."
# fi


nmcli con mod "System eth1" ipv4.routes "10.0.1.0/24 10.0.1.10"
# nmcli con mod "System eth1" ipv4.addresses 10.0.1.0/24 ipv4.gateway 10.0.1.2
# sudo ifconfig eth0 down
sudo systemctl restart network
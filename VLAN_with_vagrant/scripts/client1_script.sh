#!/bin/bash

sudo yum makecache
sudo yum install vim bind-utils -y
sudo yum install traceroute -y
sudo yum install mc -y
sudo yum install net-tools -y

sudo cp /tmp/route-eth1 /etc/sysconfig/network-scripts/route-eth1


if [[ -z "$(grep '^export EDITOR=vim' /home/vagrant/.bashrc)" ]]; then
    echo "export EDITOR=vim" >> /home/vagrant/.bashrc
    echo "vim set as the default text editor."
else
    echo "Note: vim is already the default text editor."
fi


if [[ -z "$(grep '10.0.1.11  server1' /etc/hosts)" ]] && \
   [[ -z "$(grep '10.0.5.3  client2' /etc/hosts)" ]]; then
sudo echo "## vagrant-hostmanager-start
10.0.1.11  server1
10.0.5.3  client2
## vagrant-hostmanager-end" >> /etc/hosts
fi
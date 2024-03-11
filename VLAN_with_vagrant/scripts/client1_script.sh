#!/bin/bash

sudo yum update
sudo yum install vim bind-utils -y
sudo yum install traceroute -y
sudo yum install mc -y
sudo yum install net-tools -y


if [[ -z "$(grep '^export EDITOR=vim' /home/vagrant/.bashrc)" ]]; then
    echo "export EDITOR=vim" >> /home/vagrant/.bashrc
    echo "vim set as the default text editor."
else
    echo "Note: vim is already the default text editor."
fi

if [[ -z "$(grep '10.8.0.11  server1' /etc/hosts)" ]] && \
   [[ -z "$(grep '10.10.0.13  client2' /etc/hosts)" ]]; then
sudo echo "## vagrant-hostmanager-start
10.8.0.11  server1
10.10.0.13  client2
## vagrant-hostmanager-end" >> /etc/hosts
fi
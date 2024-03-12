#!/bin/bash

sudo apt update
sudo apt install dnsutils -y
sudo apt install net-tools -y
sudo apt install traceroute -y
sudo apt install mc -y

# sudo ip route add default via 10.0.3.2 dev enp0s8

sudo rm /etc/netplan/50-vagrant.yaml
sudo cp /tmp/72-netplan-config.yaml /etc/netplan/72-netplan-config.yaml && sudo netplan apply


if [[ -z "$(grep '10.0.3.2  server1' /etc/hosts)" ]] && \
   [[ -z "$(grep '10.0.5.10  client1' /etc/hosts)" ]]; then
sudo echo "## vagrant-hostmanager-start
10.0.3.2  server1
10.0.5.10  client1
## vagrant-hostmanager-end" >> /etc/hosts
fi
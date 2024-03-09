#!/bin/bash

sudo apt update
sudo apt install dnsutils -y
sudo apt install traceroute -y
sudo apt install mc -y

if [[ -z "$(grep '10.9.0.11  server1' /etc/hosts)" ]] && \
   [[ -z "$(grep '10.10.0.12  client1' /etc/hosts)" ]]; then
sudo echo "## vagrant-hostmanager-start
10.9.0.11  server1
10.10.0.12  client1
## vagrant-hostmanager-end" >> /etc/hosts
fi
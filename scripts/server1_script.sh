#!/bin/bash

sudo apt makecache
sudo apt install dnsutils -y
sudo apt install traceroute -y
sudo apt install mc -y


# Install and configure DHCP server
sudo apt install -y isc-dhcp-server

cat <<DHCPD | sudo tee /etc/dhcp/dhcpd.conf
subnet 10.8.0.0 netmask 255.255.255.0 {
  range 10.8.0.2 10.8.0.100;
  option routers 10.8.0.1;
  option domain-name-servers 8.8.8.8, 8.8.4.4;
}
subnet 10.9.0.0 netmask 255.255.255.0 {
  range 10.9.0.2 10.9.0.100;
  option routers 10.9.0.1;
  option domain-name-servers 8.8.8.8, 8.8.4.4;
}
DHCPD

# Configure the DHCP server to listen on the private network interfaces
if [[ -z "$(grep '^INTERFACESv4="enp0s8 enp0s9"' /etc/default/isc-dhcp-server)" ]]; then
cat <<EOF | sudo tee -a /etc/default/isc-dhcp-server
INTERFACESv4="enp0s8 enp0s9"
EOF
else echo "Note: isc-dhcp-server already has INTERFACESv4 enp0s8 and enp0s9"
fi

sudo systemctl restart isc-dhcp-server

sudo rm /etc/netplan/50-vagrant.yaml
sudo cp /tmp/70-netplan-config.yaml /etc/netplan/70-netplan-config.yaml && sudo netplan apply

# Client's network aliases declaration
if [[ -z "$(grep '10.8.0.12  client1' /etc/hosts)" ]] && \
   [[ -z "$(grep '10.9.0.13  client2' /etc/hosts)" ]]; then
sudo echo "## vagrant-hostmanager-start
10.8.0.12  client1
10.9.0.13  client2
## vagrant-hostmanager-end" >> /etc/hosts
fi
# 2024-03-12    14:20
=====================

*Question1*
======================================================================
What is the difference of the two bash commands in CentOS:
mcli con mod eth1 ipv4.addresses 10.0.1.0/24 ipv4.gateway 10.0.1.2
nmcli con mod eth1 ipv4.routes “10.0.1.0/24 10.0.1.2”

*Answer1*
======================================================================
The two `nmcli` commands in CentOS you provided have different purposes:

1. `nmcli con mod eth1 ipv4.addresses 10.0.1.0/24 ipv4.gateway 10.0.1.2`
   - This command is used to modify the IPv4 addresses and gateway for the network connection named "eth1". It sets the IPv4 address to "10.0.1.0" with a subnet mask of "/24" and the gateway to "10.0.1.2".

2. `nmcli con mod "System eth1" ipv4.routes "10.0.1.0/24 10.0.1.10"`
   - This command is used to modify the IPv4 routing table for the network connection named "eth1". It adds a route for the network "10.0.1.0/24" via the gateway "10.0.1.2".

In summary:
- The first command (`ipv4.addresses` and `ipv4.gateway`) is used to set the IP address and gateway for the network connection.
- The second command (`ipv4.routes`) is used to add a specific route to the routing table for the network connection.

Both commands are used to manage different aspects of network configuration, with the first command focusing on the IP address and gateway settings, and the second command focusing on the routing table.



*Question2*
======================================================================
I have a Vagrantfile to deploy via VirtualBOX a network with a few subnets and three instances of Linux:
```bash
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "Server_1" do |s1|
    s1.vm.box = "ubuntu/bionic64"
    s1.vm.hostname = "server1"
    s1.vm.network "public_network", ip: "192.168.1.105", bridge: "wlp2s0"
    s1.vm.network "private_network", ip: "10.0.1.2", virtualbox__intnet: true
    s1.vm.network "private_network", ip: "10.0.3.2", virtualbox__intnet: true
    s1.vm.provider "virtualbox" do |vbs1|
      vbs1.memory = "600"
      vbs1.cpus = 1    
    end
    s1.vm.provision "file", source: "network_config/70-netplan-config.yaml", destination: "/tmp/70-netplan-config.yaml"
    s1.vm.synced_folder ".", "/vagrant", disabled: true
    s1.vm.provision "shell", path: "scripts/server1_script.sh"
  end

  config.vm.define "Client_1" do |c1|
    c1.vm.box = "generic/centos8"
    c1.vm.hostname = "client1"
    c1.vm.network "private_network", ip: "10.0.1.10", virtualbox__intnet: true
    c1.vm.network "private_network", ip: "10.0.5.10", virtualbox__intnet: true
    c1.vm.provider "virtualbox" do |vbc1|
      vbc1.memory = "800"
      vbc1.cpus = 1    
    end
    c1.vm.provision "file", source: "network_config/route-eth1", destination: "/tmp/route-eth1"
    c1.vm.provision "file", source: "network_config/route-eth2", destination: "/tmp/route-eth2"
    c1.vm.synced_folder ".", "/vagrant", disabled: true
    c1.vm.provision "shell", path: "scripts/client1_script.sh"
  end

  config.vm.define "Client_2" do |c2|
    c2.vm.box = "geerlingguy/ubuntu2004"
    c2.vm.hostname = "client2"
    c2.vm.network "private_network", ip: "10.0.3.10", virtualbox__intnet: true
    c2.vm.network "private_network", ip: "10.0.5.11", virtualbox__intnet: true
    c2.vm.provider "virtualbox" do |vbc2|
      vbc2.memory = "800"
      vbc2.cpus = 1    
    end
    c2.vm.provision "file", source: "network_config/72-netplan-config.yaml", destination: "/tmp/72-netplan-config.yaml"
    c2.vm.synced_folder ".", "/vagrant", disabled: true
    c2.vm.provision "shell", path: "scripts/client2_script.sh"
  end
end
```

Write the Bash commands for Server_1 iptables to allow connect via SSH from Client_1 and forbidden connect via SSH from Client_2.


*Answer2*
======================================================================
# Allow SSH connections from Client_1
iptables -A INPUT -p tcp --dport 22 -s 10.0.1.10 -j ACCEPT

# Forbid SSH connections from Client_2
iptables -A INPUT -p tcp --dport 22 -s 10.0.3.10 -j DROP
iptables -A INPUT -p tcp --dport 22 -s 10.0.5.11 -j DROP

# Save the iptables rules to persist across reboots
service iptables save



*Question3*
======================================================================
How can I check out all ports are used on hosts for SSH if it isn't 22?

*Answer3*
======================================================================
https://www.opennet.ru/docs/RUS/iptables/
To check which ports are being used for SSH on hosts if the default port 22 is not being used, you can try the following methods:

1. **Scan the network using nmap**: Nmap is a powerful network scanning tool that can help you identify open ports on hosts. You can use the following command to scan for SSH ports on a specific network:
   ```
   nmap -p 1-65535 -sV -sS -T4 <network_range>
   ```
   Replace `<network_range>` with the range of IP addresses you want to scan. This command will scan all ports from 1 to 65535 and provide information about the services running on those ports. Look for the SSH service to identify the port being used.

2. **Check the SSH configuration file**: On the host machine, you can check the SSH configuration file to determine the port being used. The configuration file is usually located at `/etc/ssh/sshd_config`. Open the file using a text editor and look for the line that specifies the port number. It should be something like:
   ```
   Port <port_number>
   ```
   The `<port_number>` will indicate the port being used for SSH.

3. **Use a port scanning tool**: There are various port scanning tools available that can help you identify open ports on hosts. One such tool is `lsof` (List Open Files). You can use the following command to check for open ports on a host:
   ```
   sudo lsof -i -P -n | grep LISTEN | grep ssh
   ```
   This command will list all open ports that are listening for SSH connections.

Please note that some of these methods may require administrative privileges or appropriate permissions to access the necessary files or tools.
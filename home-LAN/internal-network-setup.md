# 2024-04-07    12:15
=====================

*Question1*
===========================================================================
I have VirtualBOX and a virtual server Ubuntu18 server on it with a bridged network adapter and an internal network adapter. How can i assign a static ip 192.168.100.1  for the server Ubuntu18 in my internal network?

*Answer1*
To assign a static IP address (192.168.100.1) to your Ubuntu 18 server running on VirtualBox with an internal network adapter, you can follow these steps:

1. Identify the Network Interface Name:
  - Open a terminal on your Ubuntu 18 server.
  - Use the command `ip route show` a or `ifconfig` to identify the network interface name for the internal network adapter. It is usually named something like enp0s8 or eth1.

2. Edit the Netplan Configuration:
  - Netplan is used to configure network interfaces in Ubuntu 18. Navigate to the Netplan configuration directory using the command: cd /etc/netplan.
  - List the files in the directory using ls to identify the configuration file. It usually starts with a number like 01-netcfg.yaml.
  - Edit the configuration file using a text editor like nano or vi. For example: sudo nano 01-netcfg.yaml.

3. Add Static IP Configuration:
  - Inside the configuration file, locate the section for the internal network adapter (identified in step 1).
  - Add the following lines to assign the static IP address:
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      addresses:
        - 192.168.1.103/24
      gateway4: 192.168.1.1
      dhcp4: yes
      nameservers:
        addresses:
          - 8.8.8.8 
    enp0s8:
      addresses: [192.168.100.1/24]
      dhcp4: no
      
```

4. Apply the Changes:
  - Save the configuration file and exit the text editor.
  - Apply the changes by running: sudo netplan apply.

5. Verify the Configuration:
  - Check if the static IP address has been successfully assigned using the command: `ip route show` a or `ifconfig`.
  - You should see the internal network adapter configured with the static IP address you specified.


*Question2*
===========================================================================
I have VirtualBOX and a virtual server Ubuntu18 server on it with a bridged network adapter and an internal network adapter. I want to make access for any Windows 10 computer in my internal network through previously mentioned virtual server Ubuntu18. How can I do it permanently for Ubuntu18 server?

*Answer2*
To allow Windows 10 computers on your internal network to access services through your Ubuntu 18 virtual server running on VirtualBox, you can set up routing and forwarding on your Ubuntu server. Here's a general outline of the steps you can take to achieve this:

1. **Enable IP Forwarding on Ubuntu 18 Server**:
   - Open a terminal on your Ubuntu 18 virtual server.
   - Run the following command to enable IP forwarding:
     ```
     sudo sysctl -w net.ipv4.ip_forward=1
     ```

2. **Configure IP Tables**:
   - Use IP tables to set up NAT (Network Address Translation) on your Ubuntu server. This will allow your Ubuntu server to act as a gateway for the Windows 10 computers to access external networks.
   - Run the following commands to configure IP tables:
     ```
     sudo iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
     sudo iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
     sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
     ```

3. **Configure DNS on Ubuntu 18 Server**:
   - You can set up a DNS server on your Ubuntu server to resolve domain names for the Windows 10 computers. You can use a DNS server like Bind9 for this purpose.

4. **Set Up Services**:
   - Install and configure the services you want to access from your Windows 10 computers on your Ubuntu server. For example, if you want to access a web server, you can install Apache and configure it accordingly.

5. **Network Configuration**:
   - Ensure that the internal network adapter on your VirtualBox is properly configured to communicate with the Windows 10 computers.


# To switch “on” or “off” routing you must edit
    $ sudo vim /etc/sysctl.conf
# To check out routing enable use
    $ sudo sysctl net.ipv4.conf.all.forwarding
    
    
    
*Question3*
==========================================================================
I have VirtualBOX and a virtual server Ubuntu18 server on it with a bridged network adapter and an internal network adapter. I want to make access for any Windows 10 computer in my internal network through previously mentioned virtual server Ubuntu18. How can I do it permanently for Ubuntu18 server?

*Answer3*
To ensure the configuration to allow Windows 10 computers on your internal network to access services through your Ubuntu 18 virtual server remains persistent across reboots, you can make the changes permanent by modifying specific configuration files. Here's how you can achieve this:

1. **Enable IP Forwarding Permanently**:
   - Edit the sysctl configuration file to enable IP forwarding permanently:
     ```
     sudo nano /etc/sysctl.conf
     ```
   - Add the following line to the end of the file:
     ```
     net.ipv4.ip_forward=1
     ```
   - Save the file and apply the changes by running:
     ```
     sudo sysctl -p
     ```

2. **Configure IP Tables Permanently**:
   - Install the `iptables-persistent` package to save and restore IP tables rules across reboots:
     ```
     sudo apt-get install iptables-persistent
     ```
   - During installation, you will be prompted to save current IPv4 and IPv6 rules. Choose to save both.
   - Any time you make changes to your IP tables rules, you can save them using:
     ```
     sudo netfilter-persistent save
     sudo netfilter-persistent reload
     ```

3. **Configure Network Settings**:
   - Ensure that your network interfaces are configured correctly and persist across reboots. You can do this by editing the `/etc/network/interfaces` file.

4. **Set Up Services**:
   - Install and configure the necessary services on your Ubuntu server, such as setting up a web server, DNS server, or any other services you want to access from your Windows 10 computers.

5. **Firewall Configuration**:
   - If you have a firewall running on your Ubuntu server, ensure that you allow traffic on the necessary ports for the services you want to access.

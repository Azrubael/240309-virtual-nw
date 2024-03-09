# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  # Server_1 configuration
  config.vm.define "Server_1" do |s1|
    s1.vm.box = "ubuntu/bionic64"
    s1.vm.hostname = "server1"
    s1.vm.network "public_network", ip: "192.168.1.204", bridge: "wlp2s0"
    s1.vm.network "private_network", ip: "10.8.0.11", virtualbox__intnet: true
    s1.vm.network "private_network", ip: "10.9.0.11", virtualbox__intnet: true
    s1.vm.provider "virtualbox" do |vbs1|
      vbs1.memory = "800"
      vbs1.cpus = 1    
    end
    s1.vm.provision "file", source: "70-netplan-config.yaml", destination: "/tmp/70-netplan-config.yaml"
    s1.vm.synced_folder ".", "/vagrant", disabled: true
    s1.vm.provision "shell", path: "scripts/server1_script.sh"
  end


  # Client_1 configuration
  config.vm.define "Client_1" do |c1|
    c1.vm.box = "generic/centos8"
    c1.vm.hostname = "client1"
    c1.vm.network "private_network", ip: "10.8.0.12", virtualbox__intnet: true
    c1.vm.network "private_network", ip: "10.7.0.12", virtualbox__intnet: true
    c1.vm.provider "virtualbox" do |vbc1|
      vbc1.memory = "800"
      vbc1.cpus = 1    
    end
    c1.vm.synced_folder ".", "/vagrant", disabled: true
    c1.vm.provision "shell", path: "scripts/client1_script.sh"
  end


  # Client_2 configuration
  config.vm.define "Client_2" do |c2|
    c2.vm.box = "geerlingguy/ubuntu2004"
    c2.vm.hostname = "client2"
    c2.vm.network "private_network", ip: "10.9.0.13", virtualbox__intnet: true
    c2.vm.network "private_network", ip: "10.7.0.13", virtualbox__intnet: true
    c2.vm.provider "virtualbox" do |vbc2|
      vbc2.memory = "800"
      vbc2.cpus = 1    
    end
    c2.vm.synced_folder ".", "/vagrant", disabled: true
    c2.vm.provision "shell", path: "scripts/client2_script.sh"
  end

end
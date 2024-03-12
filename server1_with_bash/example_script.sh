#!/bin/bash

# Ensure that VirtualBox is installed
if ! command -v VBoxManage &> /dev/null
then
    echo "VirtualBox is not installed. Please install VirtualBox first."
    exit
fi

function create_vm {
    VM_NAME=$1
    ISO_PATH=$2
    OS_TYPE=$3
    RAM_SIZE=$4
    CPU_COUNT=$5
    DISK_SIZE=$6

    VBoxManage createvm --name $VM_NAME --ostype $OS_TYPE --register
    VBoxManage modifyvm $VM_NAME --memory $RAM_SIZE --cpus $CPU_COUNT
    VBoxManage createhd --filename $VM_NAME.vdi --size $DISK_SIZE
    VBoxManage storagectl $VM_NAME --name "SATA Controller" --add sata --controller IntelAhci
    VBoxManage storageattach $VM_NAME --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium $VM_NAME.vdi
    VBoxManage storageattach $VM_NAME --storagectl "SATA Controller" --port 1 --device 0 --type dvddrive --medium $ISO_PATH

    # Network settings 
    VBoxManage modifyvm $VM_NAME --nic1 bridged
    VBoxManage modifyvm $VM_NAME --bridgeadapter1 "wlp2s0"
    VBoxManage modifyvm $VM_NAME --nicproperty1 "ip" "192.168.1.204"
    VBoxManage modifyvm $VM_NAME --nic2 intnet
    VBoxManage modifyvm $VM_NAME --intnet2 "Net_1"
    VBoxManage modifyvm $VM_NAME --nicproperty2 "ip" "10.0.1.1"
    VBoxManage modifyvm $VM_NAME --nic3 intnet
    VBoxManage modifyvm $VM_NAME --intnet3 "Net_2"
    VBoxManage modifyvm $VM_NAME --nicproperty3 "ip" "10.0.3.1"


    VBoxManage guestcontrol $VM_NAME copyto server1_setup.sh /tmp/server1_setup.sh --username user --password password
    VBoxManage guestcontrol $VM_NAME execute --image /bin/bash --username user --password password --wait-exit --wait-stdout -- /tmp/server1_setup.sh

    VBoxManage --nologo guestcontrol $VM_NAME run --exe $VM_EXEC_PATH \
--username $VM_USER --password $VM_PASSWD --wait-stdout \
-- {$VM_EXEC}/arg0 $VM_ARGS

}


create_vm "Server_1" "/opt/ARCHIVES/Ubuntu/ubuntu-18.04.6-live-server-amd64.iso" "Ubuntu_64" 800 1 10000
VBoxManage startvm "Server_1"

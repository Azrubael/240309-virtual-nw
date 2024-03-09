# 2024-03-09  14:24
===================

# The goal of this project is to train in deploying and diagnosing a private virtual network with three virtual machines. Each virtual machine has a unique operating system. A Python script is provided to diagnose the state of the virtual network


[1] - To run the project you need installed VirtualBOX 6.1 or above and Vagrant 2.4 on Ubuntu 20.04 or newer.

```bash
vagrant up
```

[2] - If you want to connect to virtual machines
```bash
# Connect to Server_1
vagrant ssh Server_1
```
```bash
# Connect to Client_1
vagrant ssh Client_1
```
```bash
# Connect to Client_2
vagrant ssh Client_2
```

[3] - Creating an isolated environment to run a Python3 diagnostic script
```bash
sudo apt install python3.10-venv            # <--- only if you need it
python3 -m venv azenv
source azenv/bin/activate
pip install -r python_dependencies
```

[4] - To runn a script to obtain the virtual network configuration table
```bash
(azenv)$ python3 scripts/config_collection.py
```

[5] - Creating a list of dependencies
```bash
(azenv)$ pip freeze > python_dependencies
```


[6] - Deactivating an isolated environment
```bash
    (azenv)$ deactivate
```
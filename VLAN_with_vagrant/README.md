# 2024-03-12  17:23
===================

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

[3] - Creating an isolated environment
```bash
sudo apt install python3.10-venv            # <--- only if you need it
python3 -m venv azenv
source azenv/bin/activate
pip install -r python_dependencies
```

[4] - To runn a script to obtain the virtual network configuration table
```bash
(azenv)$ python3 scripts/pretty_config_collect_time.py
```

[5] - Creating a list of dependencies
```bash
(azenv)$ pip freeze > python_dependencies
```


[6] - Deactivating an isolated environment
```bash
    (azenv)$ deactivate
```
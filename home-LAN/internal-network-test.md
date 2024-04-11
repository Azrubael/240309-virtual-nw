2024-04-11  12:01
=================

*Question 1 to Codeium*
=============================================================================
Write a powershell script to check all the IP's that are using in my local network 192.168.1.0/24 at the moment. This script have to use background jobs to test the connections to multiple IP addresses concurrently, which should improve the speed of checking.


*Question 2 to Codeium*
=============================================================================
Write a python script for Windows 10 to ping all the IP's that are using in my local network 192.168.1.0/24 at the moment. This script have to use background jobs to test the connections to multiple IP addresses concurrently, which should improve the speed of checking.

```python
import ipaddress
import subprocess
import concurrent.futures


network = ipaddress.IPv4Network('192.168.1.0/24')


def ping(ip):
    try:
        result = subprocess.run(['ping', '-n', '1', str(ip)], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            return (ip, "is up")
        else:
            return (ip, "is down")
    except subprocess.TimeoutExpired:
        return (ip, "is down")


with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(ping, network.hosts())


for result in results:
    print(result[0], result[1])
```
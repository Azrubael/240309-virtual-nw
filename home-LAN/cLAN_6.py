import ipaddress
import subprocess
import concurrent.futures

network = ipaddress.IPv4Network('192.168.1.0/24')

def ping(ip):
    try:
        process = subprocess.Popen(['ping', '-n', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = process.communicate()
        if process.returncode == 0:
            return (ip, "is up")
        else:
            return (ip, "is down")
    except subprocess.TimeoutExpired:
        return (ip, "is down")

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(ping, network.hosts())

for result in results:
    # print(result)
    if "is down" in result[1]:
        print(f'Host {result[0]} is down')
    else:
        print(f'Host {result[0]} is up')

import json
import os
import re
from datetime import datetime
from tabulate import tabulate

"""This script provides diagnostics of a deployed computer network and displays the final information in tabular form."""


def save_pretty(pretty_data, file_path, file_ext='txt'):
    """Write data in text format to hard drive."""
    current_datetime = datetime.now()
    ms = str(round(current_datetime.timestamp() * 1e4))
    formatted_datetime = f"Created: {current_datetime.strftime('%Y-%m-%d %H:%M')}"
    save_path = 'reports/' + file_path + '_' + ms[3:12] + '.' + file_ext
    try:
        with open(save_path, 'w') as f:
            f.write(formatted_datetime)
            f.write('\n')
            f.write(pretty_data)
    except:
        print(f'File {file_path} writing error.')
    print('Data written to a file:', save_path)
    return formatted_datetime


def vagrant_vms_list():
    """Getting a list of virtual machines."""
    stream = os.popen("vagrant status | grep '(virtualbox)'").read()
    vagrant_env = stream.strip('\n').split('\n')
    return [vm.split()[0] for vm in vagrant_env]


def vagrant_dumps(statuses):
    """Convert a JSON to a string."""
    res = ''
    for i in statuses:
        res += str(i) + '\n' + json.dumps(statuses[i], indent=2)
    return res


def vms_hostnamectl(vms_list):
    """Collecting hostnamectl information for each virtual machine."""
    hostnamectl = {}
    for vm in vms_list:
        hostnamectl[vm] = {}
        stream = (os.popen(f'vagrant ssh {vm} -c hostnamectl').read()).strip('\n')
        lines = stream.split('\n')
        for line in lines:
            line = line.lstrip()
            colon = line.find(': ')
            key = line[:colon]
            val = line[colon+2:]
            if key == "Operating System":
                pattern = r'\u001b(.*?)\u0007'
                val = re.sub(pattern, '', val)
            hostnamectl[vm][key] = val
        vm_iproute = (os.popen(f"vagrant ssh {vm} -c 'ip route show default'").read()).strip('\n')
        answ = vm_iproute.split()
        hostnamectl[vm]['Default Gateway'] = ' '.join(answ[1:5])

    return hostnamectl


def vms_status(vms_list):
    """Collect detailed network configuration for running virtual machines."""
    status = {}
    for vm in vms_list:
        vm_hostname = (os.popen(f'vagrant ssh {vm} -c hostname').read()).strip('\n')
        stream = os.popen(f'vagrant ssh {vm} -c "ip -j addr"').read()
        status[vm_hostname] = json.loads(stream)

    return status


def total_json(hostnamectl_list, statuses_json):
    """Processing diagnostic information for output."""
    result = []
    for key in hostnamectl_list.keys():
        host = {}
        host['Device'] = key
        host['Hostname'] = hostnamectl_list[key]['Static hostname']
        host['Operating System'] = hostnamectl_list[key]['Operating System']
        ip_list = statuses_json[host['Hostname']]
        ip_addr = []
        mac_addr = []
        interfaces = []
        for el in ip_list:
            ip_data = {}
            mac_data = {}
            interface = {}
            interface[el['ifname']] = el['addr_info'][0]['label']
            ip_data[el['ifname']] = f"{el['addr_info'][0]['local']}/{el['addr_info'][0]['prefixlen']}"
            mac_data['MAC ' + el['ifname']] = el['address']
            interfaces.append(interface)
            ip_addr.append(ip_data)
            mac_addr.append(mac_data)
        host['Default Gateway'] = hostnamectl_list[key]['Default Gateway']
        host['Interface'] = interfaces
        host['IP Address'] = ip_addr
        host['MAC Adderess'] = mac_addr
        result.append(host)
    return result


def tab_gen(json_data):
    """Processing collected data to format as a table."""
    res = json_data.copy()
    for vm in res:
        for el in ['Interface', 'IP Address', 'MAC Adderess']:
            txt = ''
            for ip in vm[el]:
                item = str(list(ip.values())[0])
                if len(item) < 5: txt += f'  {item}  '
                else: txt += f'{item}\n'
            vm[el] = txt
    return res



vms_list = vagrant_vms_list()
hostnamectl_json = vms_hostnamectl(vms_list)
statuses_json = vms_status(vms_list)
out = total_json(hostnamectl_json, statuses_json)

result = tab_gen(out)
pretty_data = tabulate(result, headers="keys", tablefmt="grid", \
                       maxcolwidths=[20,20,32,32,7,20,32])

# save_pretty(vagrant_dumps(hostnamectl_json), 'virtual_machines', 'json')
# save_pretty(vagrant_dumps(statuses_json), 'virtual_network', 'json')
stamp = save_pretty(pretty_data, 'summary_table')

print(f'\n{stamp}\nDiagnostic information about the data of a virtual computer network running on the Virtualbox platform:\n')
print(pretty_data)
 
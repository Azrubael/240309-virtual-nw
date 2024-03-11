import json
import os
import re
from datetime import datetime


def save_json(json_data, file_path):
    """Write data in JSON format to hard drive"""
    ms = str(round(datetime.now().timestamp() * 1e4))
    save_path = 'reports/' + file_path + '_' + ms[3:12] + '.json'
    print('Path to the result file:', save_path)
    try:
        with open(save_path, 'w') as f:
            json.dump(json_data, f, indent=2)
    except:
        print(f'File {file_path} writing error.')


def vagrant_vms_list():
    """Getting a list of virtual machines"""
    stream = os.popen("vagrant status | grep '(virtualbox)'").read()
    vagrant_env = stream.strip('\n').split('\n')
    return [vm.split()[0] for vm in vagrant_env]


def vagrant_dumps(statuses):
    """Display detailed information about virtual machines"""
    for i in statuses:
        print(i)
        print(json.dumps(statuses[i], indent=2))


def vms_hostnamectl(vms_list):
    """Collecting hostnamectl information for each virtual machine"""
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
    """Collect detailed network configuration information for running virtual machines"""
    status = {}
    for vm in vms_list:
        vm_hostname = (os.popen(f'vagrant ssh {vm} -c hostname').read()).strip('\n')
        stream = os.popen(f'vagrant ssh {vm} -c "ip -j addr"').read()
        status[vm_hostname] = json.loads(stream)

    return status


def list2str(processed_list):
    txt = ''
    for el in processed_list:
        txt += f'\n\t{list(el.keys())[0]} => {list(el.values())[0]}'
    return txt


def total_json(hostnamectl_list, statuses_json):
    """Processing diagnostic information for output"""
    result = []
    for key in hostnamectl_list.keys():
        host = {}
        host['Device'] = key
        host['Hostname'] = hostnamectl_list[key]['Static hostname']
        host['Operating System'] = hostnamectl_list[key]['Operating System']
        ip_list = statuses_json[host['Hostname']]
        ip_addr = []
        mac_addr = []
        for el in ip_list:
            ip_data = {}
            mac_data = {}
            ip_data[el['ifname']] = f"{el['addr_info'][0]['local']}/{el['addr_info'][0]['prefixlen']}"
            mac_data['MAC ' + el['ifname']] = el['address']
            ip_addr.append(ip_data)
            mac_addr.append(mac_data)
        host['Default Gateway'] = hostnamectl_list[key]['Default Gateway']
        host['IP Addresses'] = ip_addr
        host['MAC Adderesses'] = mac_addr
        result.append(host)
    return result


def tab_gen(json_data):
    res = json_data.copy()
    for vm in res:
        for el in ['IP Addresses', 'MAC Adderesses']:
            vm[el] = list2str(vm[el])
    return res


vms_list = vagrant_vms_list()
hostnamectl_json = vms_hostnamectl(vms_list)
statuses_json = vms_status(vms_list)
out = total_json(hostnamectl_json, statuses_json)

'''
# Display information in JSON format
vagrant_dumps(statuses_json)
vagrant_dumps(hostnamectl_json)
[ print(json.dumps(el, indent=2)) for el in out ]
'''

# Display summary table
result_list = tab_gen(out)
for vm in result_list:
    for key,val in vm.items():
        print("{} : {}".format(key, val))
    print()

save_json(statuses_json, 'virtual_network')
save_json(hostnamectl_json, 'virtual_machines')
save_json(result_list, 'summary')

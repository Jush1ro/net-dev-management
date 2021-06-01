from netmiko import (ConnectHandler, NetMikoAuthenticationException,
                     NetMikoTimeoutException)

CSR = {
    'device_type': 'cisco_ios',
    'ip': 'ip_address',
    'username': 'user',
    'password': 'pass'
}

net_connect = ConnectHandler(**CSR)

output = net_connect.send_command('ping ip_address')
#output = net_connect.send_command('configure')
#commands = ['enable',
#            'configure',
#            'snmp access version v2 enable']
#output = net_connect.send_config_set(commands)

print (output)

net_connect.disconnect()

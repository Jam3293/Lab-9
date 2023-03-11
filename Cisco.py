import netmiko
import paramiko
from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
from getpass import getpass

user = input('Please input your username ')
secret = getpass('Please input your password ')

ciscoDevice = {
        'device_type': 'cisco_ios',
        'host': '192.168.32.2',
        'username': user,
        'password': secret
}

try:
    connection = ConnectHandler(**ciscoDevice)
except (NetMikoTimeoutException):
    print ('The following device timed out: ' + ciscoDevice['host'])
except (AuthenticationException):
    print('Authentication issues on remote system ' + ciscoDevice['host'])
except (SSHException):
    print('Failed to connect via SSH please try again ' + ciscoDevice['host'])


print('The script has completed successfully')

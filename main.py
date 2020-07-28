import socket


def main(host_name):
    socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_object.settimeout(5)
    ports_status = False
    open_ports = []

    print('Scanning...')

    for port in ports_list.values():
        if socket_object.connect_ex((host_name, port)):
            pass
        else:
            ports_status = True
            open_ports.append(port)

    if ports_status:
        print('[!] The following port(s) are open: ')
        for key in ports_list.keys():
            if ports_list[key] in open_ports:
                print('Port %i used for %s is open.' % (ports_list[key], key))
    elif not ports_status:
        print('[+] No common port was discovered to be open.\n')

    input('Press enter to exit.')


if __name__ == '__main__':
    print('Enter the name of a site (in the format: \'www.site.com\') or enter \'localhost\' to '
          + 'scan the device in use.')
    target_host = input()
    if target_host.lower() == 'localhost':
        host = socket.gethostname()
    else:
        host = socket.gethostbyname(target_host)

    ports_list = {
        'FTP': 21,
        'SSH': 22,
        'Telnet': 23,
        'SMTP': 25,
        'HTTP': 80,
        'POP': 110,
        'SMB': 137,
        'SMB': 138,
        'SMB': 139,
        'LDAP': 389,
        'SLP': 427,
        'HTTPS': 443,
        'AFP': 548,
        'RDP': 3389
    }

    main(host)

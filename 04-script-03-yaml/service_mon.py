#!/usr/bin/env python3

import dns.resolver
import json
import requests
import os
import signal
import time
import yaml

os.system("clear")

etl_dict = {}
# etl_dict = {'drive.google.com': {'64.233.162.194'},
#             'mail.google.com': {'64.233.165.18', '64.233.165.17', '64.233.165.19', '64.233.165.83'},
#             'google.com': {'64.233.162.139', '64.233.162.113', '64.233.162.102', '64.233.162.101',
#                            '64.233.162.138', '64.233.162.100'}}

services_list: list[str] = ['drive.google.com', 'mail.google.com', 'google.com']
query_type: str = 'A'
check_interval = 10
save_format: str = 'JSON'  # 'YAML' or 'JSON'


def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)


def url_ok(url):
    r = requests.head(url)
    return str(r.status_code) in ("200", "301", "302",)


def dns_resolve(fqdn):
    r = dns.resolver.resolve(fqdn, query_type, raise_on_no_answer=False)
    return r


def save_results(dict_to_save, save_fmt):
    with open(f'data.{save_fmt.lower()}', 'w') as f:
        if save_fmt == "JSON":
            json.dump(dict_to_save, f, indent=2)
        elif save_fmt == "YAML":
            yaml.dump(dict_to_save, f, indent=2)


signal.signal(signal.SIGINT, handler)

while 1:
    service_dict = {}
    for service in services_list:
        ip_list: list[str] = []
        answer = dns_resolve(service)
        for val in answer:
            ip = val.to_text()
            ip_list.append(ip)
            if service in etl_dict:
                if ip not in etl_dict[service]:
                    print(f'[ERROR] {service} IP mismatch: new IP {ip} not in the IP list {etl_dict[service]}')

        service_dict.update([(service, ip_list)])

        if url_ok(f'https://{service}'):
            service_status = 'Connection OK'
        else:
            service_status = 'Connection Failed'

        print(f'{service} - {service_dict[service]} - status {service_status}')

    etl_dict = service_dict

    save_results(etl_dict, save_format)

    time.sleep(check_interval)
    # os.system("clear")

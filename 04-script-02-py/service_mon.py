#!/usr/bin/env python3
from typing import List

import dns.resolver
import requests
import os
import time

os.system("clear")

etl_dict = {}
# etl_dict = {'drive.google.com': {'64.233.162.194'},
#             'mail.google.com': {'64.233.165.18', '64.233.165.17', '64.233.165.19', '64.233.165.83'},
#             'google.com': {'64.233.162.139', '64.233.162.113', '64.233.162.102', '64.233.162.101',
#                            '64.233.162.138', '64.233.162.100'}}

services_list: list[str] = ['drive.google.com', 'mail.google.com', 'google.com']
query_type: str = 'A'


def url_ok(url):
    r = requests.head(url)
    return r.status_code == 301  # 200


def dns_resolve(fqdn):
    r = dns.resolver.resolve(fqdn, query_type, raise_on_no_answer=False)
    return r


while 1:
    service_dict = {}
    for service in services_list:
        ip_list = set()
        answer = dns_resolve(service)
        for val in answer:
            ip = val.to_text()
            ip_list.add(ip)
            # print(f'{service} - {etl_dict[service]}')
            if service in etl_dict:
                if ip not in etl_dict[service]:
                    print(f'[ERROR] {service} IP mismatch: new IP {ip} not in the IP list {etl_dict[service]}')
            # print(f'{service} - {val.to_text()}')

        service_dict.update([(service, ip_list)])

        if url_ok(f'http://{service}'):
            service_status = 'Connection OK'
        else:
            service_status = 'Connection Failed'

        print(f'{service} - {service_dict[service]} - status {service_status}')
        # < URL сервиса > - < его IP >
        # print(service_dict[service])

    # print(service_dict)
    etl_dict = service_dict
    # print(etl_dict)

    time.sleep(2)
    # os.system("clear")

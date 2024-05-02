#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys

count = 0
file_size = 0
dic = {'200': 0, '301': 0, '400': 0, '401': 0,
       '403': 0, '404': 0, '405': 0, '500': 0}


def print_status(dic, file_size):
    """print file size information"""
    print(f'File size: {file_size}')
    for k, v in dic.items():
        if v != 0:
            print(f'{k}: {v}')


try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_status(dic, file_size)

        count += 1
        try:
            file_size += int(line.split()[-1])
            status_code = line.split()[-2]
            if status_code in dic:
                dic[status_code] += 1
        except Exception:
            pass
        print_status(dic, file_size)
except KeyboardInterrupt:
    print_status(dic, file_size)

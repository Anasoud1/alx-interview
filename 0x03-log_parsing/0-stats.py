#!/usr/bin/python3
"""  """
import sys
import re

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
        pattern = (r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} - \[\d{4}-\d{2}-\d{2} '
                   r'\d{2}:\d{2}:\d{2}.\d{6}\] "GET \/projects\/260 HTTP\/1.1"'
                   r' \d{1,3} \d+$')
        if re.match(pattern, line):
            if count != 0 and count % 10 == 0:
                print_status(dic, file_size)
            count += 1
            size = int(line.split()[-1])
            status_code = line.split()[-2]
            if status_code in dic:
                dic[status_code] += 1
            file_size += size
except KeyboardInterrupt:
    print_status(dic, file_size)

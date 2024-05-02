#!/usr/bin/python3
"""  """
import sys
import re


count = 0
file_size = 0
dic = {'count_200': 0, 'count_301': 0, 'count_400': 0, 'count_401': 0,
       'count_403': 0, 'count_404': 0, 'count_405': 0, 'count_500': 0}

try:
    for line in sys.stdin:
        pattern = (r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} - \[\d{4}-\d{2}-\d{2} '
                   r'\d{2}:\d{2}:\d{2}.\d{6}\] "GET \/projects\/260 HTTP\/1.1"'
                   r' \d{1,3} \d+$')
        count += 1
        size = int(line.split()[-1])
        status_code = line.split()[-2]
        if re.match(pattern, line):
            if count % 10 == 0:
                print(f'File size: {file_size}')
                for k, v in dic.items():
                    if v != 0:
                        print(f'{k.split("_")[1]}: {v}')
            for k, v in dic.items():
                if k.split("_")[1] == status_code:
                    dic[k] += 1
            file_size += size
except KeyboardInterrupt:
    print(f'File size: {file_size}')
    for k, v in dic.items():
        if v != 0:
            print(f'{k.split("_")[1]}: {v}')

#!/usr/bin/python3
""" Script to parse logs and display statistics """
import sys

stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '400': 0,
}
sizes = [0]
count = 0

def print_stats_code():
    """ Displays the statistics of status codes and the total file size """
    print('File size: {}'.format(sum(sizes)))
    for http_stats_code, count in sorted(stats.items()):
        if count:
            print('{}: {}'.format(http_stats_code, count))


try:
    for index, line in enumerate(sys.stdin, start=1):
        matches = line.rstrip().split()
        try:
            status_code = matches[-2]
            file_size = matches[-1]
            if status_code in stats.keys():
                stats[status_code] += 1
            sizes.append(int(file_size))
        except Exception:
            pass
        if index % 10 == 0:
            print_stats_code()
    print_stats_code()
except KeyboardInterrupt:
    print_stats_code()
    raise

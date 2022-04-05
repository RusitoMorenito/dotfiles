#!/usr/bin/env python3

import psutil
num = psutil.disk_usage('/')[2]/1000000000
res = "{:.1f}".format(num)
print(res, end='')

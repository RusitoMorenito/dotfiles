#!/usr/bin/env python3

import psutil
memory_gb = psutil.virtual_memory()[3]
if memory_gb > 1000000000:
	memory_gb = memory_gb / 1000000000
	res = "{:.2f}".format(memory_gb)
	print(res + "Gb", end='')
else:
	memory_gb = memory_gb / 1000000
	res = "{:.2f}".format(memory_gb)
	print(res + "Mb", end='')


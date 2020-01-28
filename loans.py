#!/usr/bin/env python3

import sys

years = int(sys.argv[2])
n = years * 12
interest = 0.053
i = interest / 12
PVa = int(sys.argv[1])

#A = PVa / 1 - (( 1 / pow(1+i, n) / i))

#A = PVa / (1 - ( 1 / pow(1+i, n)) / i )

A = (i * PVa) / (1 - pow(1+i, -n))

print(A)


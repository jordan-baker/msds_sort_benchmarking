import os
import sys
import csv
import math


for i in sys.stdin:
    i = float(i)
    key = math.floor(i*10)
    print('%s\t%s' % (key, i))


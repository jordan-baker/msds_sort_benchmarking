import os
import sys
import csv
import math
from operator import itemgetter


for i in sys.stdin:
    key, value = i.split(',', 1)
    value = value.strip('\n')
    value = float(value)
    print('%s\t%s' % (key, value))


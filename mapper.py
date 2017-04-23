#!/usr/bin/env python

#### MapReduce #####

import os
import sys
import csv
import pandas as pd
import math
import numpy as np


#temp = [0.1, -0.5, 0.9, 0.40, -0.8, -0.81, -0.88, -0.81, -0.82, -0.83, -0.87]
#
#key_list_10 = []
#key_list_9 = []
#key_list_8 = []
#key_list_7 = []
#key_list_6 = []
#key_list_5 = []
#key_list_4 = []
#key_list_3 = []
#key_list_2 = []
#key_list_1 = []
#key_list0 = []
#key_list1 = []
#key_list2 = []
#key_list3 = []
#key_list4 = []
#key_list5 = []
#key_list6 = []
#key_list7 = []
#key_list8 = []
#key_list9 = []
#key_list10 = []

for i in sys.stdin:
    i = float(i)
    key = math.floor(i*10)
    print('%s\t%s' % (key, i))

#    key_pair = [i, key]

#    if (key == -10):
#        key_list_10.append(key_pair)
#    elif (key == -9):
#        key_list_9.append(key_pair)
#    elif (key == -8):
#        key_list_8.append(key_pair)
#    elif (key == -7):
#        key_list_7.append(key_pair)
#    elif (key == -6):
#        key_list_6.append(key_pair)
#    elif (key == -5):
#        key_list_5.append(key_pair)
#    elif (key == -4):
#        key_list_4.append(key_pair)
#    elif (key == -3):
#        key_list_3.append(key_pair)
#    elif (key == -2):
#        key_list_2.append(key_pair)
#    elif (key == -1):
#        key_list_1.append(key_pair)
#    elif (key == 0):
#        key_list0.append(key_pair)
#    elif (key == 1):
#        key_list1.append(key_pair)
#    elif (key == 2):
#        key_list2.append(key_pair)
#    elif (key == 3):
#        key_list3.append(key_pair)
#    elif (key == 4):
#        key_list4.append(key_pair)
#    elif (key == 5):
#        key_list5.append(key_pair)
#    elif (key == 6):
#        key_list6.append(key_pair)
#    elif (key == 7):
#        key_list7.append(key_pair)
#    elif (key == 8):
#        key_list8.append(key_pair)
#    elif (key == 9):
#        key_list9.append(key_pair)
#    else:
#        key_list10.append(key_pair)
#        
#key_lists=[key_list_10, key_list_9, key_list_8, key_list_7, key_list_6, key_list_5,
#               key_list_4, key_list_3, key_list_2, key_list_1, key_list0, key_list1,
#               key_list2, key_list3, key_list4, key_list5, key_list6, key_list7,
#               key_list8, key_list9, key_list10]
#key_lists_neg=[key_list_10, key_list_9, key_list_8, key_list_7, key_list_6, key_list_5,
#               key_list_4, key_list_3, key_list_2, key_list_1, key_list0]
#key_lists_pos=[key_list1,key_list2, key_list3, key_list4, key_list5, key_list6, key_list7,
#               key_list8, key_list9, key_list10]              
#key_lists=[key_lists_neg,key_lists_pos]


#!/usr/bin/env python

import os
import csv
import sys
#import pandas as pd
import math
#import numpy as np
from operator import itemgetter
#up the recursion limit to avoid errors
sys.setrecursionlimit(100000)


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
   return(alist)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

   
   
current_key = -1
key = -2
value_list = []

for i in sys.stdin:
    key, value = i.split('\t', 1)
    key=int(key)
    value = value.strip('\n')
    value=float(value)
    current_key=int(current_key)
    if (current_key == key):
        value_list.append(value)
    else:
        output = quickSort(value_list)
        print(current_key, ': ', output)
        current_key = key
        value_list = []
        value_list.append(value)
    
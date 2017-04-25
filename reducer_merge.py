#!/usr/bin/env python

import os
import csv
import sys
#import pandas as pd
import math
#import numpy as np
from operator import itemgetter



def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist
    #print("Merging ",alist)
    
    

current_key = None
key = None
value_list = []

for i in sys.stdin:
    key, value = i.split('\t', 1)
    value = value.strip('\n')
    
    
    if (current_key == key):
        value_list.append(value)
    else:
        output = mergeSort(value_list)
        print(output)
        current_key = key
        value_list = []
        value_list.append(value)
   


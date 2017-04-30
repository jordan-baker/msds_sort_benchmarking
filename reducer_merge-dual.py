import os
import sys
import csv
import math
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
    
    

current_key = -1
key = -2
value_list = []
for i in sys.stdin:
    key, value = i.split('\t', 1)
    key=int(key)
    value = value.strip('\n')
    
    value=float(value)
    dic={}
    current_key=int(current_key)
    print(type(key))
    
    if (current_key == key):
        value_list.append(value)
    else:
        output = mergeSort(value_list)
        print(current_key, ": ", output)
        current_key = key
        value_list = []
        value_list.append(value)


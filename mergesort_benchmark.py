# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html

#http://stackoverflow.com/questions/6786990/find-out-time-it-took-for-a-python-script-to-complete-execution

import os
import csv
import pandas as pd
import math
import numpy as np
from datetime import datetime
import multiprocessing as mp
import random
random.seed(540)



mu, sigma = 0, 0.1 # mean and standard deviation
#s = list(np.random.normal(mu, sigma, 500000))
s1 = list(np.random.normal(mu, sigma, 10))
s2= list(np.random.normal(mu, sigma, 10))
s=[s1,s2]
t = np.random.normal(mu, sigma, 1000000)
u = np.random.normal(mu, sigma, 2000000)

ss = np.random.choice(100, 500000, replace=True)
tt = np.random.choice(100, 1000000, replace=True)
uu = np.random.choice(100, 2000000, replace=True)


# Define an output queue
output = mp.Queue()





##### Merge Sort #####
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
    #print("Merging ",alist)
    
    
##### Quick Sort #####
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
   

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


   
   
#### MapReduce #####
temp = [0.1, -0.5, 0.9, 0.40, -0.8, -0.81, -0.88, -0.81, -0.82, -0.83, -0.87]

def mapper(alist):
    
    startTime = datetime.now()

    
    key_list_10 = []
    key_list_9 = []
    key_list_8 = []
    key_list_7 = []
    key_list_6 = []
    key_list_5 = []
    key_list_4 = []
    key_list_3 = []
    key_list_2 = []
    key_list_1 = []
    key_list0 = []
    key_list1 = []
    key_list2 = []
    key_list3 = []
    key_list4 = []
    key_list5 = []
    key_list6 = []
    key_list7 = []
    key_list8 = []
    key_list9 = []
    key_list10 = []

    for i in alist:
        key = math.floor(i*10)
        key_pair = [i, key]

        if (key == -10):
            key_list_10.append(key_pair)
        elif (key == -9):
            key_list_9.append(key_pair)
        elif (key == -8):
            key_list_8.append(key_pair)
        elif (key == -7):
            key_list_7.append(key_pair)
        elif (key == -6):
            key_list_6.append(key_pair)
        elif (key == -5):
            key_list_5.append(key_pair)
        elif (key == -4):
            key_list_4.append(key_pair)
        elif (key == -3):
            key_list_3.append(key_pair)
        elif (key == -2):
            key_list_2.append(key_pair)
        elif (key == -1):
            key_list_1.append(key_pair)
        elif (key == 0):
            key_list0.append(key_pair)
        elif (key == 1):
            key_list1.append(key_pair)
        elif (key == 2):
            key_list2.append(key_pair)
        elif (key == 3):
            key_list3.append(key_pair)
        elif (key == 4):
            key_list4.append(key_pair)
        elif (key == 5):
            key_list5.append(key_pair)
        elif (key == 6):
            key_list6.append(key_pair)
        elif (key == 7):
            key_list7.append(key_pair)
        elif (key == 8):
            key_list8.append(key_pair)
        elif (key == 9):
            key_list9.append(key_pair)
        else:
            key_list10.append(key_pair)
            
    key_lists=[key_list_10, key_list_9, key_list_8, key_list_7, key_list_6, key_list_5,
                   key_list_4, key_list_3, key_list_2, key_list_1, key_list0, key_list1,
                   key_list2, key_list3, key_list4, key_list5, key_list6, key_list7,
                   key_list8, key_list9, key_list10]
    key_lists_neg=[key_list_10, key_list_9, key_list_8, key_list_7, key_list_6, key_list_5,
                   key_list_4, key_list_3, key_list_2, key_list_1, key_list0]
    key_lists_pos=[key_list1,key_list2, key_list3, key_list4, key_list5, key_list6, key_list7,
                   key_list8, key_list9, key_list10]              
    key_lists=[key_lists_neg,key_lists_pos]
    time=datetime.now() - startTime
    return key_lists, time

def reducer(a_list):
    startTime = datetime.now()
    for i in a_list:
            mergeSort(i)
            #quickSort(i)
    print(a_list)    
    time=datetime.now() - startTime
    return a_list, time

#output = mapreduce(s)


    
    
       
from multiprocessing.dummy import Pool as ThreadPool
pool=ThreadPool(2)
results=pool.map(mapper,s)

neg_list=results[0][0][0]+results[1][0][0]
pos_list=results[0][0][1]+results[1][0][1]
master_list=neg_list+pos_list
time_delta=[results[0][1],results[1][1]]
#results[0][1]/results[1][1]=time_delta
#results[0][0][0]=first negative list
#results[0][0][1]=first positive list

#####FIX THIS LATER--lists aren't in order #####
from multiprocessing.dummy import Pool as ThreadPool
pool=ThreadPool(2)
results=pool.map(reducer,master_list)    


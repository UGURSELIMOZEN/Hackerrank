#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    a = arr[n]
    for i in range(n) :
        if a < arr[n-i-1] :
            arr[n-i] = arr[n-i-1]        
                
        elif  a > arr[n-i-1] :
            arr[n-i] = a
            break
       
    if arr[0] > a :
        arr[0] = a   
        
def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        insertionSort1(i, arr)
        print(" ".join(map(str, arr)))
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

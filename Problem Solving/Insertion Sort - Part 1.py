#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    a = arr[n-1]
    for i in range(n) :
        if a < arr[n-i-1] :
            arr[n-i] = arr[n-i-1]        
            print(" ".join(map(str, arr)))
            
            
        elif  a > arr[n-i-1] :
            arr[n-i] = a
            print(" ".join(map(str, arr)))
            break
       
    if arr[0] > a :
        arr[0] = a   
        print(" ".join(map(str, arr)))
               
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

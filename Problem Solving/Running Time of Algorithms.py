#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def insertionSort1(n, arr):
    a = arr[n]
    shiftNumber1 = 0
    for i in range(n) :
        if a < arr[n-i-1] :
            arr[n-i] = arr[n-i-1]
            shiftNumber1 += 1        
                
        elif  a > arr[n-i-1] :
            arr[n-i] = a
            break
       
    if arr[0] > a :
        arr[0] = a   
    
    return shiftNumber1
 
def insertionSort2(n, arr):
    shiftNumber2 = 0
    for i in range(1, len(arr)):
        shiftNumber2 += insertionSort1(i, arr)
    
    return shiftNumber2
    
def runningTime(arr):
    return insertionSort2(n,arr)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

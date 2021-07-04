#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    equal = []
    equal.append(arr[0])  # assigning pivot element to equal array
    left = []
    right = []
    
    for i in range(len(arr)) :
        if arr[i] > arr[0] :
            right.append(arr[i])
        
        elif arr[i] < arr[0] :
            left.append(arr[i])
        
        else :
            continue  # first condition is arr[i] = arr[0] just to skip it  
                        # I used continue
    left = left + equal +right
    return left
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3

######################################

def equalStacks(h1, h2, h3):
    
    len1, len2, len3 = 0, 0, 0
    
    for item in range(0, len(h1)):    
        len1 = len1 + h1[item];
    
    for item in range(0, len(h2)):    
        len2 = len2 + h2[item];
    
    for item in range(0, len(h3)):    
        len3 = len3 + h3[item];  
    

    while len1 !=0 and len2 != 0 and len3 != 0 and (len1!=len2 or len2!=len3):
        if max(len1, len2, len3) == len1:
            len1 = len1 - h1[0]
            h1.pop(0)
        elif max(len1, len2, len3) == len2:
            len2 = len2 - h2[0]
            h2.pop(0)
        else:
            len3 = len3 - h3[0]
            h3.pop(0)
    else:
        if len1==len2 and len2==len3:
            return len1
        else:
            return 0
          
######################################
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

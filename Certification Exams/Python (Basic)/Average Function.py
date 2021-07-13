


#!/bin/python3

import math
import os
import random
import re
import sys


def avg (*nums) :
    my_sum = 0
    length = 0
    for num in nums:
        my_sum += num
        length += 1
        
    avg = float(my_sum / length)
    
    return avg


if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
    
    
    
    

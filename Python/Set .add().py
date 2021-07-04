# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

data = sys.stdin.readlines()
my_arr = []
for i in range(0 ,len(data)-1) :
    my_arr.append(data[i+1])
    
print(len(set(my_arr))-1)

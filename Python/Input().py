# Enter your code here. Read input from STDIN. Print output to STDOUT


import sys

data = sys.stdin.readlines() # it takes as input all lines to data list 
data1 = data[0].split()  # I splitted  x,k values to two pieces in the first item of list 
x = int(data1[0])
k = int(data1[1])
poly = data[1]

if eval(poly) == k : # when using eval(poly) it takes poly as polynomial expression.
     print("True")
else :
     print("False")

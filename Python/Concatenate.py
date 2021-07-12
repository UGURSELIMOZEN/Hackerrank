


import numpy 
import sys


P, N, M = map(int,input().split())
A = numpy.array([input().split() for _ in range(P)],int)
B = numpy.array([input().split() for _ in range(N)],int)
print(numpy.concatenate((A, B), axis = 0))



#    SECOND APPROACH     #

#data = sys.stdin.readlines()
#my_arr = []

#for i in range(1, len(data)) :
#    data[i] = data[i].split()
#    data[i] = [int(item) for item in data[i]]
#    my_arr.append(data[i])

#print(my_arr)



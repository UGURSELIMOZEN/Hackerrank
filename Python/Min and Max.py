


import numpy
n ,m  = map(int, raw_input().split())
my_array= numpy.array( [map(int, raw_input().split()) for i in range(n)])
min_arr= numpy.min(my_array, axis=1)
print (numpy.max(min_arr))







# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

data = sys.stdin.readlines()
my_data = []
for i in range(len(data)) :
    my_data.append(data[i].split())


a = set(my_data[1])
b = set(my_data[3])


first = a.difference(b)
last = b.difference(a)

output  = first.union(last)
output1 = sorted(set(map(int, output)))

for item in output1 :
    print(item)

    
    

    

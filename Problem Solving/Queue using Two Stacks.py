# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue(object):
    def __init__(self):
        self.q1 = []
        self.q2 = []
    
    def printFront(self):
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())
         
        return self.q2[-1]
        
    def dequeue(self):
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())
        
        return self.q2.pop()
        
    def enqueue(self, value):
        self.q1.append(value)
        
#############################
        
my_queue = Queue()        
length = int(input())
for item in range(length):
    my_values = map(int, input().split())
    my_values = list(my_values)
    if my_values[0] == 1:
        my_queue.enqueue(my_values[1])        
    elif my_values[0] == 2:
        my_queue.dequeue()
    else:
        print(my_queue.printFront())
    

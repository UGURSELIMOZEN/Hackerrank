if __name__ == '__main__':
    N = int(input())
    result = []

    for i in range(0,N) :
        my_data = input().split() 
        if my_data[0] == "insert" :
            result.insert(int(my_data[1]),int(my_data[2]))
            
        elif my_data[0] == "print" :
            print(result)
        
        elif my_data[0] == "remove" :
            result.remove(int(my_data[1]))
        
        elif my_data[0] == "append" :
            result.append(int(my_data[1]))
        
        elif my_data[0] == "sort" :
            result.sort()
        
        elif my_data[0] == "pop" :
            result.pop()
            
        elif my_data[0] == "reverse" :
            result.reverse() 

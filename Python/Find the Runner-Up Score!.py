


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_list = list(arr)
    a = max(my_list)
    
    
    while  a in  my_list :
        my_list.remove(a)
    
    print(max(my_list))
    
    
    

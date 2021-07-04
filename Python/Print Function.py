if __name__ == '__main__':
    n = int(input())
    result = []
    my_string=""
    for item in range(1,n+1) :  # first I took all items to result array
        result.append(item)
        
    for element in result :
        my_string = my_string + str(element)  # now I added  all items in str type to empty string
    
    print(my_string)

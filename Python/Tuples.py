if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) # this is in list type
    my_tuple = tuple(integer_list) # I casted to tuple type.
    print(hash(my_tuple)) # and computed with hash func. also printed

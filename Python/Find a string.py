def count_substring(string, sub_string):
    repeatedNumber = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string): # it is searching all letter groups in string for assigning with sub_string
            repeatedNumber += 1
    return repeatedNumber
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

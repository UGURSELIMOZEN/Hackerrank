def mutate_string(string, position, character):
    list_string = list(string)
    list_string[position] = str(character)
    string = ''.join(list_string)
    
    return string
  
  

 # This is second approach for function   
 
#  def mutate_string(string, position, character):
#       string = string[:position] + str(character) + string[position+1:]
#       return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

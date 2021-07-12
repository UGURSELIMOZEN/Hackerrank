


def wrapper(f):
    def fun(l):
        
        #First approach
        
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
        
        #Second approach
        
        #for i in range(len(l)):
        #    a = l[i]
        #    number = a[-10:]
        #    number1 = number[:5]
        #    number2 = number[5:10]
        #    total_number = '+91 ' + number1 +' ' + number2
            
    return fun
  
  
  
  

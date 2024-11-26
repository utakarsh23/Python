a = 'KJSS'

def let(a):
   
    count = 0
    for i in a:
        if(i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            count +=1
    if(a.__contains__('A') or a.__contains__('E') or a.__contains__('I') or a.__contains__('O') or a.__contains__('U')):
        return True, count
    else:
        return False, count
      
print(let(a))
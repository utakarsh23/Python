# Write a python to find out letter ‘A’ is available or not in given string and count how many times that
# letter is present
# Ex. str1=’KJSCE’
# ans-False
# count-0
a = 'KJSSE'

def let(a):
   
    count = 0
    for i in a:
        if(i == 'A'):
            count +=1
    if(a.__contains__('A')):
        return True, count
    else:
        return False, count
      
print(let(a))
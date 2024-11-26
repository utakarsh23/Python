## to check if string contains the prefix and is true return spaces+1 else return -1
str = "bro went to the mall"
finds = "the"
count = 1 # count starting from 1, as we can also have 0 but then we'll have to add 1 later in count
   
if(str.__contains__(finds)) : #if true in range of the foudn index of the substring
    for i in range((str.find(finds))): #checking all index
        if(str[i] == " ") : #if index == space
            count = count + 1   #count increment 
else : 
    print(-1) #else -1

if(count == -1):   #to prevent from printing twice
    print(count)
   

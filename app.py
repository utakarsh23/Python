## to check if string contains the prefix and is true return spaces+1 else return -1
str = "bro went to the mall"
finds = "the"
count = 1
   
if(str.__contains__(finds)) :
    for i in range((str.find(finds))):
        if(str[i] == " ") :
            count = count + 1   
else :
    print(-1)

if(count == -1):   
    print(count)
   

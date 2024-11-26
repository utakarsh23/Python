# Write a Python program that takes two strings as input from the user. The program should perform the
# following operations:

# Sample Input:
# String 1: "Hello123"
# String 2: "World456"
# Expected Output: "HELLOWORLD"

def removeNumbers(a): #(l)uck python libraries hahah
    li = []
    for i in range(len(a)-1):
        li.append(a[i])
        
    li2 = li.copy()    
    for word in li2: #force condition hehe
        if (word == '0' or word == '1' or word == '2' or word == '3' or word == '4' or word == '5' or word == '6' or word == '7' or word == '8' or word == '9'):  
            li.remove(word)

    x = ""
    for i in range(len(li)):
        x = x+li[i]
    return x
    
a = removeNumbers("hello12")
b = removeNumbers("word345")

ko = a+b
print(ko.upper())




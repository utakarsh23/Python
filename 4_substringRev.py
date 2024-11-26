# Write a Python program that takes a sentence from the user and prints the sentence in reverse order. For
# example, "Hello World" should be printed as "World Hello
# Write a program that extracts a substring from a given text, starting from the start index and ending at the
# end index. Print the extracted substring.

a = "Helllo World is cool"
w = " " 
l = w+a+w
li = []
for i in range(len(l)): #i for the 1st space
    for j in range(len(l)): # j for the spaces in front of i 
        if(l[i] == w): #1st space
            if(l[j] == w and j>i): #to check second space
                li.append(a[i : j-1]) #adding between the 1st space and second space
                break #break to prevent from additional to be added(a space bwtween two spaces)
  
print(li)
x = ""
for word in li:
    x = word + " " + x 
    
print(x) 
    

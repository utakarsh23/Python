# #Write a Python program that takes a string from the user, removes all vowels from the string, extracts the
# remaining letters, and sorts them in alphabetical order. The program should then print the sorted letters as
# a list.



a = "aeoputrd"
li = []
for i in range (len(a)):
        if(a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u"):
            pass
        else:
            li.append(a[i])
        

print(sorted(li))

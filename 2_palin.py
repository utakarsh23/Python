# Write a Python program that takes a list of words from the user, identifies and removes any words that
# are palindromes, and then sorts the remaining words in
# reverse alphabetical order. The program should finally print the updated list as a tuple.
# Sample Input:
# words = ['level', 'world', 'civic', 'python', 'madam', 'programming']
# Expected Output:
# ('world', 'python', 'programming')

li = []
def liAdd(x):
    while(x  != "stop") :
        x = input("Enter a value: ")
        li.append(x)
    return li
def palin(s):
    w = len(s)//2
    for i in range(w):
        if(s[i] != s[len(s)-1-i]):
            return False
    return True

li2 = li.copy()
def tu():
    li2 = li.copy() 
    for word in li2:
        if palin(word):  
            li.remove(word)
            
    w = tuple(li)     
    return w 

print(liAdd(""))
print(tu())
        
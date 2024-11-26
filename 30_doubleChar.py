# Write a Python program to count the number of strings in a given list where the string length is 3 or more
# and the string contains the same character at least twice.
# Sample List: ['hello', 'world', 'noon', 'abcd', 'aabbcc']
# Expected Result: 3
# Explanation: The strings "hello" (contains 'l' twice), "noon" (contains 'o' twice), and "aabbcc" (contains
# 'a', 'b', and 'c' twice each) meet the criteria.

def ks(s): #Lambda like func 
    count = 0
    for string in s:
        if len(string) >= 3 and any(string.count(char) > 1 for char in set(string)):
            count += 1
    return count

def ks1(s): #plane func
    count =0
    for string in s:
        if len(string) >= 3: 
            rep = False
            for char in string:  
                if string.count(char) > 1:
                    rep = True
                    break 
            if rep:
                count += 1
    return count


#can use any of the func(ks or ks1)
ls = ['hello', 'world', 'noon', 'abcd', 'aabbcc']
res = ks(ls)
res1 = ks1(ls)
print("Expected Result:", res)
print("Expected Result:", res1)
# Write a Python program to count the number of characters in a string.

# Sample String : 'google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
# Question String: ‘Somaiya University’

st = 'gooofle.com'
dict = {}
for i in range(len(st)):
    count = 0
    for j in range(len(st)):
        if(st[j] == st[i]):
            count +=1
    dict.update({st[i]: count})
  
print(dict)
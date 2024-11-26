# Write a Python program to count the number of strings where the string length is 2 or more and the first
# and last character are the same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

li = ['abc', 'xyz', 'aba', '1221', 'heheh', 'qq', 's']
count = 0
for i in li:
    if(len(i)>=2 and i[0] == i[len(i)-1]):
        count = count +1
        
print(count)
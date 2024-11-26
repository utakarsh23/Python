# Write a program to read a 5 digit number and then display the number in the following
# formats. Eg., if the user entered 12345, the result should be
# 12345 1
# 2345 12

a = 12345
s = str(a)
l = len(s)
for i in range(len(s)):
    print(s[i:],'         ', s[:i+1])
#binary ata hai ??
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and
# then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in
# a comma separated sequence.


a = [int(input("Enter 4 digit binary no. ")), int(input("Enter 4 digit binary no. ")), int(input("Enter 4 digit binary no. ")), int(input("Enter 4 digit binary no. "))]

li = []
for i in range(len(a)):
    if(a[i]%5 == 0):
         li.append(a[i])
         
x = ','
for i in li:
    print(i, ", ", end='') #print(i, end=', ')
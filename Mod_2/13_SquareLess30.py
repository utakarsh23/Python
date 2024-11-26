# Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
ls = []
for i in range(1, 6):
    i = i*i
    if(i<=30):
        ls.append(i)     
print(ls)
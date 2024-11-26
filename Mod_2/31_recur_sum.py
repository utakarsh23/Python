# Write a program to sum the series 1/2 + 2/3 + ......n/(n+1) .
n = 0
def sum(n):
    if(n == 1):
        return (1/2)
    i = n/(n+1)
    return i + sum(n-1)
print(sum(20))
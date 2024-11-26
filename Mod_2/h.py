n = 0
def sum(n):
    if(n == 1):
        return (1/2)
    i = n/(n+1)
    return i + sum(n-1)
print(sum(20))
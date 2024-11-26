#Write a python program to take list values as input parameters and returns another list without any duplicates.
li = []
def liAdd(x):
    while(x  != 12345) :
        x = int(input("Enter a value: "))
        li.append(x)


liAdd(1)

s = set(li)
print(s)
t = tuple(s)
print(t)
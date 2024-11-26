#Write a python program to take list values as input parameters and returns another list without any duplicates.
li = []
def liAdd(x):
    while(x  != "stop") :
        x = input("Enter a value: ")
        li.append(x)
    return li

liAdd("")
sets = set(li)
print(sets)

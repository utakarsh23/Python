
ni = 101
ni = str(ni)
count = 0
w = 0
for i in ni:
    w = (3*int(i))**(count) + w
    count+=1

print(w)
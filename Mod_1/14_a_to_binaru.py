#to convert into binary you have to sucessively divide the number by 2 and check with teh remainder:
#check readme for detailed image and explanation
li = []
a = 54
num_bin = a
quo = num_bin; #//firset quo will be num_bin
rem = 0; #//initialising rem to keep it universal 
while (quo!=0): #//if quo = 0, then the code sto(ps working 
    rem = quo%2 #//rem%2 will give the remainder(0 or 1 as div by 2)
    quo = quo//2 #//quo div by 2 will give next quotient
    li.append(rem)
    

li.reverse()
binary_string = ''.join(map(str, li))
print(binary_string)

#check readme to learn how digits gets converted into binary 
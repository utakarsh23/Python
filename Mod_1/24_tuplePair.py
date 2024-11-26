# Write a Python program that takes two tuples test_tuple1 and test_tuple2 and

# returns a list of all pair combinations of the two tuples.
# Input: test_tuple1(7,2), test_tuple2(7,8)
# Output : [(7,7),(7,8),(2,7),(2,8),(7, 7),(7,2),(8,2)]

tu1 = (7, 2)
tu2 = (7, 8)

for i in tu1:
    for j in tu2:
        print((i, j), end='')
        print((j, i), end='')
        
#Rough answer 
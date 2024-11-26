##Lists
# L.append(e) Adds an element at the end of the list
# L.clear() Removes all the elements from the list
# L.copy() Returns a copy of the list
# L.count(e) Returns the number of elements with the specified value
# L.extend(L2) Add the elements of a list (or any iterable), to the end of the current list
# L.index(e) Returns the index of the first element with the specified value
# L.insert(i,e) Adds an element at the specified position
# L.pop(i) Removes the element at the specified position
# L.remove(e) Removes the item with the specified value
# L.reverse() Reverses the order of the list
# L.sort() Sorts the list


#tuple are immutable, 
#list is mutable

li = ["utkarsh", "Dhruv", "Shaurya"]
li2 = ["Tripathi", "Pankhania", "Kesarwani"]
li3 = ["kemcho", "namaskar"]

print(li + li2) 
#Adds the list || ['utkarsh', 'Dhruv', 'Shaurya', 'Tripathi', 'Pankhania', 'Kesarwani']

print(li * 3) 
#Repeats the list || ['utkarsh', 'Dhruv', 'Shaurya', 'utkarsh', 'Dhruv', 'Shaurya', 'utkarsh', 'Dhruv', 'Shaurya']

print(li[1]) 
#Prints the second index || Dhruv

print(li[-1]) 
#Prints the last index || Kesarwani

print(li[1:3]) 
#Prints the index from 1 to 2 || ['Dhruv', 'Shaurya']

#|||||||||
li.append("Shresth") #adds 'Shresth' into the list 
print(li) 

li.insert(2, "Dhruv") #inserts 'Dhruv' at index 2 by moving index in front
print(li)

li.remove("Dhruv") #Removes 'Dhruv'
print(li)

print(li3)
li3.clear() #Clears the list
print(li3)

li4 = li2.copy()  #to copy the list
print(li4)


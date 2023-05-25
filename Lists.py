# Today we will be learning about list which is very cucial list a data type to store value of any type

l=[3,5,6] # This is a list
print(type(l)) # This is list type <class 'list'>
# similary use can access the string element using index like l[0],l[1]y

l[0]=45     # you can change the existing list it is mutable
print(l)     #[45, 5, 6]

# similar to string lsit also has -v indexing l[-1]

# "in" key word can be used in any iterable be it string be it tuple, list etc etc

# for example i can show you one
if 5 in l:         # In the above list 5 is prsent in l so condition is true
  print('true')

# Similar to string slicing you can slice a list l[start:end:jump index] similar to string slicig
print(l[1:3])  #[5, 6]
print(len(l))  # returns length of the list ex 3

# List comprehension 
lst=[i for i in range(5)]   #lst=[0, 1, 2, 3, 4]
lst1=[i for i in range(21) if i%2==0 ] #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#---------------------------------------------------------------
# list methods

l1=[i for i in range(8)]

l1.append(19) # append value at end of the existing list
l1.sort()# Sorts the list in ascending order 
l1.sort(reverse=True) # Sorts the list in descending order
l1.reverse() # reverse the original list its not equivalent to sorting 
l1.index(19) # retuens index of first occurance of 19 
print(l1.count(1)) # returns total number of occurance of 1 in the list

# How to copy a list
m=l1 # This is not copy  of list l1, this now m and l1 are same list if you do any change in one list the same will reflect in other list

# The right way of making a list copy is by using the copy method''
copylat=l1.copy() # This is how you should create

l1.insert(3,199)  # Insert method
print(l1)     #[0, 1, 2, 199, 3, 4, 5, 6, 7, 19]

extra=[100,200,300]
l1.extend(extra)  # extra list gets combined with l1 list

# You can create a new list by combining two lists
k=extra+l1
print(k)








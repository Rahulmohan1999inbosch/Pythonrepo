# Today we will be learning about tuple
t=(1,3,4,6)
print(t)
# To store one value in tuple you must do it this way 
t1=(1,) # Place a , after the element else python assumes it as an int typ , not tuple
#Note tuples are immutable just like string
print(t[0])  # accessing the tuple is same as list and -ve indexing is also similar to list

# you can use the 'in' method in tuple
if 1 in t:
    print('yes')

# slicing a tuple is similar how you do in list
t2=t[0:2]
print(t2)

# Revise the methods using methods on tuple and it is similar to list
# Multiply tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)  #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

#Concatenating tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)   #('a', 'b', 'c', 1, 2, 3)

#---------------------------------------------------------
# Tuple methods to apply methods on table you should first copy to list and then change the tuple
# but some methods like count ,index etc can stil work on tuple since we are not changing the existing tuple





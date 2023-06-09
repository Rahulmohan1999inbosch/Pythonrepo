#This is map filter and reduce are very important concepts

#MAP
l=[1,3,4,6,7,8]
#get the cube of all the elemets in the list 
#This can be done easily using map fuction rather than using old conventional method
#map(function,(iterable)) iterable can be a list ,string,tuple,map function returns a map object which you can type cast to list 

cube=lambda x:x*x*x  #
print(list(map(cube,l))) #cube of lists,here return type is substitution  [1, 27, 64, 216, 343, 512]


#FILTER function
filter1=lambda l:l>2
print(list(filter(filter1,l)))  #return type is a boolean [3, 4, 6, 7, 8]


#REDUCE function
#do a summation of all list elements ,map and filter are in built , but reduce should be imported, reduce method is present in functools module 
from functools import reduce 

lis=[3,4,5,6,7,8]
addition=lambda x,y:x+y
summation=reduce(addition,lis)
print(summation)







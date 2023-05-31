# Sets :-sets is a collection of well defined elements and there is no repeatation in sets
#Sets in python is used when you don't want to repeat the element again
s={2,2,4,6} # declare a set
print(s)   #{2, 4, 6}
#sets are un ordered collection of elements  order of input is not maintained in set 
#Sets are also immutable just like tuple and string
empty=set() #declaring empty set
print(type(empty))

for value in s:
    print(value)
# Sets :-sets is a collection of well defined elements and there is no repeatation in sets
#Sets in python is used when you don't want to repeat the element again
s={2,2,4,6} # declare a set
print(s)   #{2, 4, 6}
#sets are un ordered collection of elements  order of input is not maintained in set 
#Sets are also immutable just like tuple and string
empty=set() #declaring empty set
print(type(empty))

for value in s:   #This is how you can access the set element
    print(value)

##################################################################33
# Set methods whcih can be used to manipulate sets

s1={1,3,4,5,}  # set 1
s2={3,4,6,8}   # set 2

#union of two sets
print(s1.union(s2)) # output {1, 3, 4, 5, 6, 8}  s1 and s2 is unchanged since a new set is created

#Update the existing set
s1.update(s2) # performs s1 and s2 union and updates the result in s1
print(s1)  #output {1, 3, 4, 5, 6, 8}

#intersection 
print(s1.intersection(s2)) #prints the intersection between two sets  {8, 3, 4, 6}

#intersection is similar to update method of union
s2.intersection_update(s1)
print(s2)   #{8, 3, 4, 6}

#Symmetric difference is reverse of intersection and this alos generates new set
s3=s1.symmetric_difference(s2)
print(s1,s2,s3)  # {1, 3, 4, 5, 6, 8} {8, 3, 4, 6} {1, 5}  1 and 5 is not common in s1 and s2 so this is the output

#Difference method returs the difference of two sets
wwe={'Roman Reigns','Brock lesnar','Thriple H'}
ufc={'Brock lesnar','Khabib','conor'}
print(wwe.difference(ufc))  # output {'Roman Reigns', 'Thriple H'}
print(ufc.difference(wwe))   #{'Khabib', 'conor'}
# if you want to update the set you can use difference update method symmetric_differnce_update()

#isdisjoint 
#disjoint sets ->which is a exclussive they have no element in common , if the intersection of two sets is none then its a disjoint sets
print(wwe.isdisjoint(ufc)) #retus false

#issuperset
print(wwe.issuperset(ufc)) # False as wwe is not a super set of ufc 
#let us create a super set for demo
# This behaves just like our normal math
Endevor=wwe.union(ufc) #this is a super set
print(Endevor.issuperset(wwe)) #true
print(Endevor.issuperset(ufc))  #true
print(wwe.issubset(Endevor))   #true
print(ufc.issubset(Endevor)) #true

#adding  a new element to set add method
wwe.add('Randy_ortan') #{'Roman Reigns', 'Randy_ortan', 'Thriple H', 'Brock lesnar'}
print(wwe)

# to add more than one element update method
# to add multiple entry you can add them as a tuple
wwe.update(('john cena','Big show')) # {'john cena', 'Big show', 'Roman Reigns', 'Randy_ortan', 'Brock lesnar', 'Thriple H'}
print(wwe)

#removing elements from set
#remove()  /discard()
wwe.remove('Big show')
print(wwe) #{'Roman Reigns', 'Randy_ortan', 'john cena', 'Brock lesnar', 'Thriple H'}
#wwe.remove('Big show') # if Big show is not present and you try to remove him again remove method throws error

#use discard method instead which does not throw erroe if element is not present
wwe.discard('Big show') 
print(wwe)  ##{'john cena', 'Brock lesnar', 'Thriple H', 'Roman Reigns', 'Randy_ortan'}

#so based on your requirement you can use the methods

#pop() This element removes the last element of the set
print(wwe.pop()) #randomly it can pop element as sets are unordered but it wont remove that elements from the set

#del used to delete an entire set
del ufc

# clear all the elements in a set 
wwe.clear()
print(wwe)







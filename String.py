names="Rahul"
len1=len(names)
print(len1)
print(type(len1))
print(names[0:1]) # String slicing
print(names[-1]) # negative slicing  returns the last value of the string
#Note String is immutable
print(names[-3:-1]) #Rahul prints hu (goes from -1 to -2 not inculding -3)

#Quick Quiz :
nm="Harry"
print(nm[-2:-4]) # prints character present at -4 and -3 not including -2 so the output will be "rr"

#Strings metho
# after alterning a new string is generated but the existing string remians same as strings are immutable
s="Rahul"
print(s.upper()) # a new string is created
print(s.lower())
name="Harry  !!!!!!!!!  !!!!!!!!" 
print(name.rstrip('!')) # removes the trailing character ie if present as suffix
print(name.replace('Harry','john')) #replaces the occurance of harry with john in the string name
print(name.split(" ")) # this returns a list of space seperated 
print(name.capitalize()) # first chaeacter of the string becomes capital ie becomes capital
print(name.center(50)) #appends spaces to bring the string in center
print(name.count('Harry')) #gives the count of occurance of the name Harry in the string name 
print(name.startswith('Harry')) #returns a boolean value true or fasle 
print(name.endswith('Harry'))# returs a true if the string ends with Harry
#one more advace way of using starts with and endswith 
print(name.endswith('to',0,3)) # tthe string is first sliced from index 0 to 2 as 3 is  included later on the sliced string we apply the endswith function
print(name.startswith("Ha",0,3)) #works similarly with ends with also
print(name.index('H')) #returns index the fist occurace of the mentioned character if not present returns an exception and breaks the code flow
print(name.find('Ha')) #returns a similar to index method but if not found returns -1 the code flow is not interupted
print(name.isalnum()) #if alphanumeric returns True else false
print(name.isalpha())#checks alphabets
print(name.isdigit())#checks if only digit returns true
print(name.isspace()) #returns true if space is present
print(name.istitle())# if the string is not capitalize returns true else false
print(name.swapcase()) #swaps upper to lower and vice cersa
pr








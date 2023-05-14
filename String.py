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




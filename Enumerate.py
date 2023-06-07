#Enumerate fuction 
#Enumerate functio in python is a built in function that allows you to to loop over a sequence of iterables like list ,tuple ,string
#This is not valid for dictionaty as index is not available in dictionary

marks=[12,34,56,78,65,34]
for index ,mark in enumerate(marks): #the first variable will get the index and second variable will have the vlue
    print(mark,index)  
    #output
    # 12 0
    # 34 1
    # 56 2
    # 78 3
    # 65 4
    # 34 5

print("\n\n")
#You can also choose the start index
marks=[12,34,56,78,65,34]
for index ,mark in enumerate(marks,start=1): #the first variable will get the index and second variable will have the vlue
    print(mark,index)  
    # 12 1
    # 34 2
    # 56 3
    # 78 4
    # 65 5
    # 34 6


#I hope the above examples are pretty much clear, like how the code actually works
#you can explore more on this vis googling

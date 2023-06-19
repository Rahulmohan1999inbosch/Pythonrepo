#Walrus operrator in python , walrus operator was introduced 3.8 onwards 
#you can assign a vlaue from the expression
#syntax 
#   (assigned_value  :=(exprseeion)) This whole becomes one and then you can use this variable 
l=[1,2,34]
while(a:=len(l)>0):    #Like this you can assign the value with expressio in one single line
    l.pop()
    print('hello')


#combining walrus operator with while loop is sick
l=list()
while (food:=input("Enter food")) != "quit":
    l.append(food)
else:
    print(l)
    


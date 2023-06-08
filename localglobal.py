#Types of variable , local and global variables
#variables declared outside the scope of method its called global variable
#vauiles is nothig but named location ,
#you cannot access local variable , you can access gloabal variable inside and outside the function

x=4              #this x is a global variable
def func():
    x=5          #This  is a local variable its scope lies with in method
    print(x)
  
func()


y=34
def func1():
    global y    #By using global keyword you can change the values of global varible with in the function
    y=45

func1()
print(y)


#This is a concept of global , but changing the global variable via function is not a good practice



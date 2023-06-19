#Magic method , let us discuss more on this

#__init__ is a type of magic method
#magiv methods are used to do some special operations

class Employee:
    name='Rahul'

    def __len__(self):          #This is a magic method i have created
        return(len(self.name))

    def __str__(self):
        return f"Name of the student is {self.name}"
     
    def __relationship__(self):  #this won't work
        return f"Rashmi loves {self.name} very much"
   
obj=Employee()
print(obj.name)
#can you print the length the len of 0bj.name
#print(len(obj))   #This is not possible , to do that you should define a method 


print(len(obj)) #5 is the output

#####  __str__ __repr__ methods###########
print(str(obj))  #Name of the student is Rahul

##### custom made method for objects#####
#methods that are predefined in python can be redefined for objects using this , but you cannot create your own methods for redigfining


def __int__(number):
    number=number+5
    return str(number)

print(int(45))



  
# ############## Inheritance #################################################
# Inheritace can access all the methods of parent class but parent class cannot aceess the methods of child class
#This is single inheritance

class Employee:                     #This is a parent class 
    def __init__(self,name,id):
        self.name=name
        self.id=id

class programmer(Employee):         #This is a child class
    def display(self):
        print(f"name of the employee ---->{self.name}\n Employee id ----->{self.id}")


obj=Employee("Rahul",56)  #object of parent class 
obj1=programmer('Rashmi',57) #object of child class

print(obj.name)
#obj.display()    #error canot access child class 

#where as child can access all the content of the parent element
print(obj1.name)
print(obj1.id)
obj1.display()


################### access modifiers public,private and protected###################################




        
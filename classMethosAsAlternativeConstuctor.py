#Class method as alternative constructor, how to use this as alt constructor

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromstring(cls,string):
        return cls(string.split("-")[0],string.split("-")[1]) #This is code for class method as alt constructor 
    
string="Rahul-120000"
emp1=Employee.fromstring(string)
print(emp1.name)
print(emp1.salary)
    
#This is how you can use class method to use as an alternative constructor, so that you can easily format the data and pass as an argument to the class..



